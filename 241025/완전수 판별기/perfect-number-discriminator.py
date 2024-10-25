n = int(input())
sum = 0

for i in range(1, n):
    if n % i is 0:
        sum += i

if n is sum:
    print("P")
else:
    print("N")