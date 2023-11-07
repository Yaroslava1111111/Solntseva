# TODO Напишите функцию find_common_participants
def find_common_participants(first_string, second_string, separator=","):  #Создаем функцию, которая принимает две строки и разделитель (необязательный аргумент)
    first_string_splited = first_string.split(separator)  #Разделяем первую строку по значению сепаратора, то есть переменной separator
    second_string_splited = second_string.split(separator)  #Разделяем вторую строку по значению сепаратора, то есть переменной separator
    common = set(first_string_splited).intersection(set(second_string_splited))  #Находим пересечения элементов множеств
    list_common = list(common)  #Преобразуем множество в лист для последующей сортировки
    list_common.sort()  #Сортируем лист по умолчанию, то есть по алфавиту
    return list_common  #Задаем результат функции: возврат отсортированного списка


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator="|"))
