#!/usr/bin/env python

prevSep='-'
newSep='='

f = open('e.txt','r+')
lines=[]

for line in f:
    lines.append(line.replace(prevSep, newSep))

f.seek(0)
f.truncate()

for line in lines:
    f.write(line)

f.close()
