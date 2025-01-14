from graphics import title_card, main_menu
from inputs import handle_user_input

def main():
    title_card()

    # if user is new / no save file detected
    #print("\n Ah, a new user. Please answer the following questions for a better experience.")
    # users_name = input("\n What is your name? ")
    # location = input("\n Which country do you reside in? ")
    # favourite_author = input("\n Who is your favourite author? ")

    main_menu()
    handle_user_input()


if __name__ == "__main__":
    main()