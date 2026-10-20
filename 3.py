from math import *

while True:
    a = int(input())
    r = int(sqrt(a))
    if r*r==a:
        print('число - полный квадрат')
        break
    else:
        print('не полный квадрат')


