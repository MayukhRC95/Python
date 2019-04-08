p=dict()
f=open("name.txt")
for n in f:
    n=n.rstrip()
    l=n.split()
    for str in l:
        p[str]=p.get(str,0)+1
print([(v,k) for (k,v) in sorted([(v,k) for k,v in p.items()], reverse=True)])
