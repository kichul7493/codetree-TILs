n = int(input())

cnt = 0
sum = 0

for i in range(n):
    num = int(input())
    cnt += 1
    sum += num


print(f"{sum} {(sum/cnt):.1f}")