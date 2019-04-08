import re
f=open("fl.txt")
max=0
for line in f:
    line=line.rstrip()
    str=re.findall("^From: (\S+@\S+)",line)
    if str!=[]:
        print(str[0])
    l=re.findall("^X-DSPAM-Confidence: ([0-9.])",line)
    if l!=[] and float(l[0])>max:
        max=float(l[0])
print("Maximum D-SPAM value: ",max)
