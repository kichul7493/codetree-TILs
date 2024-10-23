classCnt = 0
hallwayCnt = 0
restroomCnt = 0

n = int(input())

for i in range(1, n+1):
    if i % 12 is 0:
        restroomCnt += 1
    elif i % 3 is 0:
        hallwayCnt += 1
    elif i % 2 is 0:
        classCnt += 1

print(f"{classCnt} {hallwayCnt} {restroomCnt}")