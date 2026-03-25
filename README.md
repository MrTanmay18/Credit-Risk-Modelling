# 📊 Credit Risk Modelling 

A Machine Learning project to predict **loan default risk** using customer, loan, and bureau data. This model helps financial institutions minimize losses by identifying high-risk applicants.

---

## 🚀 Project Objective

To build a credit risk model that can be used by a Risk Unit to:

- Predict whether a customer will default or not  
- Improve lending decisions  
- Reduce financial risk  

### ✅ Success Criteria

- AUC / Gini > 85  
- KS Statistic > 40  
- Maximum KS in first 3 deciles  
- Model interpretability  

---

## 📂 Dataset Description

The dataset consists of loan data from Feb 2022 to May 2024:

- **Training Data:** Feb 2022 – Feb 2024  
- **Out-of-Time Test Data:** Mar 2024 – May 2024  

---

## 🧾 Features Used

### 👤 Customer Features
- Age, Gender, Marital Status  
- Employment Status, Income  
- Number of Dependents  
- Residence Type, City, State  

### 💳 Loan Features
- Loan Type & Purpose  
- Loan Amount & Tenure  
- Net Disbursement  
- Bank Balance at Application  

### 📊 Bureau Features
- Number of Open/Closed Accounts  
- Delinquency Months  
- Total DPD (Days Past Due)  
- Credit Utilization Ratio  

---

## 🔍 Key Insights (Feature Importance)

| Feature | Insight |
|--------|--------|
| Credit Utilization Ratio | Strongest predictor of default |
| Delinquency Ratio | High delinquency → high risk |
| Loan to Income | Higher ratio increases default |
| Loan Purpose | Certain purposes are riskier |

---

## ⚙️ Data Preprocessing

- Handled missing & invalid values  
- Feature selection using:
  - IV (Information Value)  
  - VIF (Variance Inflation Factor)  
  - Domain knowledge  
- Feature engineering:
  - Loan-to-income ratio  
  - Delinquency ratio  
- Min-Max Scaling applied to numeric features  

---

## 🤖 Model Training

### Models Used:
- Logistic Regression  
- Random Forest  
- XGBoost  

### Hyperparameter Tuning:
- RandomizedSearchCV  
- Optuna  

---

## 📈 Model Performance

| Model | AUC | Gini |
|------|-----|------|
| Logistic Regression | 98% | 96% |
| XGBoost | 99% | 96% |
| Random Forest | 97% | 95% |

### 🏆 Final Model Performance:

- **AUC:** 98%  
- **Gini:** 96%  
- **Top 3 Decile Capture:** 99.53%  

---

## 🔮 How the Model Works

1. User inputs customer details via Streamlit UI  
2. Data is preprocessed (scaling + encoding)  
3. Model predicts default probability  
4. Output shown as **Risk / No Risk**  

---

## 🖥️ Project Structure
Credit-Risk-Modelling/
│
├── artifacts/              # Saved model & scaler
├── .streamlit/             # Streamlit config
├── main.py                 # Streamlit app
├── prediction_helper.py    # Prediction pipeline
├── Credit Risk Model.ipynb # Model training notebook
├── requirements.txt        # Dependencies
├── runtime.txt             # Python version
└── README.md               # Documentation

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Optuna  
- Streamlit  

---

## 📌 Key Learnings

- Importance of **recall in credit risk**  
- Feature engineering using financial ratios  
- Model evaluation using **AUC, KS, Gini**  
- Business interpretation of ML models  


---

## 👨‍💻 Author

**Tanmay**

- GitHub: https://github.com/MrTanmay18  
- LinkedIn: https://www.linkedin.com/in/tanmay-pakori  

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
