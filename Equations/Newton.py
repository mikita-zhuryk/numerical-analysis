#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Common import *


# In[2]:


#Solve the equation using Newton method

def find_all_roots(f, f_prime, intervals, epsilon):
    def find_root(interval):
        x_left = interval[0]
        x_right = interval[1]
        lam = f(x_left) / f(x_right)
        x_0 = old_x = (x_left - lam * x_right) / (1 - lam)
        #x_0 = old_x = (x_left + x_right) / 2
        new_x = old_x - f(old_x) / f_prime(old_x)
        iter_num = 1
        while (abs(old_x - new_x) >= eps):
            old_x = new_x
            #print(new_x)
            new_x = old_x - f(old_x) / f_prime(old_x)
            iter_num += 1
        return (old_x, new_x, iter_num, x_0)
    global eps
    eps = epsilon
    roots = np.array([])
    for interval in intervals:
        (x_k, x_k1, iter_num, x_0) = find_root(interval)
        print("Interval: [{}; {}]\nx^0 = {}\nRoot: x* = {}; f(x*) = {}\n|x^(k+1) - x^k| = {}\nNumber of iterations: {}\n"
              .format(interval[0], interval[1], x_0, x_k1, f(x_k1), abs(x_k - x_k1), iter_num))
        roots = np.append(roots, x_k1)
    return roots


# In[3]:


if __name__ == "__main__":
    intervals = get_intervals_table(left_border, right_border, f, samples)
    find_all_roots(f, f_prime, intervals, eps)
    
    print(-(f(0.14134905726406316) / f_prime(0.14134905726406316)))
    h_0 = -(f(1.8834601238122997) / f_prime(1.8834601238122997))
    print(h_0)

    def f_double_prime(x):
        return -6 * math.log(x) / x ** 2

    x_0 = 1.8834601238122997
    x_1 = x_0 + h_0

    print(x_0 + 2 * h_0)

    print(f_double_prime(x_0))
    print(f_double_prime(x_0 + 2 * h_0))
    M = max(abs(f_double_prime(x_0)), abs(f_double_prime(x_0 + 2 * h_0)))
    print(2 * abs(h_0) * M)
    print(f_prime(x_0))
    print()

    alpha = 0.2058310407946963193

    k = math.log2(math.log(alpha * eps) / math.log(alpha * abs(x_1 - x_0)))

    print(k)

