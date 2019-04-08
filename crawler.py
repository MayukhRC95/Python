import urllib.request, urllib.parse, urllib.error
import re
lis=list()
f=urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in f:
    str=line.decode().strip()
    pages=re.findall("href=(\S*)>",str)
    if pages !=[]:
        lis.append(pages[0])
print(lis)
c=0
for page in lis:
    print("Displaying page:",lis[c])
    webpage=lis[c]
    webpage=webpage[1:len(webpage)]
    print(type(webpage))
    fh=urllib.request.urlopen(webpage)
    for l in fh:
        print(l.decode().strip())
    c+=1
