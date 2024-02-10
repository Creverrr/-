from random import randint
random_values_array=[] # по факту для цієї задачі непотрібний масив, тому що можна просто вивести рандомні числа та не тратити пам'ять + час виконання
for i in range(9):
    random_values_array.append(randint(17, 31))
print(*random_values_array)