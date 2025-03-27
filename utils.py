import datetime

def display_mode_menu():
    print("Select a MODE")
    print("1. DELETE (this option will first HASH your content and then DELETE it. This is Irreversible.)")
    print("2. HASH (this option will only HASH your content. This is Irreversible.)")
    print("3. ENCRYPT (this option will ENCRYPT your content. You can DECRYPT your content in the future.)")
    print("4. DECRYPT (this option will DECRYPT your ENCRPTED content.)\n")

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

def askFromDate():
    try:
        date_input = input("Please enter 'From Date'.\n(Leave this Empty if you want the 'From Date' to be indefinite.) (YYYY-MM-DD): ")
        if date_input == '':
            print('')
            return datetime.datetime.strptime("1986-11-08", "%Y-%m-%d")
        fromDate = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        print('')
        return fromDate

    except ValueError:
        print("Invalid date format. Please try again.\n")
        return askFromDate()

def askToDate(fromDate):
    try:
        date_input = input("Please enter 'To Date'.\n(Leave this Empty if you want the 'To Date' to be indefinite.) (YYYY-MM-DD): ")

        if date_input == '':
            today = datetime.date.today()
            print('')
            return datetime.datetime.strptime(str(today + datetime.timedelta(days=1)), "%Y-%m-%d")

        toDate = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        if toDate < fromDate:
             print("'To date' should be on or after the entered 'From Date'. Please try again.\n")
             return askToDate(fromDate)
        print('')
        return toDate

    except ValueError:
        print("Invalid date format. Please try again.\n")
        return askToDate(fromDate)

def askForSubReddit():
    subreddit_name = input("Enter Subbredit Name.\n(Leave this Empty if you don't want it to be a criteria.): ")
    if subreddit_name != '':
        print(f"You chose the SubReddit as'{subreddit_name}'. Do you want to proceed with this SubReddit?")
    else:
        print(f"You chose N0 SubReddit. Do you want to proceed with this choice?")

    print("1. Yes.")
    print("2. No. I want to re-enter the SubReddit name.\n")

    confirmation = get_user_selection(1,2)
    print('')
    return subreddit_name if confirmation == 1 else askForSubReddit()

def askForConfirmation(user_mode):
    print(f"Please review the options selectd by you. do you want to proceed?")

    if (user_mode == "DELETE" or user_mode == "HASH"):
        print(f"\n**NOTE**: You chose the MODE as {user_mode}, these changes are IRREVERSIBLE changes.\n")
    print("1. Yes. I understand.")
    print("2. No. I want to exit.\n")
    return get_user_selection(1,2)
    
def get_user_selection(lower, upper):
    choice = input(f"Enter your choice ({lower}-{upper}): ")

    if choice == '':
        print("Invalid Selection. Select Again.\n")
        return get_user_selection(lower, upper)

    choice = int(choice)
    print('')

    if choice >= lower and choice <=upper:
        return choice
    else:
        print("Invalid Selection. Select Again.\n")
        return get_user_selection(lower, upper)
