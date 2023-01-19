# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

from random import randint
new_list = [randint(1,10) for i in range(int(input('Введите количество элементов списка: \n')))]
print(new_list)
new_set = set(new_list)
print(new_set)
print(f'Количество различных элементов в заданном списке: {len(new_set)}')