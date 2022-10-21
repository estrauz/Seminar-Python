# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
#- 3 -> 11
# - 2 -> 10

N = int(input('Enter the number : '))

list = []

while N > 0:
    list.append(N % 2)
    N = N // 2

print(list)



print(list)
