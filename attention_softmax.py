import numpy as np

v1 = np.array([2, 4, 6])
v2 = np.array([1, 1, 2])
v3 = np.array([0, 0, 2])

dot_v1_v2 = np.dot(v1, v2)
dot_v1_v3 = np.dot(v1, v3)
dot_v1_v1 = np.dot(v1, v1)

scores = np.array([dot_v1_v2, dot_v1_v3, dot_v1_v1])

softmax = np.exp(scores) / np.sum(np.exp(scores))

print(softmax)
