import os
os.chdir('/sdcard')
f = open('spanish.txt','r+')
l=[]
for line in f:
    l.append(line[2:])
f.seek(0)
f.truncate()
for line in l:
    f.write(line)
    print(line)
f.close()