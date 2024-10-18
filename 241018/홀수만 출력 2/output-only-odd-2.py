arr = input().split()

b, a = int(arr[0]), int(arr[1])

for i in range(b, a -1, -1):
    if i % 2 is 1:
        print(i, end=" ")