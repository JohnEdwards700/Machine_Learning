# import torch
# import argparse
# import numpy as np
# from torch.utils.data import DataLoader, TensorDataset
# from torch import nn, optim
# from model import XORNNetwork
# from dataset import Dataset

# def train(dataset, model, args):
#     batchsize = 4
#     epochs = 1000

#     dataloader = DataLoader(dataset,batch_size=batchsize, shuffle=True)
#     criterion = torch.nn.BCEWithLogitsLoss()
#     optimizer = optim.Adam(model.parameters(), lr=0.001)

#     for epoch in range(epochs):
#         for batch, (x, y) in enumerate(dataloader):
#             optimizer.zero_grad()
#             y_pred = model(x)
#             loss = criterion(y_pred,y)
#             loss.backward()
#             optimizer.step()
#             print({ 'epoch': epoch, 'batch': batch, 'loss': loss.item() })
#             print({ 'params': list(model.parameters())})

# parser = argparse.ArgumentParser()
# parser.add_argument('--max-epochs', type=int, default=4000)
# parser.add_argument('--batch-size', type=int, default=10)
# parser.add_argument('--n', type=int, default=7)
# args = parser.parse_args()

# xor_data = torch.tensor([
#   [0, 0], [0, 1], [1, 0], [1, 1]
# ])
# xor_labels = torch.tensor([0, 1, 1, 0])
# dataset = TensorDataset(xor_data, xor_labels)
# # dataset = Dataset(args)
# model = XORNNetwork(2,4)

# train(dataset, model, args)

import torch
import argparse
import numpy as np
from torch.utils.data import DataLoader
from torch import nn, optim
from model import XORModel as Model
from dataset import Dataset


def train(dataset, model, args):

    dataloader = DataLoader(dataset,batch_size=args.batch_size)
    criterion = torch.nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(args.max_epochs):
        for batch, (x, y) in enumerate(dataloader):
            optimizer.zero_grad()
            y_pred = model(x)
            loss = criterion(y_pred,y)
            loss.backward()
            optimizer.step()
            print({ 'epoch': epoch, 'batch': batch, 'loss': loss.item() })
            print({ 'params': list(model.parameters())})

parser = argparse.ArgumentParser()
parser.add_argument('--max-epochs', type=int, default=4000)
parser.add_argument('--batch-size', type=int, default=10)
parser.add_argument('--n', type=int, default=7)
args = parser.parse_args()


dataset = Dataset(args)
model = Model(dataset)
train(dataset, model, args)
