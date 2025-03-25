import time
import datetime
import praw
import os
from praw.exceptions import RedditAPIException
from authentication import *
from manageText import hashComment, hashPost
from aesEncryptDecrypt import aesEncrypt, aesDecrypt


class RedditRefresh:
    def __init__(self, user_mode, user_content, criteria_subreddit, criteria_from_date, criteria_to_date):
        self.redditInit()
        self.fileInit()
        self.user = self.reddit.redditor(USERNAME)
        self.user_mode = user_mode
        self.user_content = user_content
        self.criteria_subreddit = criteria_subreddit
        self.criteria_from_date = criteria_from_date 
        self.criteria_to_date =criteria_to_date

    def redditInit(self):
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            password=PASSWORD,
            user_agent=USER_AGENT,
            username=USERNAME
        )
    
    def redditRefreshSleep(self):
        # Do not cross 100 queries per minute per OAuth client id limit
        time.sleep(0.7)
    
    def fileInit(self):
        self.file = open("LOGS.md", "a+", encoding="utf-8")
        if os.path.getsize("LOGS.md") == 0:
            print("No Previously stored Logs found. Creating a new LOGS.md...")
            self.file.write(
                "# Logs of using [RedditRefresh](https://github.com/karan51ngh/RedditRefresh)\n")
        
        self.file.write("\n---\n")
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"## Script executed at: {time_string}\n"
        self.file.write(log_message)

    def fileEnd(self):
        self.file.write("\n---\n")
        self.file.write(
                "# Thank you for using [RedditRefresh](https://github.com/karan51ngh/RedditRefresh).\n"
                "Consider giving us a star.")
        self.file.close()

    def managePosts(self):
        SUB = self.criteria_subreddit
        MODE = self.user_mode
        FROM_DATE = self.criteria_from_date
        TO_DATE = self.criteria_to_date
        
        try:
            print("Iterating over your Posts.\n")
            print(f'SUB is {SUB}')
            print(f'MODE is {MODE}')
            print(f'FROM_DATE is {FROM_DATE}')
            print(f'TO_DATE is {TO_DATE}')
            for submission in self.user.submissions.new(limit=None):
                if SUB != '' and submission.subreddit.display_name.lower() != SUB.lower():
                   continue
                if not (submission.created_utc >= FROM_DATE.timestamp() and submission.created_utc <= TO_DATE.timestamp()):
                    continue
                if MODE == 'HASH' or MODE == 'DELETE':
                    hashed_text = hashPost(self.file, submission.title, submission.selftext)
                    if submission.selftext != "":
                        submission.edit(hashed_text)
                    self.redditRefreshSleep()
                    if MODE == 'DELETE':
                        submission.delete()
                        self.redditRefreshSleep()
                    print(f"POST title:\n {submission.title}\n")
                    print(f"POST body, SHA-256 Hashed:\n {hashed_text}\n\n")
                elif MODE == 'ENCRYPT':
                    postBody = str(submission.selftext)
                    if postBody.startswith("RR_AES_ENCRYPTED"):
                        continue
                    encrypted_text = "RR_AES_ENCRYPTED" + aesEncrypt(postBody).decode('utf-8')
                    print(f"POST title:\n {submission.title}\n")
                    print(f"POST body, AES Encrypted:\n {encrypted_text}\n\n")
                    submission.edit(str(encrypted_text))
                    self.redditRefreshSleep()
                else:
                    postBody = str(submission.selftext)
                    if postBody.startswith("RR_AES_ENCRYPTED"):
                        postBody = postBody.removeprefix("RR_AES_ENCRYPTED")
                        decrypted_text = aesDecrypt(postBody.encode('utf-8', errors='replace'))
                        print(f"ENCRYPTED COMMENT:\n {submission.selftext}\n")
                        print(f"COMMENT body, AES Decrypted:\n {decrypted_text}\n\n")
                        submission.edit(decrypted_text)
                        self.redditRefreshSleep()
                
        except RedditAPIException as e:
            print(
                f"Reddit API Exception raised while Processing Post Content: [{e.error_type}: {e.message}]")

    def manageComments(self):
        SUB = self.criteria_subreddit
        MODE = self.user_mode
        FROM_DATE = self.criteria_from_date
        TO_DATE = self.criteria_to_date

        try:
            print("Iterating over your Comments.\n")
            for comment in self.user.comments.new(limit=None):
                if SUB != '' and comment.subreddit.display_name.lower() != SUB.lower():
                   continue
                if not (comment.created_utc >= FROM_DATE.timestamp() and comment.created_utc <= TO_DATE.timestamp()):
                    continue
                if MODE == 'HASH' or MODE == 'DELETE':
                    hashed_text = hashComment(self.file, comment.body)
                    print(f"COMMENT: {comment.body}\n")
                    print(f"HASH of the COMENT body: {hashed_text}\n\n")
                    comment.edit(hashed_text)
                    self.redditRefreshSleep()
                    if MODE == 'DELETE':
                        comment.delete()
                        self.redditRefreshSleep()
                elif MODE == 'ENCRYPT':
                    commentBody = str(comment.body)
                    if commentBody.startswith("RR_AES_ENCRYPTED"):
                        continue
                    encrypted_text = "RR_AES_ENCRYPTED" + aesEncrypt(commentBody).decode('utf-8')
                    print(f"COMMENT:\n {comment.body}\n")
                    print(f"COMMENT body, AES Encrypted:\n {encrypted_text}\n\n")
                    comment.edit(str(encrypted_text))
                    self.redditRefreshSleep()
                else:
                    # MODE == 'DECRYPT'
                    commentBody = str(comment.body)
                    if commentBody.startswith("RR_AES_ENCRYPTED"):
                        commentBody = commentBody.removeprefix("RR_AES_ENCRYPTED")
                        decrypted_text = aesDecrypt(commentBody.encode('utf-8', errors='replace'))
                        print(f"ENCRYPTED COMMENT:\n {comment.body}\n")
                        print(f"COMMENT body, AES Decrypted:\n {decrypted_text}\n\n")
                        comment.edit(decrypted_text)
                        self.redditRefreshSleep()
        except RedditAPIException as e:
            print(
                f"Reddit API Exception raised while Processing Comment Content: [{e.error_type}: {e.message}]")

    def executeQuery(self):
        if self.user_content == 'POST':
                self.managePosts()
        else:
            self.manageComments()
        self.fileEnd()