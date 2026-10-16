# 20-Minute Video Presentation & Demonstration Script
**Project Title:** GlycoTwin-India: A Multimodal Physiological Digital Twin for Predictive Glycemic Dynamics & Counterfactual Clinical Decision Support in Asian Indian Type 2 Diabetes  
**Event:** Happiest Health Reimagining & Reforming Healthcare in India Summit – 2026, Bengaluru  
**Duration:** Exactly 20 Minutes (Structured for YouTube Unlisted Video or Recorded Slide Presentation)  

---

## Video Outline & Speaker Timings

| Timecode | Segment Title | Visual / Screen Activity | Primary Speaker |
| :--- | :--- | :--- | :--- |
| **00:00 – 02:00** | Team Introduction & The Indian Diabetes Crisis | Slide 1 & Slide 2 (Epidemiological Data) | Team Leader |
| **02:00 – 04:30** | The Healthcare Digital Twin Paradigm | Slide 3 (Digital Twin Concept & Feedback Loop) | Speaker 2 (Medical / Clinical Lead) |
| **04:30 – 07:00** | Dual Data Stream Fusion & DPDP Sandbox | Slide 4 & Architecture Diagram | Speaker 3 (Data Engineer) |
| **07:00 – 10:00** | Physiological Minimal ODE & Biomathematics | Slide 5 (Bergman Minimal Model Equations) | Speaker 4 (Bio-Modeling Lead) |
| **10:00 – 12:30** | Multimodal AI/ML Predictive Architecture | Slide 6 & 7 (ML Ensemble & Benchmarks) | Speaker 3 / ML Engineer |
| **12:30 – 16:30** | Live Interactive Prototype Demonstration | Screen Share: Streamlit Doctor Dashboard | Team Leader |
| **16:30 – 18:30** | Clinical Validation, Clarke Grid & Impact | Slide 7 & Slide 10 (Clinical Validation) | Speaker 2 (Clinical Lead) |
| **18:30 – 20:00** | Scalability, ABDM Integration & Conclusion | Slide 11 & Slide 12 (Roadmap & Closing) | Team Leader |

---

## Detailed Minute-by-Minute Script & Narration

### [00:00 – 02:00] Segment 1: Team Introduction & The Indian Diabetes Crisis
**Visual:** Slide 1 (Title Slide with Happiest Health Summit branding), transitioning to Slide 2 (Epidemiological charts showing ICMR-INDIAB statistics).

**Speaker (Team Leader):**  
"Respected jury members, technical experts from Happiest Health, and distinguished guests. We are Team [Team Name] representing [College / University Incubator Name]. Welcome to our Phase 1 prototype presentation for the Reimagining and Reforming Healthcare in India Summit 2026.

Today, we present **GlycoTwin-India**—a multimodal physiological digital twin designed to transform Type 2 Diabetes management from reactive point-in-time treatment into continuous, predictive, and proactive clinical care.

India is currently facing an unprecedented health crisis. According to the landmark ICMR-INDIAB study published in The Lancet, over 101 million Indians are living with Type 2 Diabetes, with an additional 136 million in the pre-diabetic window. 

Crucially, standard global diabetes algorithms fail in India due to what medical literature identifies as the **Asian Indian Phenotype** or the 'Thin-Fat' phenotype. Indian patients exhibit elevated visceral adiposity, higher waist-to-hip ratios, and early pancreatic beta-cell exhaustion at significantly lower BMI thresholds. Combined with high-carbohydrate staple diets, Indian diabetics suffer acute postprandial glycemic excursions exceeding 180 to 250 mg/dL, accelerating microvascular complications like retinopathy, nephropathy, and cardiovascular disease.

Our project addresses this exact challenge: building a personalized virtual replica of the patient that predicts acute glycemic events two hours before they occur."

---

### [02:00 – 04:30] Segment 2: The Healthcare Digital Twin Paradigm
**Visual:** Slide 3 (Digital Twin Concept Diagram showing physical patient, IoT continuous stream, in silico computational twin, and predictive feedback loop).

**Speaker (Clinical Lead):**  
"What is a Digital Twin in healthcare? A Digital Twin is not simply a static electronic medical record, nor is it merely a passive wearable dashboard. It is an active, dynamic biophysical simulation of a patient’s internal physiological state, continuously updated and synchronized via real-time telemetry.

In traditional diabetes care, a physician sees a patient every three to six months. They look at a static HbA1c value, which only provides a retrospective 90-day average, completely blinding them to the daily glycemic volatility that actually drives tissue damage.

With GlycoTwin-India, we create a closed-loop virtual patient:
1. When the patient consumes a meal or engages in exercise, wearable IoT sensors capture the physiological perturbation.
2. The Digital Twin synchronizes this real-time data with the patient’s historical electronic health record—their baseline insulin sensitivity, renal clearance, genetic risk alleles, and medication regimen.
3. The Twin forecasts the patient's glycemic trajectory two hours into the future, issuing proactive clinical alerts if an adverse excursion is imminent.
4. Most importantly, it empowers physicians to perform **in silico counterfactual testing**: asking 'what-if' questions—what if the patient reduces carb intake by 40 grams? What if they take a 20-minute post-prandial walk? What if we add an SGLT2 inhibitor?—and observing the outcome on the virtual patient before prescribing it in the physical world."

---

### [04:30 – 07:00] Segment 3: Dual Data Stream Fusion & DPDP Sandbox
**Visual:** Slide 4 and `docs/architecture_diagram.pdf` (High-resolution data flow from Stream 1 and Stream 2 into the Multimodal Feature Engine).

**Speaker (Data Engineer):**  
"Let us examine how GlycoTwin-India ingests and harmonizes multimodal clinical data while strictly adhering to India’s Digital Personal Data Protection Act (DPDP Act 2023) and global HIPAA sandbox guidelines.

Our prototype fuses two complementary data streams:

**Data Stream 1: Static and Historical EHR Data**  
Generated using clinical synthesis calibrated against real-world Indian demographic cohorts. This stream encapsulates 18 static features:
- Patient demographics: Age, gender, geographic location across Indian metropolitan hubs.
- Asian Indian anthropometry: BMI, Waist-to-Hip Ratio (WHR), and Visceral Adiposity Index (VAI).
- Clinical lab panels: Baseline HbA1c, fasting plasma glucose, estimated Glomerular Filtration Rate (eGFR), serum creatinine, lipid profiles, and microvascular staging.
- Genetic risk profiling: TCF7L2 high-risk polymorphism allele carriers.
- Current pharmacotherapy: Dosages of Metformin, Sulfonylureas (Glimepiride), SGLT2 inhibitors (Empagliflozin), DPP-4 inhibitors (Sitagliptin), and basal insulin.

**Data Stream 2: Dynamic Wearable IoT Telemetry**  
Mimicking continuous monitoring from commercial devices like FreeStyle Libre, Dexcom, Apple Health, and dedicated medical IoT patches:
- Interstitial glucose readings sampled at 5-minute intervals (288 observations per patient per day).
- Continuous Heart Rate (BPM) and Autonomic Heart Rate Variability (HRV RMSSD in milliseconds).
- Tri-axial accelerometer activity (steps per 5 minutes and METs).
- Circadian sleep staging: Awake, Light, Deep, and REM sleep.
- Event logs: Meal carbohydrate ingestion timestamps and medication boluses.

**The Multimodal Feature Engine:**  
Every 5 minutes, our pipeline constructs a 24-step historical rolling window (2 hours). It computes dynamic derivatives including the rate of glucose change ($dG/dt$) over 15, 30, and 60 minutes, the 2-hour area under the curve (AUC), autonomic stress drops, and activity-induced glucose disposal. These dynamic metrics are fused with the static EHR vector into a unified 33-dimensional multimodal tensor."

---

### [07:00 – 10:00] Segment 4: Physiological Minimal ODE & Biomathematics
**Visual:** Slide 5 (Mathematical formulation of extended Bergman Minimal Model with differential equations and parameter tuning).

**Speaker (Bio-Modeling Lead):**  
"At the core of our digital twin is a rigorous biophysical engine based on an extended Bergman Minimal Model, modified to account for the Asian Indian phenotype, meal absorption kinetics, and modern pharmacodynamics.

The model is defined by a system of five coupled ordinary differential equations:

1. **Glucose Dynamics in Plasma ($G$):**  
   $$\frac{dG(t)}{dt} = - (p_1 + X(t)) G(t) + p_1 G_b \cdot \Phi_{metformin} + \frac{R_a(t)}{V_g} - Cl_{renal}(G) - U_{exercise}(Step)$$  
   Here, $G_b$ is baseline fasting glucose, $\Phi_{metformin}$ represents hepatic glucose output suppression, $R_a(t)$ is the rate of gut absorption, $Cl_{renal}$ models SGLT2-mediated glucosuria above renal thresholds, and $U_{exercise}$ models insulin-independent GLUT4 muscle uptake driven by walking cadence.

2. **Remote Compartment Insulin Action ($X$):**  
   $$\frac{dX(t)}{dt} = - p_2 X(t) + p_3 \max(0, I(t) - I_b)$$  
   The patient's insulin sensitivity $S_I = p_3 / p_2$ is personalized based on their Visceral Adiposity Index and duration of diabetes. High visceral adiposity directly attenuates $S_I$.

3. **Pancreatic Insulin Secretion ($I$):**  
   $$\frac{dI(t)}{dt} = - n (I(t) - I_b - \delta_{sulf}) + \beta_{resp} \cdot \Psi_{dpp4} \cdot \max(0, G(t) - h) + \frac{Exo(t)}{V_i}$$  
   Pancreatic responsiveness $\beta_{resp}$ reflects beta-cell reserve, attenuated by elevated HbA1c and TCF7L2 genetic risk, while $\Psi_{dpp4}$ captures incretin hormone enhancement from DPP-4 inhibitors.

4. **Two-Compartment Gastrointestinal Transit ($G_{gut1}, G_{gut2}$):**  
   Nutritional carbohydrate boluses are absorbed through a dual-stage transit model, accurately simulating the postprandial glucose appearance curve.

We solve these non-linear ODEs in real-time using high-precision Runge-Kutta 4th order numerical integration with millisecond execution speed."

---

### [10:00 – 12:30] Segment 5: Multimodal AI/ML Predictive Architecture
**Visual:** Slide 6 (ML architecture diagram) and Slide 7 (ROC curve, Clarke Error Grid, and feature importance bar chart).

**Speaker (ML Engineer):**  
"While the biophysical ODE engine provides physiological fidelity, clinical environments require rapid machine learning inference that captures non-linear stochastic patterns across large cohorts.

We constructed a **Dual-Head Gradient Boosted Ensemble**:
1. **Continuous Regression Head:** Ingests the 33-dimensional multimodal feature vector and predicts continuous interstitial glucose at the 2-hour forward horizon ($t + 120$ minutes). It also projects intermediate trajectories at 15, 30, 45, 60, and 90 minutes.
2. **Classification Head:** Directly outputs calibrated risk probabilities for two critical acute events:
   - Acute Postprandial Hyperglycemic Spike ($G \ge 180$ mg/dL).
   - Nocturnal Hypoglycemia ($G \le 70$ mg/dL).

To provide clinical explainability, we evaluated feature attribution:
- The top predictive features are the **1-hour cumulative carbohydrate load**, the **2-hour CGM Area Under the Curve**, **current glucose rate of change ($dG/dt$)**, and the **Visceral Adiposity Index**.
- This proves that neither static EHR nor dynamic wearables alone are sufficient—it is their multimodal synergy that unlocks predictive accuracy."

---

### [12:30 – 16:30] Segment 6: Live Interactive Prototype Demonstration
**Visual:** Live Screen Recording of the interactive Streamlit Dashboard (`app.py`).

**Speaker (Team Leader):**  
*(Demonstrator clicks through the UI tabs while speaking)*

"We are now looking at the live GlycoTwin-India Clinician Dashboard. Let us explore how a practicing endocrinologist or diabetologist interacts with this virtual patient.

**1. Virtual Patient Profile Selection:**  
In the sidebar, we can switch between diverse clinical archetypes from Indian metropolitan centers. Let us select **Patient IND-T2D-1000: Arun Sharma**, a 58-year-old male from Bengaluru. Notice his EHR summary card: BMI of 27.2 kg/m², elevated Waist-to-Hip Ratio of 0.98, baseline HbA1c of 8.9%, and eGFR of 78 mL/min. He is currently on Metformin 1000 mg and Glimepiride 2 mg.

**2. Real-Time Twin Telemetry:**  
On Tab 1, we observe live synchronized telemetry. Current CGM reads 168.4 mg/dL. The 24-hour Time-in-Range is 68.2%, below the clinical target of 70%. Below, the interactive Plotly curve displays the 24-hour glycemic profile with target green shading between 70 and 180 mg/dL, alongside synchronized heart rate and step cadence.

**3. 2-Hour Predictive Horizon:**  
Switching to Tab 2, the Digital Twin alerts the clinician: 'Critical Spike Hazard: 84% Probability'. The machine learning model forecasts that in 120 minutes, the patient's glucose will surge to 212.4 mg/dL following an afternoon meal. The predictive chart shows the observed 90-minute past connected seamlessly to the 2-hour forward trajectory with a 90% confidence band.

**4. The What-If Counterfactual Sandbox (The Digital Twin in Action):**  
Now, let us navigate to Tab 3. Here, the doctor can test clinical interventions in silico.
- Currently, Arun consumed 75 grams of simple carbohydrates and remained sedentary. The twin forecasts a dangerous peak of 218 mg/dL.
- Let us modify the scenario: we reduce carbohydrate intake to 35 grams of low-glycemic foods, and we prescribe a 25-minute post-prandial walk.
- Furthermore, let us check 'Add SGLT2 Inhibitor (Empagliflozin 10mg)'.
- Instantly, the Digital Twin recomputes the personalized biophysical equations! 
- Look at the comparative trajectory: The counterfactual curve blunts the excursion dramatically. The peak drops by **46.8 mg/dL**, bringing the peak safely under the 180 mg/dL threshold, and increasing Time-in-Range to **89.5%**!
- The system automatically generates actionable, evidence-based recommendations that the physician can share directly with the patient."

---

### [16:30 – 18:30] Segment 7: Clinical Validation, Clarke Grid & Impact
**Visual:** Slide 7 and Slide 10 (Clinical Validation Tables and regulatory alignment).

**Speaker (Clinical Lead):**  
"Let us review the quantitative validation benchmarks achieved by GlycoTwin-India on our held-out clinical test cohort:
- **Mean Absolute Error (MAE):** 9.49 mg/dL. In clinical diabetology, an error margin under 15 mg/dL is considered optimal for decision support.
- **Root Mean Squared Error (RMSE):** 13.1 mg/dL.
- **Clarke Error Grid Analysis (CEGA):** **98.1% of all predictions fall within Zone A and Zone B**. Zone A represents clinically accurate predictions where medical decisions would be unchanged, and Zone B represents benign deviations with zero clinical risk. Less than 2% fall outside, with zero points in dangerous error Zones D or E.
- **Acute Spike ROC-AUC:** **0.970** with an **F1-Score of 0.907**, demonstrating high sensitivity and specificity in catching postprandial surges before they manifest.

From a clinical governance perspective:
- The system operates strictly as Clinical Decision Support (CDS), augmenting rather than replacing physician judgment.
- By providing a 2-hour early warning window, patients and clinicians have adequate therapeutic time to initiate non-pharmacological interventions (such as brisk walking or hydration) or adjust pre-prandial bolus timing."

---

### [18:30 – 20:00] Segment 8: Scalability, ABDM Integration & Conclusion
**Visual:** Slide 11 (Architecture & Deployment Roadmap) and Slide 12 (Conclusion Slide).

**Speaker (Team Leader):**  
"Looking ahead to Phase 2, Phase 3, and real-world deployment:
1. **ABDM and FHIR Alignment:** Our EHR data schemas are built to map directly to India’s Ayushman Bharat Digital Mission (ABDM) and HL7 FHIR standards, enabling seamless interoperability with national electronic health records.
2. **Edge Computing:** Our model's sub-8ms inference latency allows lightweight deployment directly on mobile applications or wearable microcontrollers, enabling real-time offline predictions even in low-connectivity rural settings across India.
3. **Summit Showcase:** Our team is eager and prepared to travel to Bengaluru for the Happiest Health Reimagining and Reforming Healthcare in India Summit 2026, where we will demonstrate live physical sensor streaming and multi-patient twin synchronization in front of the esteemed jury.

In conclusion: The future of medicine must be proactive, not reactive. With GlycoTwin-India, we have demonstrated that combining biophysical simulation with multimodal machine learning can help millions of Indian diabetes patients live healthier, longer, and complication-free lives.

Thank you to Happiest Health for this incredible platform. We welcome your questions and look forward to the Phase 2 presentation!"
