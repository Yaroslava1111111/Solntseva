list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)  # Определяем количество людей в списке
center = count // 2  # Находим индекс первого игрока второй команды

first_team = list_players[:center]   # Формируем первую команду до найденного индекса
second_team = list_players[center:]  # Формируем вторую команду, начиная с найденного индекса

print(first_team)
print(second_team)
