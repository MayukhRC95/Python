f=open('fl.txt')
for line in f:
    line=line.rstrip()
    l=line.split()
    if(len(l)<3 or l[0]!='From'):
        continue
    print(l[2])
