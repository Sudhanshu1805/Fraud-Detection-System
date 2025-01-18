# --- data_processing.py ---
# Preprocess transaction data
import pandas as pd

def preprocess_data(data):
    """Preprocesses the transaction data for GNN input."""
    # Example: Normalizing transaction amounts
    data['amount_normalized'] = data['amount'] / data['amount'].max()
    # Example: Encoding categorical features
    data = pd.get_dummies(data, columns=['transaction_type'], drop_first=True)
    return data