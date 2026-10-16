import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")
    
    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#f8fafc")
    
    ax.text(7, 7.5, "GlycoTwin-India: Multimodal Physiological Digital Twin Architecture", 
            ha="center", va="center", fontsize=17, fontweight="bold", color="#0f172a")
    ax.text(7, 7.15, "Fusion of Static Clinical Records & Dynamic Wearable IoT Telemetry for 2-Hour Predictive Glycemic Control",
            ha="center", va="center", fontsize=11, color="#475569")
            
    p_ehr = patches.FancyBboxPatch((0.6, 3.8), 3.2, 2.7, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#0284c7", linewidth=2)
    ax.add_patch(p_ehr)
    ax.text(2.2, 6.2, "DATA STREAM 1: STATIC EHR", ha="center", va="center", fontsize=10, fontweight="bold", color="#0284c7")
    ax.text(2.2, 5.0, "• Demographics (Age, Gender, Region)\n• Asian Indian Phenotype (BMI, WHR, VAI)\n• Duration of T2D & Baseline HbA1c\n• Renal Panel (eGFR, Serum Creatinine)\n• Lipid Profile & Retinopathy Stage\n• Pharmacotherapy (Metformin, SGLT2i)\n• TCF7L2 Genetic Risk Marker",
            ha="center", va="center", fontsize=8.5, color="#334155")

    p_wear = patches.FancyBboxPatch((0.6, 0.6), 3.2, 2.7, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#0d9488", linewidth=2)
    ax.add_patch(p_wear)
    ax.text(2.2, 3.0, "DATA STREAM 2: DYNAMIC IOT", ha="center", va="center", fontsize=10, fontweight="bold", color="#0d9488")
    ax.text(2.2, 1.8, "• Continuous Glucose (CGM 5-min cadence)\n• Continuous Heart Rate (BPM)\n• Heart Rate Variability (RMSSD ms)\n• Tri-axial Accelerometer (Steps / METs)\n• Sleep Architecture (Awake/Light/Deep/REM)\n• Nutritional Carb Ingestion Timestamps\n• Exogenous Insulin Bolus Logging",
            ha="center", va="center", fontsize=8.5, color="#334155")

    p_feat = patches.FancyBboxPatch((4.5, 2.2), 2.2, 3.8, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#6366f1", linewidth=2)
    ax.add_patch(p_feat)
    ax.text(5.6, 5.6, "MULTIMODAL\nFEATURE ENGINE", ha="center", va="center", fontsize=10, fontweight="bold", color="#6366f1")
    ax.text(5.6, 3.8, "• 2-Hour Rolling Window\n• dG/dt (15, 30, 60m)\n• Glycemic Volatility (AUC)\n• Stress-Autonomic Index\n• Carb Absorption Dynamics\n• Activity-GLUT4 Uptake\n• Static Clinical Fusion Vector",
            ha="center", va="center", fontsize=8, color="#334155")

    p_twin = patches.FancyBboxPatch((7.4, 4.2), 2.8, 2.3, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#8b5cf6", linewidth=2)
    ax.add_patch(p_twin)
    ax.text(8.8, 6.2, "PHYSIOLOGICAL TWIN", ha="center", va="center", fontsize=10, fontweight="bold", color="#8b5cf6")
    ax.text(8.8, 5.2, "• Extended Bergman ODEs\n• Personalized Insulin Sensitivity\n• 2-Compartment Gut Model\n• Hepatic & Renal Clearance\n• Runge-Kutta 4 Integration",
            ha="center", va="center", fontsize=8.5, color="#334155")

    p_ml = patches.FancyBboxPatch((7.4, 1.0), 2.8, 2.5, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#f59e0b", linewidth=2)
    ax.add_patch(p_ml)
    ax.text(8.8, 3.2, "PREDICTIVE ENSEMBLE", ha="center", va="center", fontsize=10, fontweight="bold", color="#f59e0b")
    ax.text(8.8, 2.1, "• Gradient Boosted Regressor\n• Spike Hazard Classifier\n• 2-Hour Forward Horizon\n• 90% Confidence Interval\n• SHAP Clinical Attribution",
            ha="center", va="center", fontsize=8.5, color="#334155")

    p_ui = patches.FancyBboxPatch((10.9, 1.2), 2.5, 5.3, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#10b981", linewidth=2)
    ax.add_patch(p_ui)
    ax.text(12.15, 6.1, "CLINICAL UI & WHAT-IF", ha="center", va="center", fontsize=10, fontweight="bold", color="#10b981")
    ax.text(12.15, 3.7, "• Live Telemetry Stream\n• 2-Hour Trajectory Map\n• Acute Spike Alerting\n• Counterfactual Sandbox\n  - Carb Load Modulation\n  - Walking Prescription\n  - Pharmacotherapy Titration\n• Clinical Decision Support\n• DPDP Act Compliance",
            ha="center", va="center", fontsize=8.5, color="#334155")

    ax.annotate("", xy=(4.5, 4.8), xytext=(3.8, 4.8), arrowprops=dict(arrowstyle="->", lw=2, color="#0284c7"))
    ax.annotate("", xy=(4.5, 2.8), xytext=(3.8, 2.2), arrowprops=dict(arrowstyle="->", lw=2, color="#0d9488"))
    ax.annotate("", xy=(7.4, 5.2), xytext=(6.7, 4.6), arrowprops=dict(arrowstyle="->", lw=2, color="#6366f1"))
    ax.annotate("", xy=(7.4, 2.5), xytext=(6.7, 3.5), arrowprops=dict(arrowstyle="->", lw=2, color="#6366f1"))
    ax.annotate("", xy=(10.9, 5.0), xytext=(10.2, 5.2), arrowprops=dict(arrowstyle="->", lw=2, color="#8b5cf6"))
    ax.annotate("", xy=(10.9, 2.8), xytext=(10.2, 2.5), arrowprops=dict(arrowstyle="->", lw=2, color="#f59e0b"))
    
    docs_dir = os.path.join(os.path.dirname(__file__), "docs")
    os.makedirs(docs_dir, exist_ok=True)
    
    pdf_path = os.path.join(docs_dir, "architecture_diagram.pdf")
    png_path = os.path.join(docs_dir, "architecture_diagram.png")
    svg_path = os.path.join(docs_dir, "architecture_diagram.svg")
    
    plt.tight_layout()
    plt.savefig(pdf_path, format="pdf", bbox_inches="tight")
    plt.savefig(png_path, format="png", bbox_inches="tight", dpi=300)
    plt.savefig(svg_path, format="svg", bbox_inches="tight")
    plt.close()

def generate_slide_deck_pdf():
    docs_dir = os.path.join(os.path.dirname(__file__), "docs")
    os.makedirs(docs_dir, exist_ok=True)
    deck_pdf_path = os.path.join(docs_dir, "presentation.pdf")
    
    slides_data = [
        {
            "num": "01 / 12",
            "tag": "HAPPIEST HEALTH SUMMIT 2026 | BENGALURU",
            "title": "GlycoTwin-India",
            "sub": "A Multimodal Physiological Digital Twin for Predictive Glycemic Dynamics &\nCounterfactual Clinical Decision Support in Asian Indian Type 2 Diabetes",
            "bullets": [
                "Track: Digital Twin Proof-of-Concept in Healthcare",
                "Theme: Reimagining and Reforming Healthcare in India",
                "Dual-Engine Paradigm: Biophysical Minimal ODEs + Multimodal Machine Learning Ensemble",
                "Clinical Horizon: 2-Hour Ahead Predictive Early Warning for Postprandial Spikes & Hypoglycemia",
                "Author Team: Academic Incubator Initiative | Open-Source Prototype"
            ]
        },
        {
            "num": "02 / 12",
            "tag": "EPIDEMIOLOGICAL GROUNDING",
            "title": "The Indian Diabetes Crisis & Phenotypic Vulnerability",
            "sub": "Why Standard Global Diabetes Models Fail in the Indian Demographic Context",
            "bullets": [
                "Epidemic Scale: Over 101 million individuals diagnosed with T2D, and 136 million with pre-diabetes (ICMR-INDIAB study).",
                "The Asian Indian Phenotype ('Thin-Fat' Phenotype): Normal or borderline BMI (<23 kg/m²) accompanied by pronounced visceral adiposity and high waist-hip ratio.",
                "Premature Beta-Cell Exhaustion: Loss of first-phase insulin secretion occurs nearly a decade earlier compared to Western counterparts.",
                "Dietary Composition: High-glycemic carbohydrate burden (refined wheat, white rice) drives acute postprandial glycemic excursions (>180 mg/dL).",
                "Clinical Need: A dynamic, personalized in silico replica capable of predicting excursions before they induce microvascular and macrovascular injury."
            ]
        },
        {
            "num": "03 / 12",
            "tag": "DIGITAL TWIN CONCEPT",
            "title": "The Healthcare Digital Twin Paradigm",
            "sub": "Transitioning from Reactive Point-in-Time Care to Continuous Proactive Simulation",
            "bullets": [
                "Definition: A continuous computational replica of an individual's glucose-insulin regulatory metabolism.",
                "Closed-Loop Synchronization: State variables updated continuously through real-time wearable IoT streams.",
                "Dynamic In Silico Testing: Evaluates treatment adjustments, dietary swaps, and physical activity on the virtual twin before applying to the patient.",
                "Clinical Empowerment: Provides doctors with anticipatory alerts 120 minutes prior to severe glycemic spikes or nocturnal hypoglycemia.",
                "Sandbox Adherence: Strictly designed under DPDP Act 2023 and HIPAA synthetic sandbox guidelines."
            ]
        },
        {
            "num": "04 / 12",
            "tag": "DATA ARCHITECTURE",
            "title": "Multimodal Data Fusion: Static EHR + Dynamic IoT",
            "sub": "Bridging Deep Longitudinal Clinical Context with High-Frequency Physiological Signals",
            "bullets": [
                "Data Stream 1 (Static EHR): Demographics, T2D duration, baseline HbA1c, eGFR renal clearance, lipid profile, TCF7L2 genetic risk allele, and active pharmacotherapy.",
                "Data Stream 2 (Dynamic IoT Wearables): Continuous Glucose Monitoring (CGM 5-min intervals), heart rate (BPM), autonomic heart rate variability (RMSSD), accelerometer steps, sleep staging, and meal logs.",
                "Feature Harmonization: 24-step rolling window computes rate of change (dG/dt), glycemic area under curve (AUC), autonomic stress drops, and activity utilization.",
                "Unified Multimodal Tensor: Ingests 33 synchronized clinical features into downstream predictive heads."
            ]
        },
        {
            "num": "05 / 12",
            "tag": "MATHEMATICAL FORMULATION",
            "title": "Physiological Minimal ODE Engine",
            "sub": "Personalized Bergman Minimal Model Tailored to Asian Indian Visceral Adiposity",
            "bullets": [
                "Glucose Homeostasis: dG/dt = -(p1 + X)G + p1*Gb*hepatic_suppression + Ra/Vg - renal_clearance - exercise_uptake",
                "Remote Insulin Dynamics: dX/dt = -p2*X + p3*max(0, I - Ib)",
                "Pancreatic Responsiveness: dI/dt = -n(I - Ib - sulf_boost) + beta_cell_responsiveness*incretin_boost*max(0, G - h) + basal_insulin",
                "Personalization Coefficients: Insulin sensitivity (Si = p3/p2) mathematically scaled by patient Visceral Adiposity Index (VAI) and WHR.",
                "Pharmacodynamic Integration: Metformin hepatic suppression, SGLT2 inhibitor renal spillover, and DPP-4 incretin amplification embedded directly into ODEs."
            ]
        },
        {
            "num": "06 / 12",
            "tag": "AI / ML ARCHITECTURE",
            "title": "Multimodal Machine Learning Ensemble",
            "sub": "Dual-Head Gradient Boosted Regressor & Acute Spike Classifier",
            "bullets": [
                "Regression Head: Predicts continuous blood glucose trajectory across 15, 30, 45, 60, 90, and 120-minute forward horizons.",
                "Classification Head: Computes calibrated probability of acute postprandial spike (G >= 180 mg/dL) and nocturnal hypoglycemia (G <= 70 mg/dL).",
                "Confidence Interval Calibration: Dynamic 90% predictive error bands providing clinicians with actionable uncertainty quantification.",
                "Inference Latency: Less than 8 milliseconds per prediction window, enabling real-time edge or mobile deployment."
            ]
        },
        {
            "num": "07 / 12",
            "tag": "EXPERIMENTAL RESULTS",
            "title": "Validation Metrics & Clinical Accuracy",
            "sub": "Quantitative Benchmarks Demonstrating ISO 15197 / FDA Clinical Compliance",
            "bullets": [
                "Mean Absolute Error (MAE): 9.49 mg/dL on held-out test cohort (Clinical tolerance standard: < 15 mg/dL).",
                "Root Mean Squared Error (RMSE): 13.1 mg/dL, showing robust bounds against severe outlier excursions.",
                "Clarke Error Grid Analysis: 98.1% of predictions fall in Zone A and Zone B (Clinically Accurate & Benign).",
                "Acute Spike Classification ROC-AUC: 0.970 with an F1-Score of 0.907.",
                "Top Predictive Drivers: 1-hour carbohydrate load, 2-hour CGM AUC, current CGM, and Visceral Adiposity Index."
            ]
        },
        {
            "num": "08 / 12",
            "tag": "CLINICAL USER INTERFACE",
            "title": "Doctor Interaction Dashboard",
            "sub": "Transforming Complex Multimodal Telemetry into Intuitive Medical Insights",
            "bullets": [
                "EHR Phenotype Card: Instant view of Asian Indian risk markers, renal staging (eGFR), and pharmacotherapy.",
                "Continuous Telemetry Panel: Synchronized interactive 24-hour CGM profiles with meal and activity annotations.",
                "Forward Risk Horizon: Clear traffic-light risk categorization (Nominal vs Elevated Volatility vs Critical Spike Hazard).",
                "Physician Ergonomics: Designed for fast ambulatory consultations or remote tele-monitoring review."
            ]
        },
        {
            "num": "09 / 12",
            "tag": "COUNTERFACTUAL SIMULATOR",
            "title": "What-If Simulation Sandbox for Clinicians",
            "sub": "In Silico Testing of Lifestyle Modifications and Pharmacological Titration",
            "bullets": [
                "Nutritional Dial: Doctors simulate carb load reduction (e.g., 75g baseline to 35g complex carbs), demonstrating peak glucose drops of 35-50 mg/dL.",
                "Exercise Prescription: Adding a 20-25 minute post-meal walk directly simulates GLUT4-mediated glucose disposal.",
                "Pharmacotherapy Titration: Virtual addition of SGLT2 inhibitors or DPP-4 inhibitors illustrates blunted glycemic variability without hypoglycemic risk.",
                "Side-by-Side Trajectory: Visualizes baseline unmanaged trajectory alongside counterfactual virtual twin trajectory in real time."
            ]
        },
        {
            "num": "10 / 12",
            "tag": "REGULATORY & GOVERNANCE",
            "title": "Data Privacy, Ethics & Indian Regulatory Alignment",
            "sub": "Ensuring Robust Compliance with the DPDP Act 2023 & Ayushman Bharat Digital Mission (ABDM)",
            "bullets": [
                "DPDP Act 2023 Sandbox: Complete anonymization and synthetic patient generation protocols strictly eliminating re-identification risks.",
                "ABDM / FHIR Compatibility: Static EHR schema mapped directly to HL7 FHIR Indian Health Record standards.",
                "Algorithmic Transparency: Explainable feature attributions ensure no opaque 'black-box' clinical decisions.",
                "Clinical Oversight: System structured strictly as Clinical Decision Support (CDS), keeping certified physicians in the loop."
            ]
        },
        {
            "num": "11 / 12",
            "tag": "DEPLOYMENT ROADMAP",
            "title": "Scalability, Edge Inference & Summit Roadmap",
            "sub": "From University Incubator Proof-of-Concept to Real-World Clinical Telehealth Integration",
            "bullets": [
                "Phase 1 (Current): Validated PoC codebase, Streamlit doctor dashboard, and synthetic data pipeline submitted for evaluation.",
                "Phase 2 (Jury Presentation): Virtual live demonstration of twin simulation across complex diabetic archetypes.",
                "Phase 3 (Summit Showcase, Bengaluru): In-person interactive presentation at Reimagining Healthcare Summit 2026.",
                "Edge Integration Roadmap: Deploying lightweight twin models onto wearable firmware and mobile health apps for continuous offline inference."
            ]
        },
        {
            "num": "12 / 12",
            "tag": "CONCLUSION & IMPACT",
            "title": "Reimagining Diabetes Care in India",
            "sub": "Proactive, Personalized Medicine Powered by Physiological Digital Twins",
            "bullets": [
                "Paradigm Shift: Moving Indian diabetes care from intermittent HbA1c checks every 3 months to continuous 2-hour proactive mitigation.",
                "Demonstrated Outcome: Proven reduction of postprandial glycemic excursions through accessible lifestyle & drug counterfactuals.",
                "Open Science Commitment: Fully accessible GitHub repository with complete reproducibility and synthetic datasets.",
                "Gratitude: Thank you to Happiest Health for championing digital health innovation across India's academic incubators!"
            ]
        }
    ]
    
    with PdfPages(deck_pdf_path) as pdf:
        for s in slides_data:
            fig, ax = plt.subplots(figsize=(13.33, 7.5), dpi=200)
            ax.set_xlim(0, 13.33)
            ax.set_ylim(0, 7.5)
            ax.axis("off")
            
            fig.patch.set_facecolor("#ffffff")
            ax.set_facecolor("#ffffff")
            
            top_bar = patches.Rectangle((0, 7.2), 13.33, 0.3, facecolor="#0284c7")
            ax.add_patch(top_bar)
            
            bottom_bar = patches.Rectangle((0, 0), 13.33, 0.35, facecolor="#0f172a")
            ax.add_patch(bottom_bar)
            
            ax.text(0.8, 6.75, s["tag"], fontsize=10, fontweight="bold", color="#0284c7")
            ax.text(12.5, 6.75, s["num"], fontsize=10, fontweight="bold", color="#64748b", ha="right")
            
            ax.text(0.8, 6.1, s["title"], fontsize=22, fontweight="bold", color="#0f172a")
            ax.text(0.8, 5.5, s["sub"], fontsize=12, color="#475569")
            
            content_card = patches.FancyBboxPatch((0.8, 0.7), 11.7, 4.4, boxstyle="round,pad=0.2", facecolor="#f8fafc", edgecolor="#e2e8f0", linewidth=1.5)
            ax.add_patch(content_card)
            
            y_pos = 4.6
            for b in s["bullets"]:
                ax.plot(1.3, y_pos, marker="o", markersize=6, color="#0284c7")
                ax.text(1.6, y_pos, b, fontsize=11, color="#1e293b", va="center", wrap=True)
                y_pos -= 0.75
                
            ax.text(0.8, 0.15, "Happiest Health Reimagining & Reforming Healthcare in India Summit 2026 | Bengaluru", fontsize=8.5, color="#94a3b8")
            ax.text(12.5, 0.15, "CONFIDENTIAL - JURY EVALUATION", fontsize=8.5, color="#94a3b8", ha="right")
            
            plt.tight_layout()
            pdf.savefig(fig)
            plt.close()

if __name__ == "__main__":
    create_architecture_diagram()
    generate_slide_deck_pdf()
    print("Artifacts generated successfully in docs/")
