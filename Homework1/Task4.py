

quarter = int(input('Enter a quarter: '))

if (quarter > 4 or quarter < 1):
    print('Incorrect number. Try again')

elif quarter == 1:
    print('The coordinates might be x > 0, y > 0')

elif quarter == 2:
    print('The coordinates might be x < 0, y > 0')

elif quarter == 3:
    print('The coordinates might be x < 0, y < 0')

else:
    print('The coordinates might be x > 0, y < 0')


