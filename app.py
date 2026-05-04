import streamlit as st

st.set_page_config(
    page_title="Diabetes Tracker",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Sora:wght@600;700&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

[data-testid="stSidebar"] { background: linear-gradient(160deg, #0f2027, #203a43, #2c5364); }
[data-testid="stSidebar"] * { color: #e0eafc !important; }

header[data-testid="stHeader"] { background: transparent; }

.page-title {
    font-family: 'Sora', sans-serif; font-size: 2.2rem; font-weight: 700;
    background: linear-gradient(90deg, #11998e, #38ef7d);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}
.page-sub { color: #6b7280; font-size: 1rem; margin-bottom: 1.8rem; }

.metric-card {
    background: #f8fafc; border: 1px solid #e2e8f0;
    border-radius: 14px; padding: 18px 22px; margin-bottom: 12px;
}

.stButton > button {
    background: linear-gradient(135deg, #11998e, #38ef7d) !important;
    color: #0f2027 !important; font-weight: 600 !important;
    border: none !important; border-radius: 10px !important;
    padding: 10px 28px !important; font-size: 15px !important;
}
.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 6px 20px rgba(17,153,142,0.4) !important; }

.result-safe {
    background: linear-gradient(135deg, #d1fae5, #a7f3d0);
    border-left: 5px solid #10b981; border-radius: 12px;
    padding: 20px 24px; color: #065f46; font-size: 1.1rem; font-weight: 500;
}
.result-risk {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    border-left: 5px solid #ef4444; border-radius: 12px;
    padding: 20px 24px; color: #7f1d1d; font-size: 1.1rem; font-weight: 500;
}
.result-moderate {
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    border-left: 5px solid #f59e0b; border-radius: 12px;
    padding: 20px 24px; color: #78350f; font-size: 1.1rem; font-weight: 500;
}

.food-card {
    background: white; border: 1px solid #e5e7eb;
    border-radius: 12px; padding: 14px 18px; margin-bottom: 10px;
}
.food-name { font-weight: 600; font-size: 1rem; color: #1e293b; }
.food-meta { color: #6b7280; font-size: 0.85rem; margin-top: 4px; }
.badge-veg { display:inline-block; padding:2px 10px; border-radius:20px; background:#d1fae5; color:#065f46; font-size:0.78rem; font-weight:600; }
.badge-nonveg { display:inline-block; padding:2px 10px; border-radius:20px; background:#fee2e2; color:#7f1d1d; font-size:0.78rem; font-weight:600; }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("""
<div style='text-align:center; padding: 20px 0 10px;'>
    <div style='font-size:2.5rem;'>🩺</div>
    <div style='font-family:Sora,sans-serif; font-size:1.3rem; font-weight:700; color:#38ef7d;'>DiabetesTracker</div>
    <div style='font-size:0.8rem; color:#94a3b8; margin-top:4px;'>by Akash</div>
</div>
<hr style='border-color:#2c5364; margin:10px 0 20px;'>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    ["🔍 Diabetes Prediction", "🥗 Food Recommendation"],
    label_visibility="collapsed"
)

st.sidebar.markdown("""
<hr style='border-color:#2c5364; margin:20px 0 14px;'>
<div style='font-size:0.78rem; color:#64748b; text-align:center;'>
    Powered by Random Forest ML<br>Trained on PIMA Diabetes Dataset<br>
    Accuracy: <b style='color:#38ef7d'>74.7%</b>
</div>
""", unsafe_allow_html=True)

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if "🔍 Diabetes Prediction" in page:
    from pages_modules import predict
    predict.show()
else:
    from pages_modules import food
    food.show()
