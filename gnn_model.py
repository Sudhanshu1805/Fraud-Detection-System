# --- gnn_model.py ---
# Implement a Graph Neural Network
import torch
import torch.nn as nn

class FraudDetectionGNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(FraudDetectionGNN, self).__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.layer2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.sigmoid(self.layer2(x))
        return x
