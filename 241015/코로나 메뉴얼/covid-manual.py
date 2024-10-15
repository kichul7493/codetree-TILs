arrA = input().split()
arrB = input().split()
arrC = input().split()

aSymptoms = arrA[0]
bSymptoms = arrB[0]
cSymptoms = arrC[0]

aTemp = int(arrA[1])
bTemp = int(arrB[1])
cTemp = int(arrC[1])

count = 0;

if aSymptoms is "Y" and aTemp >= 37:
    count += 1;

if bSymptoms is "Y" and bTemp >= 37:
    count += 1;

if cSymptoms is "Y" and cTemp >= 37:
    count += 1;


if count >= 2:
    print("E")
else:
    print("N")