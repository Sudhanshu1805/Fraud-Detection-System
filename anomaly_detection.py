# --- anomaly_detection.py ---
# Detect fraud anomalies in transactions
from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(data):
    """Uses Isolation Forest to detect anomalies in the given data."""
    model = IsolationForest(contamination=0.1, random_state=42)
    features = data[['amount_normalized']]
    predictions = model.fit_predict(features)
    return predictions
