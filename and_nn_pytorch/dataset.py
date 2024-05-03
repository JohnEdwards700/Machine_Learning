import torch
from itertools import product
import numpy as np

class Dataset(torch.utils.data.Dataset):
    def __init__(
            self,
            args
        ):

            self.args = args
            a = torch.zeros(self.args.n)
            for i in product([0,1], repeat=self.args.n):
                a = torch.vstack((a,torch.from_numpy(np.array(i))))

            self.X =  a[1:,:]
            self.y = torch.from_numpy(np.concatenate((np.zeros((2**(self.args.n) - 1,1)),np.ones((1,1)))))

    # number of samples in dataset
    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return (self.X[idx],self.y[idx])
