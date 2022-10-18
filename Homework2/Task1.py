
number = input('Enter the number: ')
result = 0


for i in str(number):

    if i != '.':
        
        result = result + int(i)

print(result)

