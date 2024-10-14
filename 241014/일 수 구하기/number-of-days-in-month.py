n = int(input())

if n % 2 is 0:
    if n is 2:
        print(28)
    elif n is 8 or n is 10:
        print(31)
    else:
        print(30)

else:
    if n is 9 or n is 11:
        print(30)
    else:
        print(31)