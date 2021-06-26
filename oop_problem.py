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
    def __init__(self, neurons):
        """
        enter your code here
        """
    
    def predict(self, input):
        """
        enter your code here
        """
    

class Neuron():
    """
    enter your code here
    """

