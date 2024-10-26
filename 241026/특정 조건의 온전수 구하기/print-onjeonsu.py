n = int(input())

for i in range(1, n + 1):
    if i % 2 is 0 or i % 5 is 0 or (i % 3 is 0 and i % 9 is not 0):
        continue
    
    print(i, end=" ")