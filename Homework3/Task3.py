# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint

N = int(input('Enter the number of quantity elements: '))

list = []

for i in range(N):
    list.append(randint(0, 20))

print(list)

max = list[0]
min = list[0]

for i in range(N):
    if list[i] > max:
        max = list[i]
    else:
        if list[i] < min:
            min = list[i]

print(f'Min of the list is {min}, max of the one is {max}')
print(f'The different is {max-min}')