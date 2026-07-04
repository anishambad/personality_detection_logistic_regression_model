# 🧠 Personality Prediction App

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-lightblue?logo=numpy)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)

---

## 🌟 Live Demo
Try the app here: [Personality Prediction App](https://personalitydetectionlogisticregressionmodel-zjuholzrahjf4ns2tx.streamlit.app/)

---

Welcome to the **Personality Prediction App** 🎉  
This project is an interactive **Streamlit web application** that predicts personality type (*Introvert, Ambivert, Extrovert*) based on multiple behavioral and lifestyle traits such as social energy, talkativeness, empathy, curiosity, planning, spontaneity, and more.  

The underlying model is a **Logistic Regression** trained on encoded features and achieves an accuracy of **99.75%**.  
It’s designed to showcase an end‑to‑end ML workflow — from preprocessing and training to deployment with Streamlit.

---

## ✨ Features
- 🎯 **Accurate Predictions** – Predicts personality type using a logistic regression model.  
- 🎛️ **Interactive UI** – Sliders for all features to make input intuitive.  
- 📊 **Comprehensive Traits** – Includes social, emotional, lifestyle, and work‑style factors.  
- 🌐 **Streamlit Powered** – Clean, responsive web interface.  

---

## 📂 Project Structure

```bash
personality-prediction/
│
├── app.py                        # Streamlit UI
├── model.pkl                     # Trained logistic regression model
├── scaler.pkl                    # Scaler used for preprocessing
├── personality_detection_notebook.ipynb  # Training notebook
├── personality_synthetic_dataset.xlsx    # Dataset
├── requirements.txt              # Dependencies
├── README.md                     # Project overview
└── .gitignore                    # Ignore unnecessary files
```

🏁 Quick Setup Guide

1️⃣ Clone the repository
```bash
git clone https://github.com/<anishambad>/personality-prediction.git
cd personality-prediction
```
2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

3️⃣ Run the app

```bash
streamlit run app.py
```

🛠️ Tech Stack

🐍 Python
📦 Pandas
🔢 NumPy
📈 Scikit-learn
🌐 Streamlit
📈 Model Details

Algorithm: Logistic Regression
Training: Encoded categorical + numeric features
Accuracy: 99.75%
Target: Personality Type (Introvert, Ambivert, Extrovert)

👤 Author  
Built by Anish — Third‑year Computer Engineering student at SPPU, passionate about data science, analytics, and machine learning.

