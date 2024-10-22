n = int(input())

for i in range(1, n+1):
    num_char = str(i)
    if i % 3 is 0 or "3" in num_char or "6" in num_char or "9" in num_char:
        print(0, end=" ")
    else:
        print(i, end=" ")