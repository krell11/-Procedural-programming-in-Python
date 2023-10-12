# TODO Напишите функцию find_common_participants
def find_common_participants(str1: str, str2: str, spacer: str = ','):
    set_stud1 = set(str1.split(spacer))
    set_stud2 = set(str2.split(spacer))
    unique = sorted(list(set_stud1.intersection(set_stud2)))
    return unique


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
res = find_common_participants(participants_first_group, participants_second_group, spacer='|')
