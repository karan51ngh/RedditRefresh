from authentication import *
import praw
import time
from authentication import *
from praw.exceptions import RedditAPIException
from askDate import ask_for_date


def DPBD():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent=USER_AGENT,
        username=USERNAME
    )

    user = reddit.redditor(USERNAME)

    dt = ask_for_date()
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
