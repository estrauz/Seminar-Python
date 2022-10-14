# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.

date = int(input('Enter a date: '))

if (1 <= date <= 5):
    print(f'{date} - this is a business day')

elif (6 <= date <= 7):
    print(f'{date} - this is weekends')
    
else:
    print(f'{date} - this is the incorrect number')



