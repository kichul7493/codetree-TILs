arr = input().split()
m = 1

a, b = int(arr[0]), int(arr[1])

for i in range(a, b+1):
    m *= i

print(m)