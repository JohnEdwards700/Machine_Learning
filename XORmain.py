import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn

class XORNetwork(nn.Module):
  def __init__(self, n_inputs, hidden_size):
    super(XORNetwork, self).__init__()
    self.linear1 = nn.Linear(n_inputs, hidden_size)
    self.relu = nn.ReLU()
    self.linear2 = nn.Linear(hidden_size, 1)

  def forward(self, x):
    x = self.linear1(x)
    x = self.relu(x)
    x = self.linear2(x)
    return x



# Define XOR data (replace with your actual dataset)
xor_data = torch.tensor([
  [0, 0], [0, 1], [1, 0], [1, 1]
])
xor_labels = torch.tensor([0, 1, 1, 0])

# Create dataset and dataloader
dataset = TensorDataset(xor_data, xor_labels)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)  # Adjust batch size as needed

# Hyperparameters
learning_rate = 0.1  # May require adjustments
epochs = 1000  # May require adjustments

# Define model and loss function
model = XORNetwork(2, 4)  # Adjust n_inputs and hidden_size if needed
criterion = nn.BCELoss()  # Binary Cross Entropy loss for binary classification (XOR output is 0 or 1)
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  # Stochastic Gradient Descent optimizer

# Train the model
for epoch in range(epochs):
  for data, target in dataloader:
    # Forward pass
    outputs = model(data.float())

    # Loss calculation
    loss = criterion(outputs, target.view(-1).float())  # Flatten target labels

    # Backward pass and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print training progress (optional)
    if (epoch + 1) % 100 == 0:
      print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Test the model (optional)
with torch.no_grad():
  for data, target in dataloader:
    outputs = model(data.float())
    predictions = (outputs > 0.5).float()  # Threshold for binary classification
    print(f"Input: {data}  Prediction: {predictions}  Target: {target}")

print("Training complete!")

if __name__ == "__main__":
  n_inputs = 2  # Example for 2-input XOR
  hidden_size = 4  # Example hidden layer size
  model = XORNetwork(n_inputs, hidden_size)
  print(model)