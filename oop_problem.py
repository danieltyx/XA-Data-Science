"""
The goal of this exercise is to create a dummy "neural network" using classes and functinos in python.

The neural network should contain the following classes:
    1. class Net
    2. class Neuron

class Net:
    this is the class for the neural network. It should include:
        - an attribute,"neurons", of all the neurons in the class
        - an init function taking in the list of neurons
        - a function, "predict", for predicting the output. Takes in the int "input". The prediction
            is evaluated by taking the sum of the input and the sum of the label of the neurons
            (note this is NOT even close to how a neural network works... just for the purpose of this exercise)

class Neuron:
    this is the class for a single neuron in the network. It should include:
        - an attribute, "childs", for all the neurons that it is connected to
        - an attribute, "label", for the label of neuron. The label is an integer.
        - an init function, taking in the label of the neuron
        - a function, "get_lable", to return the lable of the neuron
        - a function, "connect", to take in a child and connect the neuron to a child

Test your code by creating a network with at least 5 neurons with 6 connections. Predict using at least 3 inputs.

"""

class Net():
    neurons = []

    def __init__(self, neurons):
        self.neurons = neurons 

    
    def predict(self, input):
        cnt = input
        for neuron in self.neurons:
            cnt += neuron.label 
        return cnt

class Neuron():
    childs = []
    label = 0
    def __init__(self, label):
        self.label = label

    def get_lable(self):
        return self.label
    
    def connect(self,child_neuron):
        self.childs.append(child_neuron)



n1 = Neuron(1)
n2 = Neuron(2)
n3 = Neuron(3)
n1.connect(n2)
n1.connect(n3)
print(n1.get_lable())
net1 = Net([n1,n2,n3])
print(net1.predict(4))

