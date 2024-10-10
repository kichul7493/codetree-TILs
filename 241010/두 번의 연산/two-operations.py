a = int(input())

if a % 2 is 1:
    a += 3

if a % 3 is 0:
    a = a // 3

print(a)