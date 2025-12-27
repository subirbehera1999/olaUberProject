import pandas as pd
import streamlit as st
import requests
import datetime as dt

# App config
st.set_page_config(
    page_title="RideSense AI",
    page_icon="🚖",
    layout="centered"
)

# Constants
API_URL = "https://olauberproject.onrender.com/predict"
VEHICLE_TYPES = ["Select Vehicle","Prime Sedan", "Bike", "Prime SUV", "eBike", "Mini", "Prime Plus", "Auto"]
PAYMENT_METHODS = ["Select Payment","Cash", "UPI", "Credit Card", "Debit Card", "Not Applicable"]

# UI Header
st.markdown(
    """
    <h1 style="text-align:center;">🚖 RideSense AI</h1>
    <p style="text-align:center;color:gray;">
    Smart Ride Outcome Prediction using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# Input Form

with st.form("ride_prediction_form"):
    st.subheader("📋 Ride Details")

    col1, col2 = st.columns(2)

    with col1:
        vehicle_type = st.selectbox("Vehicle Type", VEHICLE_TYPES,index=0)
        pickup_location = st.text_input("Pickup Location")
        v_tat = st.number_input("Vehicle TAT (secs)", min_value=0.0, max_value=300.0, value=0.0)
        booking_value = st.number_input("Booking Value (₹)", min_value=0, value=0)
        ride_distance = st.number_input("Ride Distance (km)", min_value=0, value=0)
        ride_date = st.date_input("Ride Date",value=dt.date.today())

    with col2:
        payment_method = st.selectbox("Payment Method", PAYMENT_METHODS, index=0)
        drop_location = st.text_input("Drop Location")
        c_tat = st.number_input("Customer TAT (secs)", min_value=0.0, max_value=300.0,value=0.0)
        driver_rating = st.number_input("Driver Rating", min_value=0.0, max_value=5.0, value=0.0)
        customer_rating = st.number_input("Customer Rating", min_value=0.0, max_value=5.0, value=0.0)
        ride_time = st.time_input("Ride Time",value=dt.datetime.now().time())


    submit = st.form_submit_button("🔍 Predict Ride Outcome")

# validation and prediction 
if submit:
    ride_datetime = dt.datetime.combine(ride_date, ride_time)

    # -------- Validation --------
    errors = []

    if not pickup_location.strip():
        errors.append("Pickup Location is required")
    elif not drop_location.strip():
        errors.append("Drop Location is required")
    elif vehicle_type=="Select Vehicle":
        errors.append("Select One Vehicle")
    elif payment_method == "Select Payment":
        errors.append("Select Payment Method")


    if errors:
        for err in errors:
            st.error(err)
    else:
        # -------- Prepare Payload --------
        payload = {
            "Date": ride_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "Vehicle_Type": vehicle_type,
            "Pickup_Location": pickup_location,
            "Drop_Location": drop_location,
            "V_TAT": v_tat,
            "C_TAT": c_tat,
            "Booking_Value": booking_value,
            "Payment_Method": payment_method,
            "Ride_Distance": ride_distance,
            "Driver_Ratings": driver_rating,
            "Customer_Rating": customer_rating
        }
        # api call 
        with st.spinner("Predicting..."):
            try:
                response = requests.post(API_URL, json=payload, timeout=60)

                if response.status_code == 200:
                    result = response.json()

                    st.success("✅ Prediction Successful")

                    st.markdown(
                        f"""
                        <div style="
                            padding:20px;
                            background-color:#f0f2f6;
                            border-radius:10px;
                            text-align:center;
                            font-size:22px;
                        ">
                        🚦 <b>Predicted Ride Status:</b><br><br>
                        <span style="color:#2c7be5;"><b>{result['prediction']}</b></span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error(f"API Error: {response.text}")

            except requests.exceptions.RequestException as e:
                st.error("❌ Unable to connect to prediction service")
                st.error(str(e))

# Footer
# ==============================
st.divider()
st.caption("Built with ❤️ using FastAPI, XGBoost & Streamlit")
