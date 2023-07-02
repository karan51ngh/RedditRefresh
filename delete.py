import time
import datetime
import praw
import os
from praw.exceptions import RedditAPIException
from authentication import *
from askDate import ask_for_date
from manageText import manageText


def delete(flag_SubDate, flag_commentsPosts, flag_beforeAfter, flag_deleteAndEdit):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent=USER_AGENT,
        username=USERNAME
    )

    file = open("LOGS.md", "a+")
    if os.path.getsize("LOGS.md") != 0:
        file.write("\n---\n")
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"## Script executed at: {time_string}\n"
        file.write(log_message)
    else:
        # LOGS.md wasn't found in the directory
        print("No Previously stored Logs found. Creating a new LOGS.md...")
        file.write(
            "# Logs of using [RedditRefresh](https://github.com/karan51ngh/RedditRefresh)\n")
        file.write("\n---\n")
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"## Script executed at: {time_string}\n"
        file.write(log_message)

    user = reddit.redditor(USERNAME)

    if flag_SubDate == True:
        subreddit_name = input("Enter Subbredit Name: ")
        if flag_commentsPosts == True:
            # from SUBREDDIT delete COMMENTS
            print(f"Iterating over your Comments from {subreddit_name}")
            try:
                for comment in user.comments.new(limit=None):
                    if comment.subreddit.display_name.lower() == subreddit_name.lower():
                        hashed_text = manageText(
                            comment.body, file, flag_commentsPosts)
                        print(f"COMMENT: {comment.body}")
                        print(f"HASH: {hashed_text}")
                        comment.edit(hashed_text)
                        time.sleep(2)
                        if flag_deleteAndEdit:
                            comment.delete()
                        time.sleep(2)
                file.write("\n---\n")
                file.close()
            except RedditAPIException as e:
                print(
                    f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
        else:
            # from SUBREDDIT delete POSTS
            print(f"Iterating over your Posts from {subreddit_name}")
            try:
                for submission in user.submissions.new(limit=None):

                    if submission.subreddit.display_name.lower() == subreddit_name.lower():
                        hashed_text = manageText(
                            submission.title, file, flag_commentsPosts, submission.selftext)
                        print(f"POST TITLE: {submission.title}")
                        print(f"HASH: {hashed_text}")
                        if submission.selftext != "":
                            submission.edit(hashed_text)
                            time.sleep(2)
                        if flag_deleteAndEdit:
                            submission.delete()
                        time.sleep(2)
                file.write("\n---\n")
                file.close()
            except RedditAPIException as e:
                print(
                    f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
    else:
        dt = ask_for_date()
        if flag_commentsPosts == True:
            if flag_beforeAfter == True:
                # all COMMENTS BEFORE a DATE
                print(f"Iterating over your Comments posted before {dt}")

                try:
                    for comment in user.comments.new(limit=None):

                        if comment.created_utc <= dt.timestamp():
                            hashed_text = manageText(
                                comment.body, file, flag_commentsPosts)
                            print(f"COMMENT: {comment.body}")
                            print(f"HASH: {hashed_text}")
                            comment.edit(hashed_text)
                            time.sleep(2)
                            if flag_deleteAndEdit:
                                comment.delete()
                            time.sleep(2)
                    file.write("\n---\n")
                    file.close()
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
            else:
                # all COMMENTS AFTER a DATE
                print(f"Iterating over your Comments posted after {dt}")

                try:
                    for comment in user.comments.new(limit=None):

                        if comment.created_utc >= dt.timestamp():
                            hashed_text = manageText(
                                comment.body, file, flag_commentsPosts)
                            print(f"COMMENT: {comment.body}")
                            print(f"HASH: {hashed_text}")
                            comment.edit(hashed_text)
                            time.sleep(2)
                            if flag_deleteAndEdit:
                                comment.delete()
                            time.sleep(2)
                    file.write("\n---\n")
                    file.close()
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
        else:
            if flag_beforeAfter == True:
                # all POSTS BEFORE a DATE
                print(f"Iterating over your Posts before {dt}")

                try:
                    for submission in user.submissions.new(limit=None):

                        if submission.created_utc <= dt.timestamp():
                            hashed_text = manageText(
                                submission.title, file, flag_commentsPosts, submission.selftext)
                            print(f"POST TITLE: {submission.title}")
                            print(f"HASH: {hashed_text}")
                            if submission.selftext != "":
                                submission.edit(hashed_text)
                                time.sleep(2)
                            if flag_deleteAndEdit:
                                submission.delete()
                            time.sleep(2)
                    file.write("\n---\n")
                    file.close()
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
            else:
                # all POSTS AFTER a DATE
                print(f"Iterating over your Posts after {dt}")

                try:
                    for submission in user.submissions.new(limit=None):

                        if submission.created_utc >= dt.timestamp():
                            hashed_text = manageText(
                                submission.title, file, flag_commentsPosts, submission.selftext)
                            print(f"POST TITLE: {submission.title}")
                            print(f"HASH: {hashed_text}")
                            if submission.selftext != "":
                                submission.edit(hashed_text)
                                time.sleep(2)
                            if flag_deleteAndEdit:
                                submission.delete()
                            time.sleep(2)
                    file.write("\n---\n")
                    file.close()
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
