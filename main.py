import praw
import os
import time
from datetime import datetime, timezone
from praw.exceptions import RedditAPIException


def delete_posts_and_comments():
    username = os.environ['REDDIT_USERNAME']
    days_threshold = os.environ.get('REDDIT_DELETE_THRESHOLD', 365)  # default to deleting anything older than a year
    threshold = int(datetime.now(timezone.utc).timestamp()) - days_threshold * 24 * 60 * 60

    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_CLIENT_SECRET'],
        password=os.environ['REDDIT_PASSWORD'],
        username=username,
        user_agent=os.environ['REDDIT_USER_AGENT']
    )

    user = reddit.redditor(username)

    print(f"Iterating over {user.name} posts and comments")

    try:
        for submission in user.submissions.new():
            if submission.created_utc <= threshold:
                print(f"Deleting post {submission.id}")
                submission.delete()

                # to avoid rate limit errors, wait for 1 second between each delete operation
                time.sleep(1)
    except RedditAPIException as e:
        print(f"Reddit API Exception raised while deleting posts: [{e.error_type}: {e.message}]")

    try:
        for comment in user.comments.new():
            if comment.created_utc <= threshold:
                print(f"Deleting comment {comment.id}")
                comment.delete()

                # to avoid rate limit errors, wait for 1 second between each delete operation
                time.sleep(1)
    except RedditAPIException as e:
        print(f"Reddit API Exception raised while deleting comments: [{e.error_type}: {e.message}]")


if __name__ == '__main__':
    delete_posts_and_comments()
