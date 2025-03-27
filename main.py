import os
from authentication import *
from utils import *
from RedditRefresh import RedditRefresh

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to RedditRefresh!\n")

    user_mode = display_mode_menu()
    user_content = diplay_content_menu()

    criteria_subreddit = ''
    criteria_from_date = ''
    criteria_to_date = ''

    criteria_subreddit = askForSubReddit()
    criteria_from_date = askFromDate()
    criteria_to_date = askToDate(criteria_from_date)

    confirmation = True if askForConfirmation(user_mode) == 1 else False
    if confirmation:
        redditRefresh = RedditRefresh(user_mode, user_content, criteria_subreddit, criteria_from_date, criteria_to_date)
        redditRefresh.executeQuery()
    else:
        main()

if __name__ == "__main__":
    main()
