from authentication import *
import praw
import time
from authentication import *
from praw.exceptions import RedditAPIException
from askDate import ask_for_date


def delete(flag_SubDate, flag_commentsPosts, flag_beforeAfter):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent=USER_AGENT,
        username=USERNAME
    )

    user = reddit.redditor(USERNAME)

    if flag_SubDate == True:
        subreddit_name = input("Enter Subbredit Name:")
        if flag_commentsPosts == True:
            # from SUBREDDIT delete COMMENTS
            print(f"Iterating over your Comments from {subreddit_name}")
            try:
                for comment in user.comments.new(limit=None):
                    if comment.subreddit.display_name.lower() == subreddit_name.lower():
                        print(f"Deleting comment: {comment.body}")
                        comment.delete()
                        time.sleep(2)
            except RedditAPIException as e:
                print(
                    f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
        else:
            # from SUBREDDIT delete POSTS
            print(f"Iterating over your Posts from {subreddit_name}")
            try:
                for submission in user.submissions.new(limit=None):

                    if submission.subreddit.display_name.lower() == subreddit_name.lower():
                        print(f"Deleting post {submission.title}")
                        submission.delete()
                        time.sleep(2)
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
                            print(f"Deleting comment: {comment.body}")
                            comment.delete()
                            time.sleep(2)
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
            else:
                # all COMMENTS AFTER a DATE
                print(f"Iterating over your Comments posted after {dt}")

                try:
                    for comment in user.comments.new(limit=None):

                        if comment.created_utc >= dt.timestamp():
                            print(f"Deleting comment: {comment.body}")
                            comment.delete()
                            time.sleep(2)
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
                            print(f"Deleting post: {submission.title}")
                            submission.delete()
                            time.sleep(2)
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
            else:
                # all POSTS AFTER a DATE
                print(f"Iterating over your Posts after {dt}")

                try:
                    for submission in user.submissions.new(limit=None):

                        if submission.created_utc >= dt.timestamp():
                            print(f"Deleting post: {submission.title}")
                            submission.delete()
                            time.sleep(2)
                except RedditAPIException as e:
                    print(
                        f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")
