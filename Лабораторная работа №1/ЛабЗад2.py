# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44  # Объем кассеты в Мб
pages_number = 100  # Количество страниц в книге
string_number = 50  # Число строк на одной странице
symbol_number = 25  # Количество символов в одной строке
amount_for_storage = 4  # Количество байт нужное для хранения одного символа

symbols_inbook = symbol_number * string_number * pages_number  # Количество символов во всей книге
volume_book = amount_for_storage * symbols_inbook / (1024 ** 2)  # Объем книги в Мб
count = volume / volume_book  # Количество книг, которое поместиться на дискету. в вещественном виде
count_round = round(count)  # Округление значения для получения количество книг в штуках

print("Количество книг, помещающихся на дискету:", count_round)
