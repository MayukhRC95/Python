p=dict()
f=open("name.txt")
for n in f:
    n=n.rstrip()
    l=n.split()
    for str in l:
        if(str in p):
            p[str]=p[str]+1
        else:
            p[str]=1
print(p)
p=dict()
f=open("name.txt")
for n in f:
    n=n.rstrip()
    l=n.split()
    for str in l:
        p[str]=p.get(str,0)+1
print(p)
