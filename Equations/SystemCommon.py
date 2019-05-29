#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return y - x ** 2 / 2 + x - 0.5

def f1_xprime(x, y):
    return -x + 1

def f1_yprime(x, y):
    return 1

def f2(x, y):
    return 2 * x + y - y ** 3 / 6 - 1.6

def f2_xprime(x, y):
    return 2

def f2_yprime(x, y):
    return -y ** 2 / 2 + 1

def f(x, y):
    return np.array([f1(x, y), f2(x, y)], dtype=np.double)

def df(x, y):
    return np.array([[f1_xprime(x, y), f1_yprime(x, y)], [f2_xprime(x, y), f2_yprime(x, y)]], dtype=np.double)

def ysub(x):
    return 0.5 * x ** 2 - x + 0.5

def ysub_prime(x):
    return x - 1

def f2_ysub(x):
    return f2(x, ysub(x))

def f2_ysub_prime(x):
    return 2 + ysub_prime(x) - (ysub(x) ** 2) * ysub_prime(x) / 2

def infNorm(x):
    return np.max(np.abs(x))


# In[2]:


import Newton

intervals = Newton.get_intervals_table(0.0, 5.0, f2_ysub, 100)

roots = np.array([(interval[0] + interval[1]) / 2 for interval in intervals])
radii = np.array([max((ysub(interval[1]) - ysub(interval[0])) / 2, interval[1] - interval[0]) for interval in intervals])

print("x values for starting points: " + str(roots))
print("Sphere radia: " + str(radii))

points = np.array([(root, ysub(root)) for root in roots], dtype=np.double)

print("Starting points: " + str(points))

