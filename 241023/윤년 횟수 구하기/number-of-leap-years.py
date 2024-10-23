cnt = 0

n = int(input())

for i in range(1, n+1):
    if i % 4 is 0:
        if i % 100 is 0 and i % 400 is not 0:
            cnt += 0
        else:
            cnt += 1 
print(cnt)