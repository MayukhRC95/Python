str=input("Provide inout text: ")
pos=-1
i=0
for letter in str:
    if(letter=='m'):
        if(pos==-1):
            pos=i
        else:
            print(str[pos:i])
            pos=i
    i+=1
print(str[pos:])
