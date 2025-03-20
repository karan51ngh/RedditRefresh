import os
from authentication import *
from utils import *


os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to RedditRefresh!\n")

user_mode = display_mode_menu()
user_content = diplay_content_menu()
user_criteria = diplay_criteria_options()
criteria_subreddit = ''
criteria_date = ''
before_after_date = ''

if user_criteria == "SUBREDDIT":
    criteria_subreddit = askForSubReddit()
else:
    criteria_date = askForDate()
    before_after_date = askBeforeAfter(criteria_date)

confirmation = True if askForConfirmation(user_mode) == 1 else False

if(confirmation):
    print("Thanks for using RedditRefresh by karan51ngh\n")
