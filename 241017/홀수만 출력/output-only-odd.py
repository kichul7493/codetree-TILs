arr = input().split()

a, b = int(arr[0]), int(arr[1])

for i in range(a, b + 1):
    if i % 2 is 1:
        print(i, end=" ")