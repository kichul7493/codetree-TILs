arr = input().split()

a, b = int(arr[0]), int(arr[1])

result = f"{a // b}."

i = 1

m = a % b

isEnd = False

while i < 21:

    if isEnd:
        result += "0"
        i += 1
        continue


    num = m * 10

    result += f"{num // b}"

    m = num % b
    if m is 0:
        isEnd = True

    i += 1

print(result)