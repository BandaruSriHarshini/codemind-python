string=input()
sum=0
for i in string:
    if ord(i)>=48 and ord(i)<=57:
        sum=sum+int(i)
print(""+str(sum))