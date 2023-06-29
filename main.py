import os
from datetime import datetime, timezone

from praw.exceptions import RedditAPIException

from authentication import *
from welcome import *

from deleteCommentsFromSub import DCS
from deleteCommentsBeforeDate import DCBD
from deleteCommentsAfterDate import DCAD

from deletePostsFromSub import DPS
from deletePostsBeforeDate import DPBD
from deletePostsAfterDate import DPAD

while True:
    display_menu()
    user_choice = get_user_choice()

    if user_choice == "1":
        print('YOU SELECTD: "Delete all your Comments from a particular Subreddit."')
        DCS()
        break
    elif user_choice == "2":
        print('YOU SELECTD: "Delete all your Posts from a particular Subreddit"')
        DPS()
        break
    elif user_choice == "3":
        print('YOU SELECTD: "Delete all your Comments before a particular Date"')
        DCBD()
        break
    elif user_choice == "4":
        print('YOU SELECTD: "Delete all your Posts before a particular Date"')
        DPBD()
        break
    elif user_choice == "5":
        print('YOU SELECTD: "Delete all your Comments after a particular Date"')
        DCAD()
        break
    elif user_choice == "6":
        print('YOU SELECTD: "Delete all your Posts after a particular Date"')
        DPAD()
        break
    elif user_choice == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Quitting the program...")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please try again.")
