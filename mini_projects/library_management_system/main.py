class Library:
    def __init__(self, books):
        self.no_books = len(books)
        self.books = books
        
    def show_books(self):
        print("Showing books:")
        for book in self.books:
            print(book)

    def add_book(self, book_name):
        print("Adding book")
        self.books.append(book_name)
        self.no_books = len(self.books)

    def get_no(self):
        return self.no_books


# Creating library object
my_library = Library(["python", "oops"])

# Printing books
my_library.show_books()

# Adding a book
my_library.add_book("dsa")

# Printing books
my_library.show_books()

# Getting number of books
print("Number of books:", my_library.get_no())
