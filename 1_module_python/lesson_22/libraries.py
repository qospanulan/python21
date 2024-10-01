
class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, new_book):
        # print(f"Type of new book: {type(new_book)}")
        new_book.set_status(True)
        self.books.append(new_book)

    def remove_book(self, book):
        book.set_status(False)
        self.books.remove(book)

    def get_books(self):
        return self.books

    def get_available_books(self):
        # available_books = list(filter(lambda book: book.get_status() is True, self.books))
        available_books = []

        for book in self.books:
            if book.get_status() is True:
                available_books.append(book)

        return available_books

    def get_books_by_name(self, book_title_to_search):
        result = []
        for book in self.books:
            if book.title == book_title_to_search:
                result.append(book)

        return result








