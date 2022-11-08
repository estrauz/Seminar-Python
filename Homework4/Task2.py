# Задайте натуральное число N. Напишите программу, которая составит список простых множителей 
# числа N.

N = int(input('Enter a number: '))

list = []

for i in range(2, N):

    while (N % i == 0):
        N /= i

        if (i not in list):   
            list.append(i)    
   
print(list)    


