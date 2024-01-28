BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:

    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id}, name={self.name!r}, pages={self.pages})'
# TODO написать класс Book
class Library:
    def __init__(self, books=None):
        self.books = books

    def get_next_book_id(self):
    # Метод, возвращающий идентификатор для добавления новой книги в библиотеку
        if self.books is None:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
    # Метод, возвращающий индекс книги в списке
        books_list = [abook.id for abook in self.books]
        if book_id in books_list:
            return books_list.index(book_id)
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

# TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
