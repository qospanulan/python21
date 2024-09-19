from books import Book
from users import User
from libraries import Library


library1 = Library(name="Library #1")

book1 = Book(title="Harry Potter", author="J.K. Роулинг", year=1997)
book2 = Book(title="The Blind Assasin", author="Margaret Atwood", year=2005)
book3 = Book(title="War and Peace", author="Leo Tolstoy", year=1869)
book4 = Book(title="1984", author="George Orwell", year=1949)
book5 = Book(title="One Hundred Years of Solitude", author="Gabriel", year=1967)

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)
library1.add_book(book5)


user1 = User(username="bookworm")
print("Добро пожаловать в библиотеку!")

main_menu = ("\nМеню:\n"
             "1. Доступные книги\n"
             "2. Взять книгу\n"
             "3. Мои книги\n"
             "q. Выход")


while True:

    print(main_menu)

    user_input = input("Ваш выбор: ")

    if user_input == "1":
        print("Вы выбрали показ доступных книг!")

        available_books = library1.get_available_books()

        for book in available_books:
            print(book)

    elif user_input == "2":
        print("Вы выбрали показ доступных книг!")

        available_books = library1.get_available_books()

        for book in available_books:
            print(book)

    elif user_input == 'q':
        break









