#!/usr/bin/env python
# coding: utf-8


from Common import *

plt.plot(x_values, f_values)


#Check all conditions

def check_Lipschitz(interval):
    x = x_values[interval]
    xwave = x_values[interval + 1]
    q = 15
    temp_q = 0
    q_samples = 10000
    for i in range(q_samples):
        diff = (i + 1) * (xwave - x) / (2 * (q_samples))
        left = (x + xwave) / 2 - diff
        right = left + 2 * diff
        temp_q = abs((phi(right) - phi(left)) / (right - left))
        #print("Calculating q on interval [{0}; {1}]; q_{2} = {3}".format(left, right, i, temp_q))
        if (temp_q < q):
            q = temp_q
            
    if (q < 1):
        print("Lipschitz hypothesis satisfied with q =", q)
    else:
        print("Lipschitz hypothesis not satisfied with q =", q)
    return q
        
def check_phi_prime(interval):
    x = x_values[interval]
    xwave = x_values[interval + 1]
    max_phi_prime = 0
    cur_phi_prime = 0
    for cur_x in np.linspace(x, xwave, 300):
        cur_phi_prime = abs(phi_prime(cur_x))
        if (cur_phi_prime > max_phi_prime):
            max_phi_prime = cur_phi_prime
    print("max|phi'(x)| =", max_phi_prime)
    return max_phi_prime

#Solve the equation using simple iteration method

def find_root(interval):
    x_left = x_values[interval]
    x_right = x_values[interval + 1]
    lam = f(x_left) / f(x_right)
    old_x = (x_left - lam * x_right) / (1 - lam)
    #old_x = (x_left + x_right) / 2
    new_x = phi(old_x)
    m = abs(new_x - old_x)
    print("x[0] =", old_x, "; x[1] =", new_x)
    num_iter = 1

    while (abs(new_x - old_x) >= eps):
        old_x = new_x
        new_x = phi(old_x)
        num_iter = num_iter + 1

    print("X* =", new_x, "; f(X*) =", f(new_x))
    print("|x^(k+1) - x^k| =", abs(new_x - old_x))
    print("Number of iterations:", num_iter)
    return m

for i in intervals:
    interval = int(i)
    print("Interval #", interval + 1)
    print("Interval borders:", x_values[interval], x_values[interval + 1])
    m = find_root(interval)
    print()
    q = check_Lipschitz(interval)
    max_prime = check_phi_prime(interval)
    print()
    print("m =", m)
    print("q =", q)
    print("delta =", delta)
    print()
    print("m / (1 - q) =", abs(m / (1 - q)))
    if abs(m / (1 - q)) <= delta:
        print("m / (1 - q) <= delta")
    else:
        print("m / (1 - q) > delta")
    print()
    

