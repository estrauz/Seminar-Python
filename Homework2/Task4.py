#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Enter the number: '))

multiplication = 1

array = list(range(-N, N+1))

for i in range(-N, N+1):
    
    if (i != 0):
        multiplication = multiplication*i

print(array)
print(multiplication)

with open('file.txt', 'w') as data:
    data.writelines(f'The elements are {array}\n')
    data.writelines(f'The multiplication is {multiplication}')
