class LibraryBook:

    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


b1 = LibraryBook("Python Basics", "Ravi", 500)
b2 = LibraryBook("Data Science", "Aman", 700)
b3 = LibraryBook("AI Fundamentals", "Rishabh", 900)

b1.display_book_info()
b2.display_book_info()
b3.display_book_info()
