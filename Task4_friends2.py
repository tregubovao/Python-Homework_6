# 3. Еще немного о друзьях. Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) 
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

n = int(input('Введите количество друзей: \n'))
friends = []
name_list = []
age_list = []
for _ in range(n):
    new_dict = {}
    name = input('Введите имя друга: \n')
    name_list.append(name)
    age = int(input(f'Введите возраст друга: \n'))
    age_list.append(age) 
    new_dict[name] = age
    friends.append(new_dict)
summ_age = 0
for el in age_list:
    summ_age += el
print(f'Средний возраст ребят {summ_age/len(age_list)}')

maxx_len_name = name_list[0]
for i in range(len(name_list) - 1):
    if len(name_list[i + 1]) > len(name_list[i]):
        maxx_len_name = name_list[i + 1]
print(maxx_len_name)  
