n = int(input())

pr = [True]*(n+1)
for i in range(2, int(n**0.5)+1):
    if pr[i]:
        for j in range(i*i,n+1,i):
            pr[j]=False

for i in range(2,n+1):
    if pr[i]:
        print(i)