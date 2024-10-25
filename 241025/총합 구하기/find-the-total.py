arr = input().split()
sum = 0

a, b = int(arr[0]), int(arr[1])

for i in range(a, b+1):
    if i % 6 is 0 and i % 8 is not 0:
        sum += i


print(sum)