class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.desc = None
        self.finished = None
        self.total_pages = None
        self.total_chapters = None
        self.progress = None
        self.id = sum([ord(x) for x in "".join([title, author])])

    def update_book(self, arg, value):
        match(arg):
            case "title":
                self.title = value

class Bookcase:
    def __init__(self):
        self.books = {}

    def view_all_books(self):
        print("")
        for i in self.books:
            print(f"ID {i}: {self.books[i].title} - {self.books[i].author}\n")

    def add_new_to_bookcase(self, id, book):
        self.books[id] = book