# TODO Напишите функцию для поиска индекса товара
def find_goods_index(list_of_items, needed_items):  #Создаем функцию, которая принимает список товаров и определенный товар
    if needed_items in list_of_items:  #Проверяем есть ли нужный товар в списке
        return list_of_items.index(needed_items)  #Если да, то возвращаем его индекс
    else:
        return None  #Если нет, то возвращаем "None"

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_goods_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
