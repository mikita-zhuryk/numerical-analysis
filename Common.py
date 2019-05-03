#!/usr/bin/env python
# coding: utf-8

#Plot the function

import math
import numpy as np
import matplotlib.pyplot as plt

samples = 20
left_border = 0.01
right_border = 3
delta = (right_border - left_border) / samples
eps = 10 ** -8

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

def calc_f_values(x_values, f):
    f_values = np.zeros(np.shape(x_values))
    for i in range(samples):
        f_values[i] = f(x_values[i])
    return f_values

#Root separation

def separate_roots(interval, f, new_samples):
    global left_border
    left_border = interval[0]
    global right_border
    right_border = interval[1]
    global samples
    samples = new_samples
    x_values = np.linspace(left_border, right_border, samples)
    f_values = calc_f_values(x_values, f)
    intervals = np.empty((1, 2))
    for i in range(samples - 1):
        if (f_values[i + 1] * f_values[i] < 0):
            if (intervals.shape[0] == 1):
                intervals[0] = [x_values[i], x_values[i + 1]]
            else:
                intervals = np.vstack((intervals, [x_values[i], x_values[i + 1]]))
    return intervals

def dichotomy(f, init_intervals):
    def dichotomy_single_root(interval):
        if (interval[1] - interval[0] < delta):
            return interval
        print("[{}; {}]".format(interval[0], interval[1]))
        center = (interval[0] + interval[1]) / 2
        print(f(interval[0]) * f(center))
        if (f(interval[0]) * f(center) < 0):
            return dichotomy_single_root([interval[0], center])
        else:
            return dichotomy_single_root([center, interval[1]])
        
    for i in range(len(init_intervals)):
        init_intervals[i] = dichotomy_single_root(init_intervals[i])
    return init_intervals

def get_intervals_table(left, right, f, samples):
    intervals = separate_roots((left, right), f, samples)
    return intervals