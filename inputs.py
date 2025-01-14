from book import view_all_books, create_book

def handle_user_input():
    user_input = int(input("\n Enter your input here (number): "))
    
    match(user_input):
        case 1:
            view_all_books()
        case 2:
            create_book()