# Reddit Post and Comment Deleter

This script allows you to delete your old Reddit posts and comments automatically.
It uses the [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw) library to access the Reddit API and delete posts and comments based on a
given time threshold.

## Usage

1. Clone the repository: `git clone https://github.com/JosemyDuarte/reddit-cleaner.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and create a new "script" type
   application. You can name it whatever you like and set the description and about url to anything you want.
4. Set the following environment variables with your Reddit account information:

```shell
REDDIT_CLIENT_ID=<your_client_id>
REDDIT_CLIENT_SECRET=<your_client_secret>
REDDIT_USERNAME=<your_reddit_username>
REDDIT_PASSWORD=<your_reddit_password>
REDDIT_USER_AGENT=<your_user_agent>
```

You got the `client_id` and `client_secret` on previous step by creating the app. For the user_agent, you can use any
string that identifies your script.

5. (Optional) Set the `REDDIT_DELETE_THRESHOLD` environment variable to specify the number of days before which posts
   and comments will be deleted. By default, anything older than a year will be deleted.

```shell
REDDIT_DELETE_THRESHOLD=365
```

6. Run the script:

```shell
python delete_posts_and_comments.py
```

## Acknowledgments
This script was inspired by [Adrian Tombu's Twitter cleaning script](https://github.com/adriantombu/twitter-cleaning). Although for me, it was enough running it locally, so there is no Github Actions cron.


