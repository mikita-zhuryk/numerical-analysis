#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Plot the function

import math
import numpy as np
import matplotlib.pyplot as plt

samples = 20
left_border = 0.01
right_border = 3
delta = (right_border - left_border) / samples
eps = 10 ** -5

def f(x):
    l = math.log(x)
    return 3 * l ** 2 + 6 * l - 5

def f_prime(x):
    l = math.log(x)
    return 6 * (l + 1) / x

def phi(x):
    return math.e ** ((-3 * math.log(x) ** 2 + 5) / 6)

def phi_prime(x):
    return -phi(x) * math.log(x) / x


# In[2]:


x_values = np.linspace(left_border, right_border, samples)
f_values = np.zeros(np.shape(x_values))

for i in range(samples):
    f_values[i] = f(x_values[i])


# In[3]:


#Root separation

def separate_roots(x_values, f_values):
    intervals = []
    for i in range(samples - 1):
        if (f_values[i + 1] * f_values[i] < 0):
            intervals = np.append(intervals, i)
    return intervals

intervals = separate_roots(x_values, f_values)
        
print(intervals)