arr = input().split()

a, n = int(arr[0]), int(arr[1])

c = n

while c > 0:
    a += n
    c -= 1
    print(a)