import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Load the trained model and scaler
with open(r'C:\Users\Ranjan kumar pradhan\.vscode\model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open(r'C:\Users\Ranjan kumar pradhan\.vscode\scaling.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Title
st.title("🚨 Malware Attack Prediction")
st.markdown("Enter the following executable file features to predict if it's **Benign (1)** or **Malicious (0)**:")

# Input fields
features = [
    "Machine", "DebugSize", "DebugRVA", "MajorImageVersion", "MajorOSVersion", 
    "ExportRVA", "ExportSize", "IatVRA", "MajorLinkerVersion", "MinorLinkerVersion",
    "NumberOfSections", "SizeOfStackReserve", "DllCharacteristics", "ResourceSize", "BitcoinAddresses"
]

user_input = []
for feature in features:
    value = st.number_input(f"{feature}:", step=1)
    user_input.append(value)

# Predict Button
if st.button("Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    scaled_input = scaler.transform(input_array)  # ← FIXED this line
    prediction = model.predict(scaled_input)[0]
    
    if prediction == 1:
        st.success("✅ This file is **Benign**.")
    else:
        st.error("⚠️ This file is **Malicious**.")
