arr = input().split()

b, a = int(arr[0]), int(arr[1])

while a <= b:
    if b % 2 is 0:
        print(b, end=" ")
    
    b -= 1