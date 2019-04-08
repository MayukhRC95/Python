l=list()
while True:
    i=input("Enter a number: ")
    if(i=="done"):
        break
    try:
        l.append(float(i))
    except:
        print("wrong input")
print("Average:",sum(l)/len(l))
