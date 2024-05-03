import numpy as np
import matplotlib
import constants as c

# layeroutput = []

# def nueron_output():
#     layeroutput = []
#     for weight, bias in zip(c.WEIGHTS, c.BIAS):
#         output = 0
#         for nueron_input, weight in zip(c.INPUTS, weight):
#             output += nueron_input*weight
#         output += bias
#         layeroutput.append(output)
#     print(layeroutput)   
     
# nueron_output() 

#Dot Product
#np.dot(inputs, weights) + bias

X = c.INPUTS

np.random.seed(0)

class Layer_Dense:
    def __init__(self, n_inputs, n_nuerons):
        self.weights = np.random.randn(n_inputs, n_nuerons)
        self.biases = np.zeros((1, n_nuerons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

layer1 = Layer_Dense(3, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)