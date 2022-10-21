# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

N = int(input('Enter the number of quantity elements: '))

list = []

for i in range(N):
    list.append(randint(0, 10))

print(list)

result = 0
    
for i in range(N):
        if (i % 2 !=0):
            result += list[i]
                        
print(f'The sum of odd elements of the list is {result}')



