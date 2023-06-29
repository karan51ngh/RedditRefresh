from authentication import *
import praw
import time
from authentication import *
from praw.exceptions import RedditAPIException


def DPS():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent=USER_AGENT,
        username=USERNAME
    )

    user = reddit.redditor(USERNAME)

    subreddit_name = input("Enter Subbredit Name:")

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
