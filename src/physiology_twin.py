import numpy as np

class PhysiologicalTwin:
    def __init__(self, ehr_profile):
        self.ehr = ehr_profile
        self.p1 = 0.028
        self.p2 = 0.025
        
        base_sensitivity = 0.000045
        wai = float(self.ehr.get("visceral_adiposity_index", 4.0))
        whr = float(self.ehr.get("waist_hip_ratio", 0.92))
        duration = float(self.ehr.get("t2d_duration_years", 5.0))
        hba1c = float(self.ehr.get("hba1c", 8.0))
        tcf = int(self.ehr.get("tcf7l2_carrier", 0))
        
        attenuation = (1.0 + (wai * 0.12) + (whr * 0.35) + (duration * 0.025))
        self.si = base_sensitivity / attenuation
        self.p3 = self.p2 * self.si
        
        self.beta_cell_responsiveness = max(0.08, 0.42 - (hba1c * 0.028) - (0.06 if tcf == 1 else 0.0))
        
        self.gb = float(self.ehr.get("fasting_glucose", 130.0))
        self.ib = max(5.0, 16.0 - (duration * 0.4))
        
        self.vg = 12.0
        self.vi = 12.0
        self.n = 0.22
        self.h = 90.0
        
        metformin = float(self.ehr.get("metformin_mg", 1000.0))
        sglt2i = float(self.ehr.get("sglt2i_mg", 0.0))
        dpp4i = float(self.ehr.get("dpp4i_mg", 0.0))
        sulfonylurea = float(self.ehr.get("sulfonylurea_mg", 0.0))
        
        self.hepatic_suppression = 1.0 - (metformin * 0.00015)
        self.renal_threshold = 180.0 if sglt2i == 0 else 135.0
        self.sglt2_spillover_rate = 0.035 if sglt2i > 0 else 0.0
        self.incretin_boost = 1.0 + (0.28 if dpp4i > 0 else 0.0)
        self.sulf_basal_insulin_boost = sulfonylurea * 1.8
        
    def _derivatives(self, state, carb_rate, step_intensity, basal_insulin_rate):
        g, x, i_val, gut1, gut2 = state
        
        dgut1 = -0.05 * gut1 + (carb_rate * 1000.0 / 180.16)
        dgut2 = 0.05 * gut1 - 0.04 * gut2
        ra = 0.04 * gut2 * 0.85
        
        renal_clearance = 0.0
        if g > self.renal_threshold:
            renal_clearance = self.sglt2_spillover_rate * (g - self.renal_threshold)
            
        exercise_uptake = (step_intensity / 100.0) * 0.012 * (g / 100.0)
        
        dg = - (self.p1 + x) * g + (self.p1 * self.gb * self.hepatic_suppression) + (ra / self.vg) - renal_clearance - exercise_uptake
        dx = - self.p2 * x + self.p3 * max(0.0, i_val - self.ib)
        
        glucose_stimulus = max(0.0, g - self.h)
        pancreatic_secretion = self.beta_cell_responsiveness * self.incretin_boost * glucose_stimulus
        di = - self.n * (i_val - self.ib - self.sulf_basal_insulin_boost) + pancreatic_secretion + (basal_insulin_rate / self.vi)
        
        return np.array([dg, dx, di, dgut1, dgut2])

    def simulate(self, initial_glucose, horizon_minutes=120, meal_carbs=0.0, post_meal_walk_minutes=0.0, walk_start_delay=30.0, step_cadence=90.0, sglt2_override=None, dpp4_override=None):
        if sglt2_override is not None:
            self.renal_threshold = 180.0 if sglt2_override == 0 else 135.0
            self.sglt2_spillover_rate = 0.035 if sglt2_override > 0 else 0.0
        if dpp4_override is not None:
            self.incretin_boost = 1.0 + (0.28 if dpp4_override > 0 else 0.0)
            
        dt = 1.0
        total_steps = int(horizon_minutes / dt)
        
        init_x = 0.0
        init_i = self.ib + self.sulf_basal_insulin_boost
        init_gut1 = meal_carbs * 0.4
        init_gut2 = meal_carbs * 0.2
        
        state = np.array([float(initial_glucose), init_x, init_i, init_gut1, init_gut2])
        
        timeline = []
        glucose_trajectory = []
        insulin_action_trajectory = []
        
        for step in range(total_steps):
            current_minute = step * dt
            
            carb_rate = 0.0
            if current_minute < 10.0 and meal_carbs > 0:
                carb_rate = (meal_carbs * 0.4) / 10.0
                
            step_intensity = 0.0
            if post_meal_walk_minutes > 0 and walk_start_delay <= current_minute < (walk_start_delay + post_meal_walk_minutes):
                step_intensity = step_cadence
                
            basal_insulin_rate = float(self.ehr.get("insulin_basal_units", 0.0)) * 0.04
            
            k1 = self._derivatives(state, carb_rate, step_intensity, basal_insulin_rate)
            k2 = self._derivatives(state + 0.5 * dt * k1, carb_rate, step_intensity, basal_insulin_rate)
            k3 = self._derivatives(state + 0.5 * dt * k2, carb_rate, step_intensity, basal_insulin_rate)
            k4 = self._derivatives(state + dt * k3, carb_rate, step_intensity, basal_insulin_rate)
            
            state = state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            state[0] = max(40.0, min(450.0, state[0]))
            
            if step % 5 == 0:
                timeline.append(int(current_minute))
                glucose_trajectory.append(round(float(state[0]), 1))
                insulin_action_trajectory.append(round(float(state[1]), 5))
                
        return {
            "minutes": timeline,
            "glucose": glucose_trajectory,
            "insulin_action": insulin_action_trajectory,
            "final_glucose": glucose_trajectory[-1],
            "peak_glucose": max(glucose_trajectory),
            "peak_time_min": timeline[np.argmax(glucose_trajectory)],
            "time_in_range_pct": round(float(np.mean([(70.0 <= g <= 180.0) for g in glucose_trajectory]) * 100.0), 1),
            "spike_risk": 1 if max(glucose_trajectory) >= 180.0 else 0,
            "hypo_risk": 1 if min(glucose_trajectory) <= 70.0 else 0
        }
