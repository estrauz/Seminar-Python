#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input('Enter the number: '))

result = 0

for i in range(1, number + 1):
    
    list = (1 + 1 / i) ** i 
    result += list


print(f'The sum of that elements is {round(result,2)}')