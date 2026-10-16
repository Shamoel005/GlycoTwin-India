import os
import json
import pandas as pd
from src.data_engine import generate_synthetic_ehr, generate_patient_telemetry, extract_multimodal_features, build_curated_dataset
from src.predictive_model import MultimodalGlycemicPredictor

def run_training_pipeline():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    ehr_path = os.path.join(data_dir, "synthetic_ehr.csv")
    telemetry_path = os.path.join(data_dir, "synthetic_wearables.csv")
    model_path = os.path.join(data_dir, "trained_model.pkl")
    metrics_path = os.path.join(data_dir, "model_metrics.json")
    
    if os.path.exists(ehr_path) and os.path.exists(telemetry_path):
        ehr_df = pd.read_csv(ehr_path)
        telemetry_df = pd.read_csv(telemetry_path)
    else:
        ehr_df, telemetry_df = build_curated_dataset()
        
    features_df = extract_multimodal_features(ehr_df, telemetry_df, prediction_horizon_intervals=24)
    features_df.to_csv(os.path.join(data_dir, "extracted_features.csv"), index=False)
    
    predictor = MultimodalGlycemicPredictor()
    metrics, importances = predictor.fit(features_df)
    
    predictor.save(model_path)
    importances.to_csv(os.path.join(data_dir, "feature_importances.csv"), index=False)
    
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
        
    print(f"Training completed successfully.")
    print(f"MAE: {metrics['mae']} mg/dL | RMSE: {metrics['rmse']} mg/dL | Clarke Zones A+B: {metrics['clarke_zone_ab_pct']}%")
    print(f"Spike Classification ROC-AUC: {metrics['roc_auc']} | F1-Score: {metrics['f1_score']}")
    
    return metrics

if __name__ == "__main__":
    run_training_pipeline()
