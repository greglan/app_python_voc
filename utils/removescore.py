#!/usr/bin/env python

import sys


if len(sys.argv) > 1:
    f = open(sys.argv[1], 'r+')
else:
    f = open('e.txt','r+')

lines=[]

for line in f:
    lines.append(line[2:])

f.seek(0)
f.truncate()

for line in lines:
    f.write(line)

f.close()