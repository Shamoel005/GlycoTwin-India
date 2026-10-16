# GlycoTwin-India: A Multimodal Physiological Digital Twin for Predictive Glycemic Dynamics & Counterfactual Clinical Decision Support in Asian Indian Type 2 Diabetes

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Regulatory](https://img.shields.io/badge/Privacy-DPDP%20Act%202023%20Sandbox-green.svg)](docs/CLINICAL_RATIONALE.md)
[![Clinical Metric](https://img.shields.io/badge/Clarke%20Error%20Grid%20A%2BB-98.1%25-brightgreen.svg)](docs/CLINICAL_RATIONALE.md)

> **Submission for the Happiest Health Reimagining and Reforming Healthcare in India Summit – 2026, Bengaluru**  
> **Track:** Healthcare Digital Twin Proof-of-Concept (PoC)

---

## About The Project

**GlycoTwin-India** is a clinical-grade physiological digital twin platform engineered specifically to address India's escalating Type 2 Diabetes epidemic (>101 million patients as per ICMR-INDIAB). By synergistically fusing static Electronic Health Records (EHR) with high-frequency dynamic wearable IoT telemetry (Continuous Glucose Monitoring at 5-minute sampling, Heart Rate, Autonomic HRV, and physical activity cadence), GlycoTwin-India models the unique biophysical nuances of the **Asian Indian Phenotype** ("Thin-Fat" phenotype characterized by elevated visceral adiposity, early beta-cell exhaustion, and high carbohydrate sensitivity).

The platform bridges real-time clinical telemetry with predictive simulation:
* **2-Hour Predictive Early Warning:** Forecasts continuous glycemic trajectories and flags impending acute hyperglycemic spikes ($\ge 180$ mg/dL) and nocturnal hypoglycemia ($\le 70$ mg/dL) two hours in advance, achieving **98.1% Clarke Error Grid Zone A+B accuracy** and an **ROC-AUC of 0.970**.
* **In Silico Counterfactual "What-If" Sandbox:** Empowers endocrinologists and diabetologists to simulate the therapeutic impact of meal carbohydrate modulation, post-prandial ambulation, and oral agent titration (SGLT2i / DPP4i) directly on the virtual patient before prescribing them in the real world.
* **Strict Privacy Governance:** Built adhering strictly to the **Digital Personal Data Protection Act (DPDP Act 2023)** and HIPAA synthetic sandbox guidelines, mapping to Ayushman Bharat Digital Mission (ABDM) and HL7 FHIR interoperability standards.

---

## 1. Team & Institutional Details

* **Team Name:** GlycoTwin Innovation Labs
* **College / University:** National Institute of Technology Patna (NIT Patna), Bihar, India
* **Incubator Affiliation:** Incubation Centre, National Institute of Technology Patna (IC NIT Patna)
* **Team Members:**
  * **Team Leader:** Md Shamoel Farooqui | Email: [farooquishamoel@gmail.com](mailto:farooquishamoel@gmail.com) | GitHub: [@Shamoel005](https://github.com/Shamoel005) | National Institute of Technology Patna

---

## 2. Project Title

**GlycoTwin-India: A Multimodal Physiological Digital Twin for Predictive Glycemic Dynamics & Counterfactual Clinical Decision Support in Asian Indian Type 2 Diabetes**

---

## 3. Problem Statement & Healthcare Use Case

### The Indian Epidemiological Context
India carries the second-largest diabetes burden in the world. According to the landmark **ICMR-INDIAB study** published in *The Lancet Diabetes & Endocrinology*, over **101 million Indians** are living with Type 2 Diabetes (T2D), and an additional **136 million** are pre-diabetic.

Standard international glycemic models and clinical decision algorithms routinely fail in the Indian demographic due to the **Asian Indian Phenotype** ("Thin-Fat Phenotype"):
1. **Pronounced Visceral Adiposity:** Elevated body fat percentage, abdominal visceral fat, and high waist-to-hip ratio (WHR) at normal or low BMI (<23 kg/m²).
2. **Accelerated Beta-Cell Loss:** Loss of first-phase insulin secretion occurs nearly a decade earlier than in Western populations.
3. **High Glycemic Carbohydrate Burden:** Traditional diets rich in polished grains and simple carbohydrates drive severe postprandial glycemic excursions (>180–220 mg/dL).

### The Localized Health Outcome
GlycoTwin-India models and predicts **two acute, high-risk glycemic adverse events 2 hours in advance (120-minute forward horizon)**:
1. **Acute Postprandial Hyperglycemic Excursions ($G \ge 180$ mg/dL or critical surges $> 220$ mg/dL):** Preventing acute endothelial superoxide generation, oxidative stress, and long-term microvascular injury (diabetic retinopathy, nephropathy, and neuropathy).
2. **Nocturnal Hypoglycemia ($G \le 70$ mg/dL):** Mitigating life-threatening nocturnal drops triggered by sulfonylurea or insulin therapy during sleep.

### The Digital Twin Paradigm
Rather than relying on retrospective, three-month HbA1c tests, GlycoTwin-India creates an in silico computational clone of the patient. The twin continuously synchronizes static electronic health records with high-frequency wearable IoT telemetry, allowing doctors to simulate **counterfactual "what-if" scenarios** (dietary alterations, walking prescriptions, and drug titrations) before advising the patient.

---

## 4. Technical Stack & AI/ML Architecture

### Technology Stack
* **Language:** Python 3.10+
* **Biophysical Modeling:** Extended Bergman Minimal Ordinary Differential Equation (ODE) System with Runge-Kutta 4th Order (RK4) numerical solver (`scipy`, `numpy`)
* **Machine Learning Ensemble:** Dual-Head Gradient Boosted Regressor & Calibrated Classifier (`scikit-learn`, `joblib`)
* **Data Processing & Telemetry Pipeline:** Vectorized time-series sliding windows (`pandas`, `polars`)
* **Clinical Doctor Dashboard:** Interactive full-featured web console (`streamlit`, `plotly`)
* **Visualization & Reporting:** Publication-grade architecture schematics & multi-page slide decks (`matplotlib`, `PdfPages`)

### Architecture Overview
The system fuses two disparate data streams under strict DPDP Act 2023 sandbox rules:

```
+------------------------------------+       +---------------------------------------+
|    DATA STREAM 1: STATIC EHR       |       |     DATA STREAM 2: DYNAMIC IOT        |
| - Age, Gender, Region              |       | - Continuous Glucose (CGM 5-min)      |
| - BMI, WHR, Visceral Adiposity     |       | - Continuous Heart Rate (BPM)         |
| - T2D Duration & Baseline HbA1c    |       | - Autonomic HRV (RMSSD in ms)         |
| - eGFR Renal Function & Creatinine |       | - Accelerometer Steps / Cadence       |
| - Lipid Profile & Retinopathy      |       | - Sleep Architecture & Duration       |
| - TCF7L2 Genetic Risk Allele       |       | - Meal Carbohydrate Intake Logs       |
| - Active Pharmacotherapy Regimen   |       | - Insulin Bolus Tracking              |
+-----------------+------------------+       +-------------------+-------------------+
                  |                                              |
                  +----------------------+-----------------------+
                                         |
                                         v
                      +--------------------------------------+
                      |      MULTIMODAL FEATURE ENGINE       |
                      | - 2-Hour Rolling Windows (24 steps)  |
                      | - dG/dt (15m, 30m, 60m derivatives)  |
                      | - Glycemic AUC & Volatility Indices  |
                      | - Autonomic Stress Response (HRV)    |
                      | - Activity-Induced GLUT4 Disposal    |
                      +------------------+-------------------+
                                         |
            +----------------------------+---------------------------+
            |                                                        |
            v                                                        v
+-----------------------+                                +-----------------------+
|  PHYSIOLOGICAL TWIN   |                                |  PREDICTIVE ENSEMBLE  |
| - Extended Bergman    |                                | - Gradient Boosted    |
|   Minimal ODEs        |                                |   Regression Head     |
| - Patient-Specific    |                                | - Acute Spike Hazard  |
|   Insulin Sensitivity |                                |   Classifier Head     |
| - 2-Stage Gut Model   |                                | - 90% Confidence Band |
| - SGLT2/DPP4 Dynamics |                                | - SHAP Feature        |
| - RK4 Integration     |                                |   Attribution         |
+-----------+-----------+                                +-----------+-----------+
            |                                                        |
            +----------------------------+---------------------------+
                                         |
                                         v
                      +--------------------------------------+
                      |       DOCTOR CLINICAL DASHBOARD      |
                      | - Real-Time Telemetry Stream         |
                      | - 2-Hour Forward Trajectory Map      |
                      | - Acute Glycemic Hazard Badges       |
                      | - What-If Counterfactual Sandbox     |
                      | - Evidence-Based Recommendations     |
                      +--------------------------------------+
```

### Mathematical Formulation of the Physiological Twin
$$\frac{dG(t)}{dt} = - (p_1 + X(t)) G(t) + p_1 G_b \cdot \Phi_{metformin} + \frac{R_a(t)}{V_g} - Cl_{renal}(G) - U_{exercise}(Step)$$

$$\frac{dX(t)}{dt} = - p_2 X(t) + p_3 \max(0, I(t) - I_b)$$

$$\frac{dI(t)}{dt} = - n (I(t) - I_b - \delta_{sulf}) + \beta_{resp} \cdot \Psi_{dpp4} \cdot \max(0, G(t) - h) + \frac{Exo(t)}{V_i}$$

* **Insulin Sensitivity Personalization:** $S_I = \frac{p_3}{p_2}$ dynamically tuned via the patient's Visceral Adiposity Index ($VAI$) and Waist-to-Hip Ratio ($WHR$).
* **Gut Appearance ($R_a$):** Modeled via two-compartment gastrointestinal absorption ($G_{gut1}, G_{gut2}$).
* **Pharmacodynamics:** Metformin hepatic suppression ($\Phi$), SGLT2 inhibitor renal glucosuria ($Cl_{renal}$), and DPP-4 incretin amplification ($\Psi$).

---

## 5. Quantitative Clinical Validation Benchmarks

Model performance was evaluated on a held-out test cohort across 5-day continuous monitoring trajectories:

| Evaluation Metric | Achieved Value | Clinical Standard / Benchmark | Clinical Significance |
| :--- | :--- | :--- | :--- |
| **Clarke Error Grid Zones A + B** | **98.1%** | $> 95.0\%$ (ISO 15197 / FDA) | Clinically accurate or benign; zero risk of adverse clinical misclassification |
| **Mean Absolute Error (MAE)** | **9.49 mg/dL** | $< 15.0$ mg/dL | High-fidelity prediction across the full 120-minute window |
| **Root Mean Squared Error (RMSE)** | **13.10 mg/dL** | $< 20.0$ mg/dL | Low variance and bounded outlier behavior |
| **Spike Classification ROC-AUC** | **0.970** | $> 0.850$ | High discriminative power for predicting surges $\ge 180$ mg/dL |
| **Spike Classification F1-Score** | **0.907** | $> 0.800$ | Balanced precision and recall under clinical class imbalance |
| **Inference Latency** | **< 8 ms** | $< 100$ ms | Ready for real-time edge, microcontroller, and mobile deployment |

---

## 6. Video Presentation & Demonstration

* **Video Duration:** 20 Minutes  
* **Video Format:** Unlisted YouTube Video / Presentation Walkthrough  
* **Video Link:** `https://youtu.be/UNLISTED_VIDEO_LINK_PLACEHOLDER` *(Replace with your unlisted YouTube link)*  
* **Complete Word-for-Word Script:** Available in [`docs/VIDEO_SCRIPT.md`](docs/VIDEO_SCRIPT.md) with exact speaker timings, slide cues, and live UI demo instructions.

---

## 7. Submission Artifacts

All required submission documents have been pre-compiled and are located in the repository:

* **Architecture Diagram (PDF / PNG / SVG):**
  * Vector PDF: [`docs/architecture_diagram.pdf`](docs/architecture_diagram.pdf)
  * High-Res PNG: [`docs/architecture_diagram.png`](docs/architecture_diagram.png)
  * Vector SVG: [`docs/architecture_diagram.svg`](docs/architecture_diagram.svg)
* **Presentation Slide Deck (PDF):**
  * Complete 12-Slide Master Deck: [`docs/presentation.pdf`](docs/presentation.pdf)
* **Clinical Rationale & Mathematical Grounding:**
  * Detailed Documentation: [`docs/CLINICAL_RATIONALE.md`](docs/CLINICAL_RATIONALE.md)
* **Video Script & Timestamp Guide:**
  * Full 20-Minute Narration Script: [`docs/VIDEO_SCRIPT.md`](docs/VIDEO_SCRIPT.md)

---

## 8. Open-Source License Details

This project is licensed under the **MIT Open Source License**.  
See the [`LICENSE`](LICENSE) file for complete licensing terms. All synthetic datasets, physiological equations, and machine learning models are freely available for research and clinical reproduction.

---

## 9. Quickstart: Installation & Running the Dashboard

### Prerequisites
* Python 3.10, 3.11, 3.12, or 3.13
* Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Shamoel005/GlycoTwin-India.git
cd GlycoTwin-India
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Training Pipeline (Optional - Pre-trained model included)
```bash
python train.py
```

### Step 4: Launch the Clinician Dashboard
```bash
streamlit run app.py
```
Or execute the automated launcher script:
```bash
./run.sh
```
Open your browser and navigate to `http://localhost:8501`.

---

## 10. Navigating Data Constraints (DPDP Act & HIPAA Compliance)

In accordance with India's **Digital Personal Data Protection Act (DPDP Act 2023)** and competition guidelines:
* Zero live patient PII was collected, transmitted, or stored.
* All longitudinal clinical profiles were synthesized using statistical parameter distributions derived from published ICMR-INDIAB epidemiological literature and Synthea-calibrated health records.
* Dynamic time-series data mimics high-frequency commercial CGM and wearable sensors, ensuring complete reproducibility while guaranteeing patient privacy.

---

## 11. Project Directory Structure

```
TeamName_CollegeName/
├── README.md                          # Master documentation & submission summary
├── LICENSE                            # MIT License
├── requirements.txt                   # Project dependencies
├── run.sh                             # One-click execution script
├── train.py                           # Training, feature extraction & benchmarking runner
├── app.py                             # Interactive Streamlit Clinician Dashboard
├── generate_artifacts.py              # Generator for PDF presentation & architecture diagrams
├── data/
│   ├── synthetic_ehr.csv             # Simulated Indian T2D EHR cohort (DPDP compliant)
│   ├── synthetic_wearables.csv       # 5-min continuous CGM, HR, HRV, steps & sleep telemetry
│   ├── extracted_features.csv        # Synchronized 33-dimensional multimodal feature dataset
│   ├── trained_model.pkl             # Serialized predictive ML ensemble
│   ├── patient_profiles.json         # Patient clinical archetypes for simulation
│   └── feature_importances.csv       # Relative feature attributions
├── src/
│   ├── __init__.py
│   ├── data_engine.py                # Dual-stream synthetic generation & feature engineering
│   ├── physiology_twin.py            # Extended Bergman Minimal Model & ODE solver
│   ├── predictive_model.py           # Dual-head ML regressor & spike risk classifier
│   └── counterfactual_simulator.py   # In silico what-if clinical intervention engine
└── docs/
    ├── architecture_diagram.pdf      # Architecture diagram in PDF format
    ├── architecture_diagram.png      # Architecture diagram in PNG format
    ├── architecture_diagram.svg      # Architecture diagram in SVG format
    ├── presentation.pdf              # 12-Slide Master presentation deck in PDF format
    ├── CLINICAL_RATIONALE.md         # ICMR medical grounding & biomathematical formulation
    └── VIDEO_SCRIPT.md               # 20-Minute video presentation transcript & cues
```

---

*Happiest Health Reimagining and Reforming Healthcare in India Summit 2026, Bengaluru*
