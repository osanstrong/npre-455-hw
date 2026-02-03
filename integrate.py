import numpy as np

# Shortform

def sinh(x):
    return np.sinh(x)

def sqrt(x):
    return x**0.5

def exp(x):
    return np.exp(x)

# The Watt function (not the electric Watt)

def watt(E: float):
    '''
    Docstring for watt
    
    :param E: Neutron energy. Must be in units of MeV
    :type E: float
    '''
    return 0.4865 * sinh(sqrt(2*E)) * exp(-1*E)

# Integrating procedures

def center_integral(func, a:float, b:float, steps:int):
    diff = b - a
    dx = diff / steps
    sum = 0
    for i in range(steps): # i.e. excluding b itself
        left_x = a + (i+0.5)*dx
        left_val = func(left_x)
        sum += left_val * dx
    return sum

def left_integral(func, a:float, b:float, steps:int):
    diff = b - a
    dx = diff / steps
    sum = 0
    for i in range(steps): # i.e. excluding b itself
        left_x = a + i*dx
        left_val = func(left_x)
        sum += left_val * dx
    return sum




