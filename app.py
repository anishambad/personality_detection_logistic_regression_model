import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load model and scaler
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Personality Predictor", page_icon="🧠", layout="wide")

st.title("🧠 Personality Type Prediction")
st.markdown("Use the sliders below to set your traits and click **Predict** to see your personality type.")

st.sidebar.header("ℹ️ About")
st.sidebar.info(
    "This app predicts personality type using a trained Logistic Regression model. "
    "Adjust the sliders to reflect your traits and press Predict."
)

# -----------------------------
# Input Sliders
# -----------------------------
features = [
    "social_energy", "alone_time_preference", "talkativeness", "deep_reflection",
    "group_comfort", "party_liking", "listening_skill", "empathy",
    "organization", "leadership", "risk_taking", "public_speaking_comfort",
    "curiosity", "routine_preference", "excitement_seeking", "friendliness",
    "planning", "spontaneity", "adventurousness", "reading_habit",
    "sports_interest", "online_social_usage", "travel_desire", "gadget_usage",
    "work_style_collaborative", "decision_speed"
]

st.markdown("## 🎚️ Personality Traits")

cols = st.columns(3)  # 3 sliders per row for neat layout
values = []

for i, feature in enumerate(features):
    col = cols[i % 3]
    with col:
        val = st.slider(feature.replace("_", " ").title(), 0, 10, 5)
        values.append(val)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🚀 Predict Personality Type"):
    input_data = np.array([values])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    # Map numeric prediction to readable labels
    label_map = {
        0: "Introvert",
        1: "Ambivert",
        2: "Extrovert"
    }

    personality_label = label_map.get(prediction, "Unknown")

    st.subheader("Prediction Result")
    st.write(f"🎯 Predicted Personality Type: **{personality_label}**")
