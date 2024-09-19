
class User:

    def __init__(self, username):
        self.username = username
        self.user_books = []

    def take_book(self, book):
        book.set_status(False)
        self.user_books.append(book)

    def return_book(self, book):
        book.set_status(True)
        self.user_books.remove(book)


