import numpy as np
from src.physiology_twin import PhysiologicalTwin

class CounterfactualSimulator:
    def __init__(self, ehr_dict):
        self.ehr = ehr_dict
        self.twin = PhysiologicalTwin(ehr_dict)
        
    def evaluate_interventions(self, current_glucose, baseline_carbs=70.0, modified_carbs=35.0, walk_duration_min=20.0, add_sglt2i=False, add_dpp4i=False):
        baseline_sim = self.twin.simulate(
            initial_glucose=current_glucose,
            horizon_minutes=120,
            meal_carbs=baseline_carbs,
            post_meal_walk_minutes=0.0
        )
        
        counterfactual_twin = PhysiologicalTwin(self.ehr)
        sglt2_val = 10 if (add_sglt2i or self.ehr.get("sglt2i_mg", 0) > 0) else 0
        dpp4_val = 100 if (add_dpp4i or self.ehr.get("dpp4i_mg", 0) > 0) else 0
        
        counterfactual_sim = counterfactual_twin.simulate(
            initial_glucose=current_glucose,
            horizon_minutes=120,
            meal_carbs=modified_carbs,
            post_meal_walk_minutes=walk_duration_min,
            walk_start_delay=25.0,
            step_cadence=95.0,
            sglt2_override=sglt2_val,
            dpp4_override=dpp4_val
        )
        
        delta_peak = round(counterfactual_sim["peak_glucose"] - baseline_sim["peak_glucose"], 1)
        delta_tir = round(counterfactual_sim["time_in_range_pct"] - baseline_sim["time_in_range_pct"], 1)
        delta_final = round(counterfactual_sim["final_glucose"] - baseline_sim["final_glucose"], 1)
        
        recommendations = []
        if baseline_sim["peak_glucose"] > 180.0:
            if modified_carbs < baseline_carbs:
                recommendations.append(f"Carbohydrate reduction from {baseline_carbs}g to {modified_carbs}g curbs acute postprandial surge by {abs(delta_peak)} mg/dL.")
            if walk_duration_min > 0:
                recommendations.append(f"A {int(walk_duration_min)}-minute post-prandial walk enhances non-insulin-dependent muscle GLUT4 translocation, lowering the peak.")
            if add_sglt2i and self.ehr.get("sglt2i_mg", 0) == 0:
                recommendations.append("Initiation of SGLT2 inhibitor provides steady glucosuria, blunting glycemic excursion without hypoglycemia.")
        else:
            recommendations.append("Patient profile is in optimal glycemic control for this nutritional window.")
            
        return {
            "baseline": baseline_sim,
            "counterfactual": counterfactual_sim,
            "delta_peak_mg_dl": delta_peak,
            "delta_tir_percentage": delta_tir,
            "delta_final_glucose": delta_final,
            "clinical_recommendations": recommendations
        }
