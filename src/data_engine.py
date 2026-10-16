import os
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_synthetic_ehr(num_patients=50, random_seed=42):
    np.random.seed(random_seed)
    
    cities = ["Bengaluru", "Mumbai", "Delhi NCR", "Chennai", "Hyderabad", "Kolkata", "Pune", "Ahmedabad"]
    genders = ["Male", "Female"]
    
    patient_ids = [f"IND-T2D-{1000 + i}" for i in range(num_patients)]
    ages = np.random.randint(32, 74, size=num_patients)
    gender_list = np.random.choice(genders, size=num_patients, p=[0.58, 0.42])
    locations = np.random.choice(cities, size=num_patients)
    
    bmis = np.round(np.random.normal(25.8, 3.4, size=num_patients), 1)
    bmis = np.clip(bmis, 19.5, 36.0)
    
    waist_hip_ratio = np.where(
        gender_list == "Male",
        np.round(np.random.normal(0.96, 0.05, size=num_patients), 2),
        np.round(np.random.normal(0.89, 0.06, size=num_patients), 2)
    )
    
    visceral_adiposity_index = np.round(np.random.normal(4.2, 1.2, size=num_patients), 2)
    visceral_adiposity_index = np.clip(visceral_adiposity_index, 1.5, 8.5)
    
    t2d_duration = np.round(np.random.exponential(5.5, size=num_patients), 1)
    t2d_duration = np.clip(t2d_duration, 0.5, 25.0)
    
    hba1c = np.round(np.random.normal(8.1, 1.3, size=num_patients), 1)
    hba1c = np.clip(hba1c, 6.2, 12.5)
    
    fasting_glucose = np.round(hba1c * 17.5 + np.random.normal(0, 12, size=num_patients), 0)
    fasting_glucose = np.clip(fasting_glucose, 95, 260)
    
    systolic_bp = np.round(np.random.normal(134, 14, size=num_patients), 0)
    diastolic_bp = np.round(np.random.normal(84, 8, size=num_patients), 0)
    
    egfr = np.round(np.random.normal(82, 18, size=num_patients), 0)
    egfr = np.clip(egfr, 32, 115)
    
    serum_creatinine = np.round(140.0 / egfr + np.random.normal(0, 0.15, size=num_patients), 2)
    serum_creatinine = np.clip(serum_creatinine, 0.6, 2.8)
    
    total_cholesterol = np.round(np.random.normal(198, 32, size=num_patients), 0)
    triglycerides = np.round(np.random.normal(185, 48, size=num_patients), 0)
    hdl = np.round(np.random.normal(41, 7, size=num_patients), 0)
    ldl = np.round(total_cholesterol - hdl - (triglycerides / 5.0), 0)
    
    tcf7l2_carrier = np.random.binomial(1, 0.38, size=num_patients)
    
    metformin_mg = np.random.choice([0, 500, 1000, 1500, 2000], size=num_patients, p=[0.05, 0.15, 0.40, 0.25, 0.15])
    sulfonylurea_mg = np.random.choice([0, 1, 2, 4], size=num_patients, p=[0.35, 0.25, 0.25, 0.15])
    sglt2i_mg = np.random.choice([0, 10, 25], size=num_patients, p=[0.45, 0.35, 0.20])
    dpp4i_mg = np.random.choice([0, 50, 100], size=num_patients, p=[0.40, 0.30, 0.30])
    insulin_basal_units = np.where(hba1c > 9.0, np.random.choice([0, 10, 18, 24], size=num_patients, p=[0.3, 0.3, 0.25, 0.15]), 0)
    
    nephropathy_stage = np.where(egfr < 60, "Stage 3 CKD", np.where(egfr < 90, "Stage 2 Mild", "Normal"))
    retinopathy = np.random.choice(["None", "Non-Proliferative", "Proliferative"], size=num_patients, p=[0.62, 0.30, 0.08])
    
    ehr_df = pd.DataFrame({
        "patient_id": patient_ids,
        "age": ages,
        "gender": gender_list,
        "location": locations,
        "bmi": bmis,
        "waist_hip_ratio": waist_hip_ratio,
        "visceral_adiposity_index": visceral_adiposity_index,
        "t2d_duration_years": t2d_duration,
        "hba1c": hba1c,
        "fasting_glucose": fasting_glucose,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "egfr": egfr,
        "serum_creatinine": serum_creatinine,
        "total_cholesterol": total_cholesterol,
        "triglycerides": triglycerides,
        "hdl": hdl,
        "ldl": ldl,
        "tcf7l2_carrier": tcf7l2_carrier,
        "metformin_mg": metformin_mg,
        "sulfonylurea_mg": sulfonylurea_mg,
        "sglt2i_mg": sglt2i_mg,
        "dpp4i_mg": dpp4i_mg,
        "insulin_basal_units": insulin_basal_units,
        "nephropathy_stage": nephropathy_stage,
        "retinopathy": retinopathy
    })
    
    return ehr_df

def generate_patient_telemetry(ehr_row, days=7, random_seed=42):
    np.random.seed(random_seed + int(str(ehr_row["patient_id"])[-3:]))
    
    start_time = datetime(2026, 10, 1, 0, 0, 0)
    intervals_per_day = 288
    total_intervals = days * intervals_per_day
    
    timestamps = [start_time + timedelta(minutes=5 * i) for i in range(total_intervals)]
    
    base_glucose = ehr_row["fasting_glucose"]
    hba1c = ehr_row["hba1c"]
    metformin = ehr_row["metformin_mg"]
    sglt2i = ehr_row["sglt2i_mg"]
    sulfonylurea = ehr_row["sulfonylurea_mg"]
    insulin = ehr_row["insulin_basal_units"]
    
    drug_attenuation = (metformin * 0.008) + (sglt2i * 0.45)
    insulin_sensitivity = max(0.4, 2.5 - (ehr_row["visceral_adiposity_index"] * 0.22) - (hba1c * 0.08))
    
    cgm_readings = []
    heart_rates = []
    hrv_values = []
    step_counts = []
    sleep_stages = []
    carbs_logged = []
    bolus_logged = []
    
    current_glucose = base_glucose
    gut_glucose = 0.0
    active_insulin = 0.0
    
    for i, t in enumerate(timestamps):
        minute_of_day = t.hour * 60 + t.minute
        hour = t.hour
        is_sleeping = 23 <= hour or hour < 6
        
        carbs = 0.0
        bolus = 0.0
        steps = 0
        
        if not is_sleeping:
            if t.hour == 8 and t.minute == 30:
                carbs = np.random.uniform(45, 75)
            elif t.hour == 13 and t.minute == 30:
                carbs = np.random.uniform(60, 95)
            elif t.hour == 17 and t.minute == 15:
                carbs = np.random.uniform(15, 35)
            elif t.hour == 20 and t.minute == 30:
                carbs = np.random.uniform(55, 90)
                
            if np.random.rand() < 0.28:
                steps = int(np.random.gamma(shape=2.5, scale=40))
            else:
                steps = int(np.random.uniform(0, 15))
                
            if 7 <= t.hour <= 8 and t.minute == 0 and np.random.rand() < 0.6:
                steps = int(np.random.uniform(250, 650))
            elif 21 <= t.hour <= 22 and t.minute == 0 and np.random.rand() < 0.45:
                steps = int(np.random.uniform(180, 480))
        else:
            steps = 0
            
        if is_sleeping:
            if hour in [0, 1, 2]:
                stage = np.random.choice([1, 2], p=[0.4, 0.6])
            elif hour in [3, 4]:
                stage = np.random.choice([1, 3], p=[0.45, 0.55])
            else:
                stage = np.random.choice([0, 1], p=[0.3, 0.7])
        else:
            stage = 0
            
        if carbs > 0:
            gut_glucose += carbs * 1.85
            if insulin > 0 and carbs > 40:
                bolus = np.round(carbs / 12.0, 1)
                active_insulin += bolus * 8.0
                
        glucose_appearance = gut_glucose * 0.075
        gut_glucose = max(0.0, gut_glucose - glucose_appearance)
        
        dawn_drift = 0.0
        if 4 <= hour <= 7:
            dawn_drift = np.sin((minute_of_day - 240) / 240 * np.pi) * 0.8
            
        step_utilization = (steps / 100.0) * 1.65 * insulin_sensitivity
        
        basal_clearance = (current_glucose - base_glucose) * 0.025 * insulin_sensitivity
        
        sulf_drop = 0.0
        if sulfonylurea > 0 and 2 <= hour <= 5:
            sulf_drop = sulfonylurea * 0.65
            
        active_insulin_effect = active_insulin * 0.12 * insulin_sensitivity
        active_insulin = max(0.0, active_insulin * 0.94)
        
        net_change = (glucose_appearance + dawn_drift) - (basal_clearance + step_utilization + drug_attenuation * 0.02 + sulf_drop + active_insulin_effect)
        current_glucose = current_glucose + net_change + np.random.normal(0, 1.2)
        current_glucose = np.clip(current_glucose, 55, 340)
        
        if is_sleeping:
            hr = int(np.random.normal(58, 4))
            hrv = float(np.round(np.random.normal(52, 8), 1))
        else:
            hr_base = 72 + (steps / 50.0) * 8.0
            hr = int(np.clip(np.random.normal(hr_base, 5), 55, 145))
            stress_drop = 0.0
            if current_glucose > 200:
                stress_drop = 12.0
            elif current_glucose < 75:
                stress_drop = 18.0
            hrv = float(np.round(np.clip(np.random.normal(42 - stress_drop, 6), 12, 95), 1))
            
        cgm_readings.append(np.round(current_glucose, 1))
        heart_rates.append(hr)
        hrv_values.append(hrv)
        step_counts.append(steps)
        sleep_stages.append(stage)
        carbs_logged.append(round(carbs, 1))
        bolus_logged.append(round(bolus, 1))
        
    telemetry_df = pd.DataFrame({
        "timestamp": timestamps,
        "patient_id": ehr_row["patient_id"],
        "cgm_glucose": cgm_readings,
        "heart_rate": heart_rates,
        "hrv_rmssd": hrv_values,
        "step_count": step_counts,
        "sleep_stage": sleep_stages,
        "carbs_intake": carbs_logged,
        "insulin_bolus": bolus_logged
    })
    
    return telemetry_df

def extract_multimodal_features(ehr_df, telemetry_df, prediction_horizon_intervals=24):
    features_list = []
    patients = ehr_df["patient_id"].unique()
    
    ehr_indexed = ehr_df.set_index("patient_id")
    
    for pid in patients:
        p_telem = telemetry_df[telemetry_df["patient_id"] == pid].sort_values("timestamp").reset_index(drop=True)
        if len(p_telem) <= (prediction_horizon_intervals + 36):
            continue
            
        ehr = ehr_indexed.loc[pid]
        
        cgm = p_telem["cgm_glucose"].values
        hr = p_telem["heart_rate"].values
        hrv = p_telem["hrv_rmssd"].values
        steps = p_telem["step_count"].values
        carbs = p_telem["carbs_intake"].values
        sleep = p_telem["sleep_stage"].values
        timestamps = p_telem["timestamp"].values
        
        window_size = 24
        
        for idx in range(window_size, len(p_telem) - prediction_horizon_intervals, 3):
            sub_cgm = cgm[idx - window_size:idx]
            sub_hr = hr[idx - window_size:idx]
            sub_hrv = hrv[idx - window_size:idx]
            sub_steps = steps[idx - window_size:idx]
            sub_carbs = carbs[idx - window_size:idx]
            
            current_cgm = sub_cgm[-1]
            cgm_diff_15m = sub_cgm[-1] - sub_cgm[-4]
            cgm_diff_30m = sub_cgm[-1] - sub_cgm[-7]
            cgm_diff_60m = sub_cgm[-1] - sub_cgm[-13]
            
            cgm_mean_2h = np.mean(sub_cgm)
            cgm_std_2h = np.std(sub_cgm)
            cgm_min_2h = np.min(sub_cgm)
            cgm_max_2h = np.max(sub_cgm)
            cgm_auc_2h = np.sum(sub_cgm) * 5.0
            
            hr_mean_2h = np.mean(sub_hr)
            hrv_mean_2h = np.mean(sub_hrv)
            steps_1h = np.sum(sub_steps[-12:])
            carbs_1h = np.sum(sub_carbs[-12:])
            carbs_2h = np.sum(sub_carbs)
            
            target_glucose = cgm[idx + prediction_horizon_intervals]
            target_spike = 1 if target_glucose >= 180.0 else 0
            target_hypo = 1 if target_glucose <= 70.0 else 0
            
            features_list.append({
                "patient_id": pid,
                "timestamp": timestamps[idx],
                "age": ehr["age"],
                "gender": 1 if ehr["gender"] == "Male" else 0,
                "bmi": ehr["bmi"],
                "waist_hip_ratio": ehr["waist_hip_ratio"],
                "visceral_adiposity_index": ehr["visceral_adiposity_index"],
                "t2d_duration_years": ehr["t2d_duration_years"],
                "hba1c": ehr["hba1c"],
                "fasting_glucose": ehr["fasting_glucose"],
                "systolic_bp": ehr["systolic_bp"],
                "egfr": ehr["egfr"],
                "serum_creatinine": ehr["serum_creatinine"],
                "triglycerides": ehr["triglycerides"],
                "hdl": ehr["hdl"],
                "tcf7l2_carrier": ehr["tcf7l2_carrier"],
                "metformin_mg": ehr["metformin_mg"],
                "sulfonylurea_mg": ehr["sulfonylurea_mg"],
                "sglt2i_mg": ehr["sglt2i_mg"],
                "dpp4i_mg": ehr["dpp4i_mg"],
                "insulin_basal_units": ehr["insulin_basal_units"],
                "current_cgm": current_cgm,
                "cgm_diff_15m": cgm_diff_15m,
                "cgm_diff_30m": cgm_diff_30m,
                "cgm_diff_60m": cgm_diff_60m,
                "cgm_mean_2h": cgm_mean_2h,
                "cgm_std_2h": cgm_std_2h,
                "cgm_min_2h": cgm_min_2h,
                "cgm_max_2h": cgm_max_2h,
                "cgm_auc_2h": cgm_auc_2h,
                "hr_mean_2h": hr_mean_2h,
                "hrv_mean_2h": hrv_mean_2h,
                "steps_1h": steps_1h,
                "carbs_1h": carbs_1h,
                "carbs_2h": carbs_2h,
                "target_glucose_120m": target_glucose,
                "target_spike_120m": target_spike,
                "target_hypo_120m": target_hypo
            })
            
    return pd.DataFrame(features_list)

def build_curated_dataset():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)
    
    ehr_path = os.path.join(data_dir, "synthetic_ehr.csv")
    telemetry_path = os.path.join(data_dir, "synthetic_wearables.csv")
    profiles_path = os.path.join(data_dir, "patient_profiles.json")
    
    ehr_df = generate_synthetic_ehr(num_patients=25, random_seed=42)
    ehr_df.to_csv(ehr_path, index=False)
    
    all_telemetry = []
    for _, row in ehr_df.iterrows():
        t_df = generate_patient_telemetry(row, days=5, random_seed=101)
        all_telemetry.append(t_df)
        
    telemetry_df = pd.concat(all_telemetry, ignore_index=True)
    telemetry_df.to_csv(telemetry_path, index=False)
    
    profiles = []
    archetypes = [
        {"id": "IND-T2D-1000", "label": "Arun Sharma (58M, Bengaluru) - High Volatility, Postprandial Spikes"},
        {"id": "IND-T2D-1001", "label": "Priya Nair (49F, Chennai) - Controlled Baseline, Moderate Glycemic Drift"},
        {"id": "IND-T2D-1004", "label": "Rajesh Gupta (63M, Delhi NCR) - High Visceral Fat, Nocturnal Hypo Vulnerability"}
    ]
    for arch in archetypes:
        row = ehr_df[ehr_df["patient_id"] == arch["id"]].iloc[0].to_dict()
        row["display_label"] = arch["label"]
        profiles.append(row)
        
    with open(profiles_path, "w") as f:
        json.dump(profiles, f, indent=2)
        
    return ehr_df, telemetry_df

if __name__ == "__main__":
    build_curated_dataset()
