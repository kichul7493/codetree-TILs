m = int(input())

if m <= 2 or m >= 12:
    print("Winter")
elif m >= 9 and m <= 11:
    print("Fall")
elif m >= 6 and m <= 8:
    print("Summer")
else:
    print("Spring")