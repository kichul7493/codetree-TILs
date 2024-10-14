y = int(input())

if y % 4 is not 0 or (y % 100 is 0 and y % 400 is not 0):
    print('false')
else:
    print('true')