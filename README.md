# 🩺 DiabetesTracker

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red)
![Model](https://img.shields.io/badge/Model-Random%20Forest-green)
![Accuracy](https://img.shields.io/badge/Accuracy-74.7%25-brightgreen)

A machine learning web application for **diabetes risk prediction** and **food recommendations**, built with Python and Streamlit.

---

## 🖥️ Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://akash-xai-diabetestracker-app-ajsjut.streamlit.app/)

> 🔗 **[https://akash-xai-diabetestracker-app-ajsjut.streamlit.app/](https://akash-xai-diabetestracker-app-ajsjut.streamlit.app/)**

---

## 🌟 Features

- **Diabetes Risk Prediction** — Enter your health metrics and get an instant risk assessment (Low / Moderate / High) powered by a Random Forest model
- **Food Recommendations** — Browse 160+ diabetes-friendly foods filtered by nutrient, food type (Veg/Non-Veg), and sorted by price
- **Live BMI Indicator** — Real-time BMI category displayed as you fill the form
- **Key Risk Factor Breakdown** — Highlights which specific inputs are contributing to your risk
- **No Login Required** — Open access, no account needed

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| ML Model | Random Forest (scikit-learn) |
| Data Processing | Pandas, NumPy |
| Dataset | PIMA Indians Diabetes Dataset |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```
DiabetesApp/
├── app.py                  # Main entry point & navigation
├── best_model.pkl          # Trained Random Forest model
├── requirements.txt        # Python dependencies
├── data/
│   ├── diabetes.csv        # PIMA diabetes dataset
│   └── food_dataset.csv    # Food recommendation dataset
└── pages_modules/
    ├── predict.py          # Diabetes prediction page
    └── food.py             # Food recommendation page
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akash-xai/DiabetesTracker.git
   cd DiabetesTracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. Open your browser at `http://localhost:8501`

---

## 🤖 ML Model Details

| Property | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Number of Trees | 200 |
| Test Accuracy | **74.7%** |
| Dataset | PIMA Indians Diabetes (768 samples) |
| Features Used | Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age |

### Data Preprocessing
- Replaced biologically invalid zero values with column medians for: Glucose, Blood Pressure, Skin Thickness, Insulin, BMI
- Stratified 80/20 train-test split

---

## 📊 Input Features

| Feature | Description | Normal Range |
|---|---|---|
| Age | Patient age in years | — |
| Pregnancies | Number of times pregnant | 0–17 |
| BMI | Body Mass Index | 18.5–24.9 |
| Glucose | Plasma glucose concentration (mg/dL) | 70–99 |
| Blood Pressure | Diastolic blood pressure (mm Hg) | < 80 |
| Skin Thickness | Triceps skin fold thickness (mm) | — |
| Insulin | 2-hour serum insulin (µU/mL) | 16–166 |
| Diabetes Pedigree | Family history score | 0.0–2.5 |

---

## ⚠️ Disclaimer

This application is built for **educational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical decisions.

---

## 👨‍💻 Author

**Akash**  
GitHub: [@akash-xai](https://github.com/akash-xai)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
