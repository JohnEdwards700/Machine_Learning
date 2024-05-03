import torch
import argparse
import numpy as np
from torch.utils.data import DataLoader
from torch import nn, optim
from model import Model
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
