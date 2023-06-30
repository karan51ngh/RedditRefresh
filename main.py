import os

from authentication import *
from welcome import *
from delete import delete

while True:
    display_menu()
    user_choice = get_user_choice()

    if user_choice == "1":
        print('YOU SELECTD: "Delete all your Comments from a particular Subreddit."')
        delete(True, True, None)
        break
    elif user_choice == "2":
        print('YOU SELECTD: "Delete all your Posts from a particular Subreddit"')
        delete(True, False, None)
        break
    elif user_choice == "3":
        print('YOU SELECTD: "Delete all your Comments before a particular Date"')
        delete(False, True, True)
        break
    elif user_choice == "4":
        print('YOU SELECTD: "Delete all your Posts before a particular Date"')
        delete(False, False, True)
        break
    elif user_choice == "5":
        print('YOU SELECTD: "Delete all your Comments after a particular Date"')
        delete(False, True, False)
        break
    elif user_choice == "6":
        print('YOU SELECTD: "Delete all your Posts after a particular Date"')
        delete(False, False, False)
        break
    elif user_choice == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Quitting the program...")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please try again.")
