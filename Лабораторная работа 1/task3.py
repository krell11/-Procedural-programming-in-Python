list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
mid_idx = len(list_players) // 2
print(list_players[:mid_idx])
print(list_players[mid_idx::])
