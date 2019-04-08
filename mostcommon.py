p=dict()
f=open(input("Enter file name: "))
num=int(input("How many words? "))
for n in f:
    n=n.rstrip()
    l=n.split()
    for str in l:
        p[str]=p.get(str,0)+1
lis=list()
for k,v in p.items():
    lis.append((v,k))
lis=sorted(lis, reverse=True)
for k,v in lis[:num]:
    print(v,k)
