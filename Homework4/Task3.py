#Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list = []

for i in range(10):
    list.append(randint(0, 5))

list1 = []

for i in list:
    if i not in list1:
        list1.append(i)
    
print(list)
print(list1)