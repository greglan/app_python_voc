# -*- coding: utf-8 -*-
#!/usr/bin/env python

from math import *
import matplotlib.pyplot as plt

def p(x):
    return 0.3−0.00252525*x

x = [k for k in range(100)]
p_x = [p(k) for k in range(100)]

plt.plot(x, p_x)

plt.xlim([0,100])
plt.ylim([0,1])

plt.show()

print("Loi: ", sum(p(k) for k in range(100))==1)