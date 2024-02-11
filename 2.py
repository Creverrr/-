from random import randint
random_values_array=[] 
for i in range(9):
    random_values_array.append(randint(17, 31))
print(*random_values_array)
