n = int(input())

for i in range(1,n+1):
    deli = 0
    for j in range(1,i//2+1):
        if i%j==0:
            deli+=j
    if deli==i:
        print(i)
