from authentication import *
import praw
import time
from authentication import *
from praw.exceptions import RedditAPIException
from askDate import ask_for_date


def DCBD():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent=USER_AGENT,
        username=USERNAME
    )

    user = reddit.redditor(USERNAME)

    dt = ask_for_date()
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
