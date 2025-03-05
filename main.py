import os

from authentication import *
from welcome import *
from delete import delete


# Only want this to be displayed once
print("Welcome to RedditRefresh")
display_comment_or_delete_menu()
# if delete_and_edit is true then we delete AND edit
# if delete_and_edit is false then we only edit
delete_and_edit = get_user_selected_mode()

while True:

    display_menu("Delete" if delete_and_edit else "Hash")
    user_choice = get_user_choice()

    if user_choice == "1":
        print(
            f'YOU SELECTD: "{"Delete" if delete_and_edit else "Hash"} all your Comments from a particular Subreddit."')
        delete(True, True, None, delete_and_edit)
        break
    elif user_choice == "2":
        print(
            f'YOU SELECTD: "{"Delete" if delete_and_edit else "Hash"} all your Posts from a particular Subreddit"')
        delete(True, False, None, delete_and_edit)
        break
    elif user_choice == "3":
        print(
            f'YOU SELECTD: "{"Delete" if delete_and_edit else "Hash"} all your Comments before a particular Date"')
        delete(False, True, True, delete_and_edit)
        break
    elif user_choice == "4":
        print(
            f'YOU SELECTD: "{"Delete" if delete_and_edit else "Hash"} all your Posts before a particular Date"')
        delete(False, False, True, delete_and_edit)
        break
    elif user_choice == "5":
        print(
            f'YOU SELECTD: "{"Delete" if delete_and_edit else "Hash"} all your Comments after a particular Date"')
        delete(False, True, False, delete_and_edit)
        break
    elif user_choice == "6":
        print(
            f'YOU SELECTD: "{"Delete" if delete_and_edit else "Hash"} all your Posts after a particular Date"')
        delete(False, False, False, delete_and_edit)
        break
    elif user_choice == "7":
        display_comment_or_delete_menu()
        delete_and_edit = get_user_selected_mode()
    elif user_choice == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Quitting the program...")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please try again.")
