arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if (a >= b and a <=c) or (a >= c and a <= b):
    print(a)
elif (b >= a and b <=c) or (b >= c and b <= a):
    print(b)
else:
    print(c)