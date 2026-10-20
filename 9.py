from math import *
n, k, r = map(int, input().split())
st = r/n
bs = 1+(k/100)
res = ceil(log(st,bs))+1
print(res)
