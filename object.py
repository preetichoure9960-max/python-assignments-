class Library:
    
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f"{self.book_name} has been issued.")
        else:
            print(f"{self.book_name} is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.book_name} has been returned.")
        else:
            print(f"{self.book_name} was already available.")

    def display(self):
        status = "Available" if self.available else "Issued"
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)
        print("---------------------")

book1 = Library("Python Basics", "ABC Author")
book2 = Library("Data Structures", "XYZ Author", False)
book1.display()
book2.display()
book1.check_out()
book1.display()
book2.return_book()
book2.display()