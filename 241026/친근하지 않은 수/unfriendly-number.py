cnt = 0

n = int(input())

for i in range(1, n+1):
    if i % 2 is 0 or i % 3 is 0 or i % 5 is 0:
        continue
    
    cnt += 1

print(cnt)