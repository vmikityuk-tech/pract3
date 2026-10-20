a = input()
b = ''
for i in range(len(a)):
    if (i+1)%3==0:
        b+=a[i]
print(b)