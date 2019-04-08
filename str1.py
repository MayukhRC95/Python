str="X-DSPAM-Confidential: 0.8475 "
pos=str.find(" ")
str1=str[pos+1:str.find(" ",pos+1)]
print(float(str1))
