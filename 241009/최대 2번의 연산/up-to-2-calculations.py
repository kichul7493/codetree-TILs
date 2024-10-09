a = int(input())

if a % 2 is 0:
    a = a // 2

if a % 2 is 1:
    a = (a + 1) // 2

print(a)