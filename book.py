import requests
from graphics import display_messages

class Book:
    def __init__(self, title, author, rating = None, comments = None, finished = None, total_pages = None, total_chapters = None, progress = None, status = None):
        self.title = title
        self.author = author
        self.rating = rating
        self.comments = comments
        self.finished = finished
        self.total_pages = total_pages
        self.total_chapters = total_chapters
        self.progress = progress
        self.status = status
        self.id = sum([ord(x) for x in "".join([title, author])])

    def update_book(self, arg, value):
        match(arg):
            case "title":
                self.title = value

    def get_book(self):
        temp = {
                "title": self.title,
                "author": self.author,
                "progress": self.progress,
                "status": self.status,
                "total_chapters": self.total_chapters,
                "total_pages": self.total_pages,
                "rating": self.rating,
                "comments": self.comments
        }
        return temp

class Bookcase:
    def __init__(self):
        self.books = {}

    def view_all_books(self):
        if self.get_length() > 0:
            line1 = "Viewing all books currently in your library: "
            temp = []
            for i in self.books:
                line2 = f"ID {i}: {self.books[i].title} - {self.books[i].author}\n"
                temp.append(line2)
            display_messages(line1, temp)
        else:
            line1 = "You currently have no books in your library."
            line2 = f"Choose option 2 at the main menu to add a book."
            display_messages([line1, line2])

    def add_new_to_bookcase(self, book):
        self.books[book.id] = book
    
    def get_length(self):
        return len(self.books)

    def bulk_add_books(self, books):
        self.books = books

def search_book(title, author):
    # url = "https://www.googleapis.com/books/v1/volumes?q="
    # title = title.replace(" ", "+").lower()
    # author = author.replace(" ", "+").lower()
    # query = f'"{title}"+"{author}"'
    # res = requests.get(url+query)
    # book_data = res.json()
    # clean_book = clean_book_search(book_data)
    book = Book(title, author)
    return book

def clean_book_search(book):
    print(book["items"][0]["volumeInfo"])