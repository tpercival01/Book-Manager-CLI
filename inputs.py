from book import search_book

def handle_user_input(bookcase):
    user_input = int(input("\n Enter your input here (number): "))
    
    match(user_input):
        case 1:
            bookcase.view_all_books()
        case 2:
            print("\n Adding a new book. Please fill out the following details: ")
            title = input("\n Enter the title of the book: ")
            author = input("\n Enter the author of the book: ")
            book = search_book(title, author)
            #bookcase.add_new_to_bookcase()