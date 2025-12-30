# 🚖 Ride Status Prediction System (OLA/Uber-Like)

## 📌 Project Overview
This project predicts the **final ride status** for a cab booking using machine learning.
The model classifies each ride into one of the following outcomes:

- **Success**
- **Driver Not Found**
- **Cancelled by Driver**
- **Cancelled by Customer**

The system is built end-to-end — from data preprocessing and feature engineering to **API deployment and live user interaction**.

---

## 🧠 Problem Statement
Ride cancellations and driver availability issues directly impact customer experience.
This project helps predict ride outcomes **before execution**, enabling:

- Operational risk reduction
- Better customer communication
- Smarter dispatch planning

---

## 📊 Dataset & Features

### Input Features (Raw Data)
- `Date` (combined date-time input)
- `Vehicle_Type`
- `Pickup_Location`
- `Drop_Location`
- `V_TAT`
- `C_TAT`
- `Booking_Value`
- `Payment_Method`
- `Ride_Distance`
- `Driver_Ratings`
- `Customer_Rating`

### Target Variable
- `Ride_Status` (Multi-class)

---

## ⚙️ Feature Engineering
Custom transformers were implemented using **scikit-learn compatible classes**:

- Date-time extraction (month, weekday, hour, AM/PM, day type)
- Flag variable generation (threshold-based indicators)
- Missing value handling via custom data cleaner
- Categorical encoding using:
  - One-Hot Encoding
  - Target Encoding

All steps are integrated into a **single ML pipeline**.

---

## 🤖 Model & Evaluation
- **Algorithm**: XGBoost (Multi-class Classification)
- **Evaluation Metric**: F1-Score (class-balanced)
- **Imbalance Handling**: Sample weighting
- **Model Persistence**: Pickle (`.pkl`)

---

## 🚀 Deployment Architecture

### Backend API
- **Framework**: FastAPI
- **Hosting**: Render (Free Tier)
- **Endpoint**: *https://olauberproject.onrender.com/predict*

---

### Frontend
- **Framework**: Streamlit  
- User-friendly UI for single-record prediction  
- Input validation & default handling  

---

## 🔗 Live Links
- **API Endpoint**: *https://olauberproject.onrender.com/predict*  
- **Streamlit App**: *https://ridebookingstatus.streamlit.app/*  

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- scikit-learn  
- XGBoost  
- FastAPI  
- Streamlit  
- Render  

---

## 🧪 API Request Example
{
  "Date": "2024-08-25 14:30",
  "Vehicle_Type": "Auto",
  "Pickup_Location": "Bhubaneswar",
  "Drop_Location": "Cuttack",
  "V_TAT": 25,
  "C_TAT": 18,
  "Booking_Value": 350,
  "Payment_Method": "Cash",
  "Ride_Distance": 12,
  "Driver_Ratings": 4.6,
  "Customer_Rating": 4.4
}

---

## ✅ Key Highlights
- End-to-end ML pipeline
- Production-ready deployment
- Handles unseen categorical values safely
- Clean separation of training, API, and UI
- Real-world business use case

---

## 👨‍💻 Author
### Subir Kumar Behera
Aspiring Data Analyst | **Machine Learning** Enthusiast
