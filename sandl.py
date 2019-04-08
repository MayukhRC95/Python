str=""
found=0
while True:
    i=input("enter a friends name: ")
    str+=i+" "
    c=input("have more friends? ")
    if(c=="no"):
        break
l=str.split()
s=input("search which friend? ")
for f in range(len(l)):
    if(l[f]==s):
        print("friend found at",f)
        found=1
        break
if(found==0):
    print("not a friend")
