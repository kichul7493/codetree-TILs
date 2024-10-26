arr = input().split()

a, b = int(arr[0]), int(arr[1])

m = 1

for i in range(1, b +1):
    if i % a is 0:
        m *= i

print(m)