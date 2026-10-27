n = int(input())
c=0
for i in range(0,n+1):
    c+=i*2
for j in range(0,n//2+2):
    for k in range(j+1,n+1):
        c+=j
        c+=k
print(c)