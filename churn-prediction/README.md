# Advanced Customer Churn Prediction

## 📌 Overview
This is a production-style machine learning project to predict customer churn.

---

## 📥 Input
You must download dataset from:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Place it in:
data/churn.csv

---

## ▶️ Run Project

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Train model
python train.py

Expected output:
Accuracy: ~0.82-0.86
ROC-AUC: ~0.87-0.91

### Step 3: Run API
python app.py

---

## 🔗 API Usage

### Endpoint
POST /predict

### Sample Input JSON
{
  "tenure": 12,
  "MonthlyCharges": 70,
  "TotalCharges": 840,
  "SeniorCitizen": 0
}

### Sample Output
{
  "prediction": 0,
  "probability": 0.23
}

---

## 🚀 Upload to GitHub

1. Create repo on GitHub
2. Open terminal:
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_REPO_URL
   git push -u origin main

---

## 🧠 Resume Line

Built an advanced churn prediction system using XGBoost achieving ~0.90 ROC-AUC with API deployment and modular ML pipeline.
