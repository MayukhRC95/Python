cont=1
num=0
false=0
while cont==1 :
    str=input("Enter a number: ")
    try:
        num=int(str)
    except:
        false=1
    if num>0 and false==0:
        print("Number entered is:",num)
    elif false==1:
        print("not a number")
    cont=int(input("do you want to continue: "))
    false=0
print("Program done")
