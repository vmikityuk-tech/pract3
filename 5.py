n = int(input())
s = ''
i=1
while i**3<=n:
    s+= f'{i**3} '
    i+=1
print(s)