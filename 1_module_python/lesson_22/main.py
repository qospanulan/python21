from books import Book
from users import User
from libraries import Library


library1 = Library(name="Library #1")

book1 = Book(title="Book 1", author="Author 1", year=1999)
book2 = Book(title="Book 2", author="Author 2", year=2017)

library1.add_book(book1)
library1.add_book(book2)

all_books = library1.get_books()

print("all books:")
for book in all_books:
    print(book)

print("\n================================")


user1 = User(username="book_worm")

user1.take_book(book1)

# all_books = library1.get_books()
all_books = library1.get_available_books()

print("left books:")
for book in all_books:
    print(book)

