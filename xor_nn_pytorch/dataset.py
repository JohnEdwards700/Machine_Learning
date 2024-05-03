# # import torch

# # class XORDataset(torch.utils.data.Dataset):
# #   def __init__(self, args):
# #     self.args = args.get('n',2)
# #     self.X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]])
# #     self.y = torch.tensor([0, 1, 1, 0])

# #   def __len__(self):
# #     return len(self.X)

# #   def __getitem__(self, idx):
# #     return self.X[idx], self.y[idx]

# # if __name__ == "__main__":
# #   dataset = XORDataset()
# #   print(f"Number of data points: {len(dataset)}")
# #   for i in range(len(dataset)):
# #     x, y = dataset[i]
# #     print(f"Data point {i+1}: Input: {x}, Label: {y}")


# import torch
# from itertools import product
# import numpy as np

# class Dataset(torch.utils.data.Dataset):
#     def __init__(
#             self,
#             args
#         ):

#             self.args = args
#             a = torch.zeros(self.args.n)
#             for i in product([0,1], repeat=self.args.n):
#                 a = torch.vstack((a,torch.from_numpy(np.array(i))))

#             self.X =  a[1:,:]
#             self.y = torch.from_numpy(np.concatenate((np.zeros((2**(self.args.n) - 1,1)),np.ones((1,1)))))

#     # number of samples in dataset
#     def __len__(self):
#         return len(self.y)

#     def __getitem__(self, idx):
#         return (self.X[idx],self.y[idx])

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
            self.y = torch.from_numpy(np.concatenate((np.zeros((2**(self.args.n) - 2,1)),np.ones((1,1)))))

    # number of samples in dataset
    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return (self.X[idx],self.y[idx])
