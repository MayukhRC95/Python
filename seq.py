seq=[67,6,2,9,199,45,39,10,5]
max=-1
sum=0
num=0
small=None
for i in seq:
    if(small is None):
        small=i
    elif(small>i):
        small=i
    if(i>max):
        max=i
    sum+=i
    num+=1
    if(i>40):
        print("Large number",i)
print("Smallest:",small)
print("Maximum is: ",max)
print("number of elements:",num)
print("Average:",float(sum/num))
