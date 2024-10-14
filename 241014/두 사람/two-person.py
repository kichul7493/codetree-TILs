personA = input().split()
personB = input().split()

ageA, genderA = int(personA[0]), personA[1]
ageB, genderB = int(personB[0]), personB[1]

if ageA >= 19 and genderA is "M":
    print(1)
elif ageB >= 19 and genderB is "M":
    print(1)
else:
    print(0)