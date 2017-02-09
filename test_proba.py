# -*- coding: utf-8 -*-
#!/usr/bin/env python

from math import *
import matplotlib.pyplot as plt

mu=0
sigma=2
l = 1.5
N=10000


def f():
    n = floor( rd.normalvariate(mu, sigma))
    return n

def expo():
    return floor(rd.expovariate(l))

data = [0 for k in range(10)]

for k in range(N):
    x=expo()
    if x <10:
        data[x] += 1

for i in range(10):
    data[i] = data[i]/N
    
plt.plot(range(10), data)
plt.xlim([0,6])

plt.show()

