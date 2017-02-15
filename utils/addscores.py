#!/usr/bin/env python

import sys

nArgs = len(sys.argv)
scoreSep='='


if nArgs > 1:
    f = open(sys.argv[1], 'r+')
    
    if nArgs == 3:
        sep = sys.argv[2]
        if len(sep)==1:
            scoreSep = sep
        else:
            print("Sep if more than one character, ignoring...")
        
else:
    f = open('e.txt','r+')

lines=[]

for line in f:
    lines.append("0"+scoreSep+line)

f.seek(0)
f.truncate()

for line in lines:
    f.write(line)

f.close()