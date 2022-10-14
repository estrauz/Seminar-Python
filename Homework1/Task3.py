# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

X = int(input('Enter the coordinate X of A: '))
Y = int(input('Enter the coordinate Y of A: '))

if (X == 0 and Y == 0):
    print('Incorrect coordinates. Try again')

elif (X == 0 and Y != 0):
        print(f'A ({X}; {Y}) - This point located in the coordinate axis OY')

elif (X != 0 and Y == 0):
        print(f'A ({X}; {Y}) - This point located in the coordinate axis OX')

elif X > 0 and Y > 0:
    print(f'A ({X}; {Y}) - This point located in the I quarter')

elif X < 0 and Y > 0:
    print(f'A ({X}; {Y}) - This point located in the II quarter')

elif X < 0 and Y < 0:
    print(f'A ({X}; {Y}) - This point located in the III quarter')

else:
    print(f'A ({X}; {Y}) - This point located in the IV quarter')


