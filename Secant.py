#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Common import *

def get_intervals(left, right, f, samples):
    intervals = separate_roots((left, right), f, samples)
    return intervals


# In[2]:


#Solve the equation using secant method
    
def find_all_roots(intervals, f, epsilon):
    def find_root(interval, f):
        def diff_ratio(old_x, new_x):
            v = (f(new_x) - f(old_x)) / (new_x - old_x) 
            return v
        
        x_left = interval[0]
        x_right = interval[1]
        lam = f(x_left) / f(x_right)
        x_k2 = (x_left - lam * x_right) / (1 - lam)
        x_0 = x_k2
        #old_x = (x_left + x_right) / 2
        x_k1 = x_k2 - f(x_k2) / f_prime(x_k2)
        print("x_1 after one Newton step:", x_k1)
        x_k = x_k1 - f(x_k1) / diff_ratio(x_k2, x_k1)
        iter_num = 2
        while (abs(x_k1 - x_k) >= eps):
            x_k2 = x_k1
            x_k1 = x_k
            x_k = x_k1 - f(x_k1) / diff_ratio(x_k2, x_k1)
            #print(x_k)
            iter_num += 1
        return (x_k1, x_k, iter_num, x_0)
    
    global eps
    eps = epsilon
    roots = np.array([])
    for interval in intervals:
        (x_k, x_k1, iter_num, x_0) = find_root(interval, f)
        print("Interval: [{}; {}]\nx^0 = {}\nRoot: x* = {}; f(x*) = {}\n|x^(k+1) - x^k| = {}\nNumber of iterations: {}\n"
              .format(interval[0], interval[1], x_0, x_k1, f(x_k1), abs(x_k - x_k1), iter_num))
        if len(roots) == 1:
            roots[0] = x_k1
        else:
            roots = np.append(roots, x_k1)
    return roots
    
if __name__ == "__main__":
    intervals = get_intervals(left_border, right_border, f, samples)
    find_all_roots(intervals, f, eps)

