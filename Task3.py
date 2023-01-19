# Старший и младший. Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

n = int(input('Введите количество друзей: \n'))
friends = []
for _ in range(n):
    new_dict = {}
    name = input('Введите имя друга: \n')
    age = int(input(f'Введите возраст друга: \n'))   
    new_dict[name] = age
    friends.append(new_dict)
i = 0
age_list = []
while i < len(friends):
    for value in friends[i]:
        age_list.append(friends[i][value])        
    i += 1
for key in friends[age_list.index(min(age_list))]:
    print(key)

