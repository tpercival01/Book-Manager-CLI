from graphics import title_card, main_menu, display_messages
from inputs import handle_user_input
from database import load_file, save_file, create_save_data

def main():
    title_card()

    display_messages("Checking for save file...")
    bookcase = load_file()

    if bookcase.get_length() < 1:
        #print("\n Ah, a new user. Please answer the following questions for a better experience.")
        # users_name = input("\n What is your name? ")
        # location = input("\n Which country do you reside in? ")
        # favourite_author = input("\n Who is your favourite author? ")
        pass
    
    running = True

    while running:
        main_menu()
        running = handle_user_input(bookcase)
        
        json_file = create_save_data(bookcase)
        save_file(json_file)

if __name__ == "__main__":
    main()