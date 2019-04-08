import urllib.request, urllib.parse, urllib.error
f=urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in f:
    print(line.decode().strip())
