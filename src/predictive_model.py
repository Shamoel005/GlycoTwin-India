import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, roc_auc_score, f1_score, classification_report
from sklearn.preprocessing import StandardScaler

class MultimodalGlycemicPredictor:
    def __init__(self):
        self.feature_columns = [
            "age", "gender", "bmi", "waist_hip_ratio", "visceral_adiposity_index",
            "t2d_duration_years", "hba1c", "fasting_glucose", "systolic_bp",
            "egfr", "serum_creatinine", "triglycerides", "hdl", "tcf7l2_carrier",
            "metformin_mg", "sulfonylurea_mg", "sglt2i_mg", "dpp4i_mg", "insulin_basal_units",
            "current_cgm", "cgm_diff_15m", "cgm_diff_30m", "cgm_diff_60m",
            "cgm_mean_2h", "cgm_std_2h", "cgm_min_2h", "cgm_max_2h", "cgm_auc_2h",
            "hr_mean_2h", "hrv_mean_2h", "steps_1h", "carbs_1h", "carbs_2h"
        ]
        self.scaler = StandardScaler()
        self.regressor = GradientBoostingRegressor(
            n_estimators=140,
            learning_rate=0.06,
            max_depth=5,
            subsample=0.85,
            random_state=42
        )
        self.classifier_spike = GradientBoostingClassifier(
            n_estimators=120,
            learning_rate=0.05,
            max_depth=4,
            random_state=42
        )
        self.is_fitted = False
        
    def fit(self, features_df):
        X = features_df[self.feature_columns].values
        y_reg = features_df["target_glucose_120m"].values
        y_spike = features_df["target_spike_120m"].values
        
        X_train, X_test, y_reg_train, y_reg_test, y_spike_train, y_spike_test = train_test_split(
            X, y_reg, y_spike, test_size=0.2, random_state=42
        )
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        self.regressor.fit(X_train_scaled, y_reg_train)
        self.classifier_spike.fit(X_train_scaled, y_spike_train)
        self.is_fitted = True
        
        preds_reg = self.regressor.predict(X_test_scaled)
        preds_spike_prob = self.classifier_spike.predict_proba(X_test_scaled)[:, 1]
        preds_spike_bin = (preds_spike_prob >= 0.5).astype(int)
        
        mae = mean_absolute_error(y_reg_test, preds_reg)
        rmse = np.sqrt(mean_squared_error(y_reg_test, preds_reg))
        clarke_zone_ab = np.mean(np.abs(y_reg_test - preds_reg) <= (0.20 * y_reg_test)) * 100.0
        
        roc_auc = roc_auc_score(y_spike_test, preds_spike_prob)
        f1 = f1_score(y_spike_test, preds_spike_bin)
        
        feature_importances = pd.DataFrame({
            "feature": self.feature_columns,
            "importance": self.regressor.feature_importances_
        }).sort_values("importance", ascending=False).reset_index(drop=True)
        
        metrics = {
            "mae": round(float(mae), 2),
            "rmse": round(float(rmse), 2),
            "clarke_zone_ab_pct": round(float(clarke_zone_ab), 1),
            "roc_auc": round(float(roc_auc), 3),
            "f1_score": round(float(f1), 3),
            "test_sample_count": len(y_reg_test)
        }
        
        return metrics, feature_importances

    def predict(self, feature_dict):
        if not self.is_fitted:
            raise ValueError("Predictor is not fitted yet.")
            
        x_vector = np.array([[feature_dict[col] for col in self.feature_columns]])
        x_scaled = self.scaler.transform(x_vector)
        
        pred_glucose = float(self.regressor.predict(x_scaled)[0])
        pred_spike_prob = float(self.classifier_spike.predict_proba(x_scaled)[0, 1])
        
        current_g = feature_dict["current_cgm"]
        curve_intervals = [15, 30, 45, 60, 75, 90, 105, 120]
        curve = []
        delta_total = pred_glucose - current_g
        
        for t in curve_intervals:
            fraction = 1.0 / (1.0 + np.exp(- (t - 60) / 18.0))
            projected = current_g + (delta_total * fraction)
            curve.append({
                "minute": t,
                "projected_glucose": round(float(projected), 1),
                "lower_bound": round(float(projected - 12.0), 1),
                "upper_bound": round(float(projected + 14.5), 1)
            })
            
        hypo_prob = 0.05
        if pred_glucose < 85.0:
            hypo_prob = 0.78
        elif pred_glucose < 100.0 and feature_dict["sulfonylurea_mg"] > 0:
            hypo_prob = 0.42
            
        return {
            "predicted_glucose_120m": round(pred_glucose, 1),
            "spike_probability": round(pred_spike_prob, 3),
            "hypo_probability": round(hypo_prob, 3),
            "risk_category": "Critical Spike Hazard" if pred_spike_prob >= 0.75 else ("Elevated Volatility" if pred_spike_prob >= 0.45 else "Nominal Homeostasis"),
            "trajectory_curve": curve
        }

    def save(self, filepath):
        joblib.dump({
            "scaler": self.scaler,
            "regressor": self.regressor,
            "classifier_spike": self.classifier_spike,
            "feature_columns": self.feature_columns,
            "is_fitted": self.is_fitted
        }, filepath)

    def load(self, filepath):
        bundle = joblib.load(filepath)
        self.scaler = bundle["scaler"]
        self.regressor = bundle["regressor"]
        self.classifier_spike = bundle["classifier_spike"]
        self.feature_columns = bundle["feature_columns"]
        self.is_fitted = bundle["is_fitted"]
