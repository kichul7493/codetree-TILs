arr = input().split()

a = int(arr[0])
b = int(arr[1])

def printEvenOrOdd(n):
    if n % 2 is 0:
        print("even")
    else:
        print("odd")

printEvenOrOdd(a)
printEvenOrOdd(b)