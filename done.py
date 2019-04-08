sum=0
count=0
while True:
    data=input("Input data: ")
    if(data=="done"):
        break
    sum+=int(data)
    count+=1
print("Total:",sum)
print("Count of data",count)
print("Average:",float(sum/count))
