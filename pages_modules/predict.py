import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Resolve paths relative to this file — works from any working directory
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'best_model.pkl')

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at: {MODEL_PATH}")
        return None
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

def show():
    st.markdown('<div class="page-title">🔍 Diabetes Risk Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Enter your health metrics below to assess your diabetes risk using our Random Forest model.</div>', unsafe_allow_html=True)

    bundle = load_model()
    if bundle is None:
        st.stop()

    model         = bundle['model']
    scaler        = bundle['scaler']
    use_scaler    = bundle['use_scaler']
    feature_names = bundle.get('feature_names',
        ['Pregnancies','Glucose','BloodPressure','SkinThickness',
         'Insulin','BMI','DiabetesPedigreeFunction','Age'])

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### 👤 Personal Info")
        age         = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0, step=1,
                                      help="Enter 0 if not applicable")
        bmi         = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=70.0, value=25.0, step=0.1,
                                      help="Normal: 18.5–24.9")

        st.markdown("#### 💉 Blood Metrics")
        glucose        = st.number_input("Plasma Glucose (mg/dL)", min_value=50, max_value=300, value=100, step=1,
                                         help="Normal fasting: 70–99 mg/dL")
        blood_pressure = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=30, max_value=150, value=70, step=1,
                                         help="Normal: below 80 mm Hg")

    with col2:
        st.markdown("#### 🧪 Additional Measurements")
        skin_thickness = st.number_input("Triceps Skin Fold Thickness (mm)", min_value=0, max_value=100, value=20, step=1)
        insulin        = st.number_input("2-Hour Serum Insulin (µU/mL)", min_value=0, max_value=900, value=80, step=1,
                                         help="Normal 2-hr: 16–166 µU/mL")
        dpf            = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.3, step=0.01,
                                         help="Reflects family history. Higher = greater genetic risk")

        st.markdown("#### 📊 BMI Reference")
        if bmi < 18.5:
            bmi_cat, bmi_col = "Underweight", "#3b82f6"
        elif bmi < 25:
            bmi_cat, bmi_col = "Normal weight ✓", "#10b981"
        elif bmi < 30:
            bmi_cat, bmi_col = "Overweight", "#f59e0b"
        else:
            bmi_cat, bmi_col = "Obese", "#ef4444"
        st.markdown(f"""
        <div class='metric-card' style='border-left: 4px solid {bmi_col};'>
            <b>Your BMI: {bmi:.1f}</b><br>
            <span style='color:{bmi_col}; font-weight:600;'>{bmi_cat}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🔍 Predict My Risk", use_container_width=True)

    if predict_btn:
        features = pd.DataFrame(
            [[pregnancies, glucose, blood_pressure, skin_thickness,
              insulin, bmi, dpf, age]],
            columns=feature_names
        )
        features_input = scaler.transform(features) if use_scaler else features

        prediction = model.predict(features_input)[0]
        proba      = model.predict_proba(features_input)[0][1]
        risk_pct   = round(proba * 100, 1)

        st.markdown("---")
        st.markdown("### 📋 Your Result")

        c1, c2, c3 = st.columns(3)
        c1.metric("Risk Score",  f"{risk_pct}%")
        c2.metric("Prediction",  "Diabetic" if prediction == 1 else "Not Diabetic")
        c3.metric("Model Used",  "Random Forest")

        if risk_pct < 30:
            st.markdown(f"""
            <div class='result-safe'>
                ✅ <b>Low Risk ({risk_pct}%)</b><br>
                Your health metrics suggest a low probability of diabetes. Keep maintaining a healthy lifestyle!
            </div>""", unsafe_allow_html=True)
        elif risk_pct < 60:
            st.markdown(f"""
            <div class='result-moderate'>
                ⚠️ <b>Moderate Risk ({risk_pct}%)</b><br>
                Some of your metrics indicate elevated risk. Consider consulting a doctor and making lifestyle adjustments.
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='result-risk'>
                🚨 <b>High Risk ({risk_pct}%)</b><br>
                Your metrics suggest a high probability of diabetes. Please consult a healthcare professional promptly.
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.info("⚠️ **Disclaimer:** This tool is for educational purposes only and does not replace professional medical advice.")

        st.markdown("#### 🔎 Key Risk Factors in Your Input")
        factors = []
        if glucose        > 125: factors.append(f"🔴 High glucose ({glucose} mg/dL)")
        if bmi            > 30:  factors.append(f"🔴 High BMI ({bmi})")
        if blood_pressure > 89:  factors.append(f"🟡 Elevated blood pressure ({blood_pressure} mm Hg)")
        if dpf            > 0.5: factors.append(f"🟡 Notable family history (DPF: {dpf})")
        if age            > 45:  factors.append(f"🟡 Age above 45 ({age} yrs)")
        if insulin        == 0:  factors.append("🟡 Insulin value is 0 — may want to verify")

        if factors:
            for f in factors:
                st.markdown(f"- {f}")
        else:
            st.markdown("- ✅ No major individual risk flags detected.")
