# app.py
import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open("model/spam_rf_model.pkl", "rb") as f:
    model, scaler = pickle.load(f)

st.set_page_config(page_title="Spam Classifier", layout="wide")
st.title("📧 Spam Email Classifier")

st.markdown("""
Enter values for some common word/character frequencies and features.  
The model will predict whether the email is **Spam** or **Not Spam**.
""")

# Select a subset of important features for simplicity
input_features = [
    'word_freq_make', 'word_freq_free', 'word_freq_your',
    'word_freq_000', 'word_freq_money', 'char_freq_$',
    'capital_run_length_average', 'capital_run_length_longest',
    'capital_run_length_total'
]

# Collect inputs
inputs = []
for feature in input_features:
    value = st.slider(f"{feature}", 0.0, 100.0, 0.0, step=0.5)
    inputs.append(value)

# Fill in rest of the 57 features with 0s
full_input = [0.0] * 57
for i, f in enumerate(input_features):
    idx = i if f in input_features else -1
    if idx >= 0:
        full_input[i] = inputs[i]

# Scale
scaled_input = scaler.transform([full_input])

# Predict
if st.button("sPredict"):
    pred = model.predict(scaled_input)[0]
    label = "Not Spam" if pred == 0 else "Spam"
    st.success(f"Prediction: **{label}**")
