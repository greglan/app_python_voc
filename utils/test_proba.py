# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
    Test different probability laws
"""

from math import *
import random as rd
import matplotlib.pyplot as plt

score_max=4+1
score_min=0
N=10000                                                                         # Number of tests

tests = []
data = []


def expo(l):
    return floor(rd.expovariate(l))


for k in range(N):
    tests.append(expo(1.5))

for i in range(score_max):
    data.append( tests.count(i)/N )
    
plt.plot(range(score_max), data)
plt.xlim([score_min, score_max])

print("Sum of probas: "+str( sum(data[k] for k in range(score_max-1)) ))

plt.show()