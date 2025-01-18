# --- app.py ---
# Streamlit Web Application
import streamlit as st
from src.data_processing import preprocess_data
from src.gnn_model import FraudDetectionGNN
from src.visualization import plot_transaction_distribution
from src.anomaly_detection import detect_anomalies
import pandas as pd
import torch

st.title("Fraud Detection System for E-Commerce Platforms")

uploaded_file = st.file_uploader("Upload transaction data (CSV)", type="csv")

if uploaded_file:
    # Load and preprocess data
    data = pd.read_csv(uploaded_file)
    processed_data = preprocess_data(data)

    st.write("Preprocessed Data:")
    st.dataframe(processed_data.head())

    # Visualize transaction distribution
    st.write("Transaction Amount Distribution:")
    plot_transaction_distribution(data)

    # Detect anomalies
    st.write("Anomaly Predictions:")
    anomalies = detect_anomalies(processed_data)
    data['anomaly'] = anomalies
    st.dataframe(data[['amount', 'anomaly']])

    # Placeholder for GNN predictions (mock example)
    model = FraudDetectionGNN(input_dim=10, hidden_dim=20, output_dim=1)  # Mock dimensions
    st.write("Fraud predictions would be shown here.")