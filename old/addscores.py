f = open('../e.txt','r+')
l=[]
for line in f:
    l.append("0-"+line)
f.seek(0)
f.truncate()
for line in l:
    f.write(line)
f.close()