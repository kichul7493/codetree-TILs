arrA = input().split()
arrB = input().split()

aMath = int(arrA[0])
aEng = int(arrA[1])

bMath = int(arrB[0])
bEng = int(arrB[1])

if aMath > bMath:
    print("A")
elif aMath < bMath:
    print("B")
else:
    if aEng > bEng:
        print("A")
    else:
        print("B")