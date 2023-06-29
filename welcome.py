def display_menu():
    print("Welcome to the Menu")
    print("1. Delete all your Comments from a particular Subreddit.")
    print("2. Delete all your Posts from a particular Subreddit")
    print("3. Delete all your Comments before a particular Date")
    print("4. Delete all your Posts before a particular Date")
    print("5. Delete all your Comments after a particular Date")
    print("6. Delete all your Posts after a particular Date")
    print("7. Quit")


def get_user_choice():
    choice = input("Enter your choice (1-7): ")
    return choice
