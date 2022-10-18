#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел 
# от 1 до N.

number = int(input('Enter the number: '))

list = [1]
for a in range(2, number + 1):

    list.append(list[a - 2] * a)

print(f"The result is {list}")



