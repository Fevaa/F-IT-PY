users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict = {
        "Общее количество": 0,
        "Уникальные посещения": 0
        }
num = len(users)
un = set(users)
num_2 = len(un)
dict["Общее количество"] = num
dict["Уникальные посещения"] = num_2
print(dict)


# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
