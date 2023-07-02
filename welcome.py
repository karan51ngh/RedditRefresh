def display_comment_or_delete_menu():
    print("Select a mode")
    print("1. DELETE (this option will first ENCRYPT your content and then DELETE)")
    print("2. ENCRYPT (this option will only ENCRYPT your content)")


def get_user_selected_mode():
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        return True
    elif choice == "2":
        return False
    print(f"The value {choice} is not in range (1-2). Defaulting to ENCRYPT.")
    return False


def display_menu(option):
    print("Welcome to the Menu")
    print(f"1. {option} all your Comments from a particular Subreddit.")
    print(f"2. {option} all your Posts from a particular Subreddit")
    print(f"3. {option} all your Comments before a particular Date")
    print(f"4. {option} all your Posts before a particular Date")
    print(f"5. {option} all your Comments after a particular Date")
    print(f"6. {option} all your Posts after a particular Date")
    print(
        f"7. Change to {'Delete' if option == 'Encrypt' else 'Encrypt'} mode")
    print("8. Quit")

def get_user_choice():
    choice = input("Enter your choice (1-8): ")
    return choice
