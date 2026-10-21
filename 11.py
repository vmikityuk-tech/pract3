score = int(input())
res = score
while score!=-1:
    score = int(input())
    if score!=-1 and score>res:
        res = score
print(res)
