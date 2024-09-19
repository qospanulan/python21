
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        self.status = False

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Книга: {self.title} - Автор: {self.author}"

