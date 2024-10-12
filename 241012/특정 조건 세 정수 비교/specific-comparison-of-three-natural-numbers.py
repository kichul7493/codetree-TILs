arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a < b and a < c:
    print(1, end=" ")
else:
    print(0, end=" ")


if a is b and a is c:
    print(1, end=" ")
else:
    print(0, end=" ")