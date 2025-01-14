class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.rating = None
        self.comments = None
        self.finished = None
        self.total_pages = None
        self.total_chapters = None
        self.progress = {
            "current_page": 0,
            "current_chapter": 0
        }
        self.status = None
        self.id = sum([ord(x) for x in "".join([title, author])])

    def update_book(self, arg, value):
        match(arg):
            case "title":
                self.title = value

    def get_book(self):
        temp = {
            self.id: {
                "title": self.title,
                "author": self.author,
                "progress": self.progress,
                "status": self.status,
                "total_chapters": self.total_chapters,
                "total_pages": self.total_pages,
                "rating": self.rating,
                "comments": self.comments
            }
        }
        return temp

class Bookcase:
    def __init__(self):
        self.books = {}

    def view_all_books(self):
        print("")
        for i in self.books:
            print(f"ID {i}: {self.books[i].title} - {self.books[i].author}\n")

    def add_new_to_bookcase(self, id, book):
        self.books[id] = book

def search_book(title, author):
    url = "https://openlibrary.org/search.json?"
    title = title.replace(" ", "+").lower()
    author = author.replace(" ", "+").lower()
    print(title)
    print(author)
    query = f"q={title}&author={author}"