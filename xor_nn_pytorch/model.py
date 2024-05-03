# import torch 
# import torch.nn as nn

# class XORNNetwork(nn.Module):
#     def __init__(self, n_inputs, hidden_size):
#         super(XORNNetwork, self).__init__()
#         self.linear1 = nn.Linear(n_inputs, hidden_size)
#         self.relu = nn.ReLU()
#         self.linear2 = nn.Linear(hidden_size, 1)
        
#     def forward(self, x):
#         x=self.linear1(x)
#         x=self.relu(x)
#         x=self.linear2(x)
#         return x
    
# if __name__=="__main__":
#     n_inputs = 2 
#     hidden_size = 4
#     model = XORNNetwork(n_inputs, hidden_size)
#     print(model)

import torch
from torch import nn

class XORModel(nn.Module):
    def __init__(self, dataset):
        super(XORModel, self).__init__()
        self.hidden = nn.Linear(dataset.args.n, dataset.args.n)
        self.activation = nn.ReLU()
        self.Linear2 = nn.Linear(dataset.args.n,1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.activation(x)
        x = self.Linear2(x)

        return x
