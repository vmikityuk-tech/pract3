c = 0
s = ''
for x in range(10**2,10**3):
    if x%17==0:
        c+=1
        s += f'{x} '
print(s)
print(c)