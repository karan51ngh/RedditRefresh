import datetime

def display_mode_menu():
    print("Select a MODE")
    print("1. DELETE (this option will first HASH your content and then DELETE)")
    print("2. HASH (this option will only HASH your content)")
    print("3. ENCRYPT ((this option will first ENCRYPT your content. You can DECRYPT your content in the future.)")
    print("4. DECRYPT ((this option will first DECRYPT your ENCRPTED content.)\n")
    choice = get_user_selection(1,4)
    if choice == 1:
        return "DELETE"
    elif choice == 2:
        return "HASH"
    elif choice == 3:
        return "ENCRYPT"
    else:
        return "DECRYPT"

def diplay_content_menu():
    print("Select the type of CONTENT you want to deal with from your Reddit account:")
    print("1. Your Reddit COMMENTs")
    print("2. Your Reddit POSTs\n")
    choice = get_user_selection(1,2)
    return "COMMENT" if choice == 1 else "POST"

def diplay_criteria_options():
    print("Select the CRITERIA on the basis of which you want to deal with the CONTENT:")
    print("1. Based on a particular SUBREDDIT.")
    print("2. Based on DATE the CONTENT was posted.\n")
    choice = get_user_selection(1,2)
    return "SUBREDDIT" if choice == 1 else "DATE"

def askForDate():
    try:
        date_input = input("Please enter a date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        print("\n")
        return date
    except ValueError:
        print("Invalid date format. Please try again.\n")
        return askForDate()

def askBeforeAfter(date):
    print(f"Select whether you want to execute the script BEFORE or AFTER {date}:")
    print("1. BEFORE.")
    print("2. AFTER.\n")
    choice = get_user_selection(1,2)
    return "BEFORE" if choice == 1 else "AFTER"


def askForSubReddit():
    subreddit_name = input("Enter Subbredit Name: ")
    print(f"You chose the SubReddit as'{subreddit_name}'. Do you want to proceed with this SubReddit?")
    print("1. Yes.")
    print("2. No. I want to re-enter the SubReddit name.\n")
    confirmation = get_user_selection(1,2)
    print("\n")
    return subreddit_name if confirmation == 1 else askForSubReddit()

def askForConfirmation(user_mode):
    print(f"Please review the options selectd by you. do you want to proceed?")
    if (user_mode == "DELETE" or user_mode == "HASH"):
        print(f"NOTE: You chose the MODE as {user_mode}, these changes are IRREVERSIBLE changes.")
    print("1. Yes. I understand.")
    print("2. No. I want to exit.\n")
    return get_user_selection(1,2)
    
def get_user_selection(lower, upper):
    choice = int(input(f"Enter your choice ({lower}-{upper}): "))
    print('')
    if choice >= lower and choice <=upper:
        return choice
    else:
        print("Invalid Selection. Select Again.\n")
        return get_user_selection(lower, upper)

