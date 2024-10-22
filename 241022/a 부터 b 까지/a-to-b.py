arr = input().split()

a, b = int(arr[0]), int(arr[1])

print(a, end=" ")

while a < b:
    if a % 2 is 0:
        a += 3
    else:
        a *= 2
    print(a, end=" ")