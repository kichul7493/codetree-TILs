cnt3 = 0
cnt5 = 0

for i in range(10):
    n = int(input())

    if n % 3 is 0:
        cnt3 += 1
    if n % 5 is 0:
        cnt5 += 1

print(f"{cnt3} {cnt5}")