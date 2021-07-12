#!usr/bin/env python3

import sys
import numpy as np
import math
# Functions

def eulers_method(f,y0,b,N):
    '''
    f: the function f' that we wish to evaluate
    y0: initial value f(0)
    b: endpoint of x
    N: number of subintervals (number of steps)
    Return: a list of tuples (xi, yi) for i = 0,...,N
    '''
    ### START CODE HERE ###
    step = b / N
    x = 0
    y = y0
    res = []
    
    
    while b - x >=0.00000001:

        y += step * f(x)
        x += step
        res.append((x,y))
    return res

def f_derivative(x):
    return math.exp(x) * math.sin(x)

def f2(x):
    return 2*x

def main():
    soln1 = eulers_method(f_derivative, 0.0, 30.0, 2000)
    print("Test Case 1: f'(x) = e^x * sin(x) and f(0) = 0, steps = 2000, evaluate f(30)")
    print(f"When x = {soln1[-1][0]:.3f}, y is approximated to be {soln1[-1][1]:.3f}")

    soln2 = eulers_method(f2, 0, 30, 20000)
    print("Test Case 2: f'(x) = 2x and f(0) = 0, steps = 20000, evaluate f(30)")
    print(f"When x = {soln2[-1][0]}, y is approximated to be {soln2[-1][1]}")

# Main Execution

if __name__ == '__main__':
    main()
    
    
'''
Test Case 1: f'(x) = e^x * sin(x) and f(0) = 0, steps = 2000, evaluate f(30)
When x = 30.000, y is approximated to be -6024467273647.519
Test Case 2: f'(x) = 2x and f(0) = 0, steps = 20000, evaluate f(30)
When x = 30.00000000000108, y is approximated to be 899.955000000031
'''