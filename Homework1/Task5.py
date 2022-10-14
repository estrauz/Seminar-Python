#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

X1 = float(input('Enter the coordinate X of A: '))
Y1 = float(input('Enter the coordinate Y of A: '))
X2 = float(input('Enter the coordinate X of C: '))
Y2 = float(input('Enter the coordinate Y of C: '))

length = round(((X2 - X1)**2 + (Y2 - Y1)**2)**(0.5), 2)
print(f'The lenght of point A and C is a {length}')

