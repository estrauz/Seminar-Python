# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

N = int(input('Enter the number of quantity elements: '))

list = []

for i in range(N):
    list.append(randint(0, 20))

print(list)

result = 0


if (N % 2 == 0):
    for i in range(N):
        if (i < N):
            result = list[i] * list[N - 1]
            print(result)
            
            result = 0
            N-=1

elif (N % 2 != 0):
    for i in range(N):
        if (i <= N):
            result = list[i] * list[N - 1]
            print(result)
        
            result = 0
            N-=1



    

