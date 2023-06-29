# Reddit Post and Comment Deleter

This script allows you to delete your old Reddit posts and comments automatically.
It uses the [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw) library to access the Reddit API and delete posts and comments based on a
given time threshold.

## Usage

1. Clone the repository: `git clone https://github.com/JosemyDuarte/reddit-cleaner.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and create a new "script" type
   application. You can name it whatever you like and set the description and about url to anything you want.
4. Open `authentication.py` in a text editor and edit the follwing information:

```
CLIENT_ID = "<your_client_id>"
CLIENT_SECRET = "<your_client_secret>"
PASSWORD = "<your_account_password>"
USER_AGENT = "<your script's name (by u/your_username)>"
USERNAME = "<your_username>"
```

You got the `client_id` and `client_secret` on previous step by creating the app. For the user_agent, you can use any
string that identifies your script.

5. Run the script:

```shell
cd reddit-cleaner
python main.py
```

## Acknowledgments
This script was inspired by [Adrian Tombu's Twitter cleaning script](https://github.com/adriantombu/twitter-cleaning). Although for me, it was enough running it locally, so there is no Github Actions cron.


