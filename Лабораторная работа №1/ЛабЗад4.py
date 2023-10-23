users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count_users = len(users)  # Подсчитываем количество всех посещений
unique_users = set(users)  # Определяем уникальные посещения
count_unique = len(unique_users)  # Подсчитываем количество уникальных посещений
dictionary["Общее количество"] = count_users  # Задаем новое значение по ключу
dictionary["Уникальные посещения"] = count_unique  # Задаем новое значение по ключу
print(dictionary)
