#!/usr/bin/env python

f = open('../e_expressions.txt','r+')
l=[]
for line in f:
    l.append("0="+line)
f.seek(0)
f.truncate()
for line in l:
    f.write(line)
f.close()