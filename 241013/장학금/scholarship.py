arr = input().split()

m = int(arr[0])
f = int(arr[1])

if m < 90:
    print(0)
elif f >= 95:
    print(100000)
elif f >= 90:
    print(50000)