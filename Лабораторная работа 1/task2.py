# TODO Найдите количество книг, которое можно разместить на дискете
pages, strings, symbols = 100, 50, 25
bytes_in_book = pages * strings * symbols * 4
all_memory = 1.44 * 1024 ** 2
count_books = int(all_memory // bytes_in_book)
print("Количество книг, помещающихся на дискету:", count_books)
