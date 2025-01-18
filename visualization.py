# --- visualization.py ---
# Visualize data and predictions
import matplotlib.pyplot as plt

def plot_transaction_distribution(data):
    """Plot transaction amount distribution."""
    plt.hist(data['amount'], bins=50, alpha=0.7)
    plt.title('Transaction Amount Distribution')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.show()
