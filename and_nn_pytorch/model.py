import torch
from torch import nn

class Model(nn.Module):
    def __init__(self, dataset):
        super(Model, self).__init__()
        self.hidden = nn.Linear(dataset.args.n, dataset.args.n)
        self.activation = nn.ReLU()
        self.olayer = nn.Linear(dataset.args.n,1)

    def forward(self, x):
        out = self.olayer(x)

        return out
