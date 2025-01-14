from graphics import title_card, main_menu
from inputs import handle_user_input
from database import load_file, save_file, create_save_data

def main():
    title_card()

    bookcase = load_file()

    if len(bookcase) > 0:
        pass
    else:
        #print("\n Ah, a new user. Please answer the following questions for a better experience.")
        # users_name = input("\n What is your name? ")
        # location = input("\n Which country do you reside in? ")
        # favourite_author = input("\n Who is your favourite author? ")
        pass

    main_menu()
    handle_user_input(bookcase)

    json_file = create_save_data(bookcase)
    save_file(json_file)


if __name__ == "__main__":
    main()