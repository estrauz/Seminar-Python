import random as rand

K = int(input('Enter a k-measure: '))


list = []

for i in range(1, K+1):
    
    coordinate = rand.randint(0, 50)
    free_part = rand.randint(0, 101)
    full_poly = ""
    
    if K == 0:
        print("This it not a polynomial")

    else:
        if K == 1:
            polynomial = f"{coordinate}X + {free_part}"
        else:
            polynomial = f"{coordinate}X^{K} + "
            
    K -= 1   
    index = polynomial.find('+ ')
    full_poly += polynomial
    print(full_poly)

print(f"{full_poly} = 0")
        
with open('file.txt', 'w') as data:
    data.writelines(f'The elements are {full_poly}\n')
    
    

    







