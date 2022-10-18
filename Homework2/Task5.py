#Реализуйте алгоритм перемешивания списка.

import random

def mix_list(list):
    
    re_list = list[:]
    
    list_length = len(re_list)

    for i in range(list_length):
        
        j = random.randint(0, list_length - 1)
        
        temp = re_list[i]
        re_list[i] = re_list[j]
        re_list[j] = temp
    
    return re_list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mixed_list = mix_list(list)

print(f'The list is: {list}')
print(f'The mixed list is: {mixed_list}')
