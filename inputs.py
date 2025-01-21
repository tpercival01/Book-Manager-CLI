from book import search_book, update_a_book
from graphics import display_messages

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def handle_user_input(bookcase):
    user_input = int(input("\nEnter your input here (number): "))
    match(user_input):
        case 1:
            bookcase.view_all_books()
            return True
        case 2:
            temp = f"{RED}Adding a new book.{RESET} Please fill out the following details: "
            display_messages(temp)
            title = input(f"{RED}Enter the title of the book{RESET}: ")
            author = input(f"\n{RED}Enter the author of the book{RESET}: ")
            
            temp = f"{RED}Added book{RESET}: {title} by {author} to your library!"
            display_messages(temp)

            book = search_book(title, author)
            bookcase.add_new_to_bookcase(book)
            return True
        case 3:
            pass
        case 4:
            display_messages([f"{RED}Updating a book.{RESET}",f"{RED}Enter the details you wish to update (if no update, just press enter):{RESET}"])
            book_title = input(f"{RED}Please enter the title for the book you wish to update: {RESET}")
            book_updates = {}
            parameters = ["title", "author", "rating", "comments", "finished", "total pages", "total chapters", "current page", "current chapter", "status"]
            for i in parameters:
                temp = input(f"{RED}Enter the new value for the{RESET} {GREEN}{i}{RESET}: ")
                book_updates[i] = temp if len(temp) > 0 else None
            
            update_a_book(bookcase, book_updates, book_title)
            return False
        case 5:
            return False