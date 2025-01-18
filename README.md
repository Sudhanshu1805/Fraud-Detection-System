# Fraud Detection System for E-Commerce Platforms

## Overview
This project detects fraudulent activities in e-commerce transactions using Graph Neural Networks, Kafka for real-time event streaming, and advanced anomaly detection techniques.

## Features
- Preprocess transaction data for model input
- Real-time integration with Kafka
- Fraud detection using a Graph Neural Network
- Visualize transaction distributions and anomaly predictions

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fraud-detection-system.git
   cd fraud-detection-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

## Usage
1. Upload a transaction dataset (CSV).
2. View preprocessed data, transaction distribution, and anomaly predictions.
3. (Future) Real-time fraud detection using Kafka and GNN.

## Technologies Used
- Graph Neural Networks
- Kafka
- Streamlit
- Python
- Matplotlib
- Scikit-learn

## Future Enhancements
- Integrate a trained GNN model for live fraud prediction.
- Add user authentication for a secure dashboard.
- Expand data preprocessing to handle larger datasets.

## License
This project is open-source under the MIT License.
