from graphics import title_card, main_menu, display_messages
from inputs import handle_user_input
from database import load_file, save_file, create_save_data, create_backup

def main():
    title_card()

    display_messages("Checking for save file...")
    bookcase = load_file()

    if bookcase.get_length() < 1:
        display_messages("Ah, a new user. Please answer the following questions for a better experience.")
        users_name = input("\n What is your name? ")
        favourite_authors = input("\n List some of your favourite authors (use a comma): ")
        json_file = create_save_data([users_name, favourite_authors], "personal")
        save_file(json_file, "personal")
    
    running = True

    while running:
        main_menu()
        running = handle_user_input(bookcase)
        
        json_file = create_save_data(bookcase, "bookcase")
        save_file(json_file, "bookcase")
        create_backup()

if __name__ == "__main__":
    main()