# 🌫️ Air Quality Index (AQI) Prediction Web App

This is a Machine Learning–powered Flask web application that predicts **Air Quality Index (AQI)** using pollutant concentrations such as PM2.5, CO, NO₂, SO₂, O₃, Benzene, Toluene, etc.
The application allows users to **select different ML models** (Random Forest, XGBoost, SVM, and Stacking Ensemble) and displays AQI value along with category and color indicator.

---

## 🚀 Features

- Predict AQI using multiple trained ML models
- Choose between Random Forest, SVM, XGBoost, and Ensemble
- Displays AQI category (Good, Moderate, Poor, etc.)
- UI built using Tailwind CSS
- Informative page explaining pollutants
- Dataset cleaned, transformed, and multicollinearity handled
- Cross-validation applied for reliable results
- Flask backend with saved models (.pkl files)

---

## 🧪 Machine Learning Models Used

### **1️⃣ Random Forest Regressor (Best Model)**
- Handles non-linearity well
- Not sensitive to multicollinearity
- Highest prediction accuracy

### **2️⃣ XGBoost Regressor**
- Gradient boosting approach
- Strong generalization power

### **3️⃣ Support Vector Regression (SVR)**
- Requires scaling
- Sensitive to multicollinearity

### **4️⃣ Stacking Ensemble**
- Combines Random Forest + XGBoost + SVM
- Final estimator: Linear Regression

---

## 📊 Model Performance (Best Model: Random Forest)

| Metric | Value |
|--------|--------|
| **MAE** | 0.80 |
| **MSE** | 1.37 |
| **RMSE** | 1.171 |
| **R² Score** | 0.9267 |
| **Model Accuracy** | **92.67%** |

The model predicts AQI with **high accuracy and low error**, making it stable and reliable.

---

## 🛠️ Tech Stack

### **Backend**
- Python
- Flask
- Pickle

### **Frontend**
- HTML
- Tailwind CSS

---

## 📁 Project Structure

```
AQI Predictor/
│── app.py
│── data.csv
│── model_random.pkl
│── model_xgboost.pkl
│── model_svm.pkl
│── model_ensemble.pkl
│── model.ipynb
│── requirements.txt
│── templates/
│     ├── index.html
│     └── info.html
│── static/
       └── (CSS / Images)
```

---

## ▶️ How to Run the Project Locally

### **1. Clone the repository**
```bash
git clone https://github.com/LightBringer02/AQI-Web-App.git
cd AQI-Web-App
```

### **2. Create a virtual environment**
```bash
python -m venv venv
```

### **3. Activate the environment**
**Windows**
```bash
venv\Scripts\activate
```
**Mac/Linux**
```bash
source venv/bin/activate
```

### **4. Install requirements**
```bash
pip install -r requirements.txt
```

### **5. Run the Flask app**
```bash
python app.py
```

### **6. Open in browser**
```
http://127.0.0.1:5000/
```

---

## 📘 How the Web App Works

1. User enters pollutant values  
2. User selects ML model  
3. Flask loads the respective `.pkl` model  
4. Model predicts AQI  
5. AQI value + status + color indicator are shown  
6. Additional pollutant info available on `/info`

---

## 📚 Data Preprocessing Steps

✔ Removed missing values  
✔ Removed outliers  
✔ Handled skewness using log transformation  
✔ Checked correlations  
✔ Fixed multicollinearity using VIF  
✔ Scaling for SVM dataset  
✔ Applied 5-Fold Cross Validation  
✔ Saved best models

---

## 🏁 Final Conclusion

This project demonstrates a complete end-to-end ML workflow — from data cleaning and preprocessing to model training, evaluation, and finally deployment as a Flask web application.
The **Random Forest model achieved 92.67% accuracy**, making the system highly reliable for AQI prediction.

This project helped strengthen concepts like:

- Data preprocessing  
- Feature engineering  
- Handling multicollinearity  
- Cross-validation  
- Model deployment using Flask  

The final application is accurate, fast, and practical for real-world AQI monitoring.

---

## ⭐ Future Improvements

- Integrate live AQI sensor/API data  
- Add deep learning (LSTM) model  
- Add visual graphs/charts in UI  
- Deploy online using Render / AWS / Railway  

---

## 🙌 Author

**Manan Dixit**  
B.Tech CSE (AI & ML)  
Lamrin Tech Skills University, Punjab
