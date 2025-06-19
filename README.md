# 🩺 Diabalyze - Diabetes Prediction with Machine Learning

**Diabalyze** is a machine learning-based web application that predicts whether a person is diabetic or not based on medical inputs like glucose level, insulin, BMI, and more.

This project is built using a trained Gradient Boosting Classifier model and provides an easy-to-use interface via **Streamlit**.

---

## 🚀 Features
- Machine Learning models used: Logistic Regression, KNN, Decision Tree, Gradient Boosting
- Full pipeline: data cleaning, outlier removal, feature engineering, one-hot encoding
- Model evaluation with accuracy score, confusion matrix, and classification report
- Web interface built using **Streamlit**

---

## 🧪 Inputs
- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

---

## 🖥️ How to Run

### 1. Clone the repo and install dependencies:
```bash
pip install streamlit numpy scikit-learn
```

### 2. Make sure `Diabalyze.pkl` (your trained model) is in the same directory.

### 3. Run the Streamlit app:
```bash
streamlit run diabalyze_app.py
```

---

## 📦 File Structure
```
├── diabalyze_app.py       # Streamlit web app
├── Diabalyze.pkl          # Trained ML model (must be generated separately)
└── README.md              # Project documentation
```

---

## ✅ Future Improvements
- Add cross-validation and hyperparameter tuning
- Visualize model insights using SHAP
- Enable batch prediction via CSV upload

---
