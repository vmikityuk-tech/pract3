temp = float(input())
s = [temp]
c = 0
while temp!=0:
    temp = float(input())
    s+=[temp]
    if (s[-2]-s[-1]>0) and s[-1]!=0:
        c+=1
print(c)