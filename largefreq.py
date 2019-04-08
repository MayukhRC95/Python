p=dict()
na=input("enter file: ")
f=open(na)
for n in f:
    n=n.rstrip()
    l=n.split()
    for str in l:
        if(str in p):
            p[str]=p[str]+1
        else:
            p[str]=1
bigcount=None
bigword=None
for key,value in p.items():
    if(bigcount is None or value>bigcount):
        bigword=key
        bigcount=value
print(bigword,bigcount)
