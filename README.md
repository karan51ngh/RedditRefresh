# Reddit Bulk Comment/Post Deletion and Encryption Tool

- This script allows you to **Mass-Delete** or **Encrypt** your old Reddit posts or comments.
- It **Encrypts** your posts or comments using **SHA-256** encryption algorithm **before deletion** to prevent Reddit from restoring your posts or comments after your account is deleted.
- You also have an option to only Encrypt your content and not Delete it. This can be useful in a case, where you want to **render your content unreadable** (For e.g. in protest of the Reddit API changes.).
- Additionally it also creates a **local backup** of your content in a mardown format file.
- It uses the [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw) library to access the Reddit API and delete posts and comments based on a particular sub-reddit you posted to, or on a given time threshold.

## Usage

1. Clone the repository: `git clone https://github.com/karan51ngh/RedditRefresh.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and create a new "script" type application. You can name it whatever you like and set the description and about url to anything you want. You can add http://localhost:8080/ as the **redirect uri**. 
4. Open `authentication.py` in a text editor and edit the follwing information:

```
CLIENT_ID = "<your_client_id>"
CLIENT_SECRET = "<your_client_secret>"
PASSWORD = "<your_account_password>"
USER_AGENT = "<your script's name (by u/your_username)>"
USERNAME = "<your_username>"
```
For Help with the above step refer [this](https://i.imgur.com/31TI2XA.png) image.

5. Run the script:

```shell
cd RedditRefresh
python main.py
```
6. It creates a file called `LOGS.md` that saves all your comments and posts before deletion.

## Options

- You have 2 modes in which the above script will operate.
    - DELETE mode (this option will first ENCRYPT your content and then DELETE it)
    - ENCRYPT mode (this option will only ENCRYPT your content)
- Currently you get 6 options on how to proceede with the Encryption/Deletion of your Posts/Comments:
    1. Delete/Encrypt all your **Comments** from a particular **Subreddit**.
    2. Delete/Encrypt all your **Posts** from a particular **Subreddit**.
    3. Delete/Encrypt all your **Comments before** a particular **Date**.
    4. Delete/Encrypt all your **Posts before** a particular **Date**.
    5. Delete/Encrypt all your **Comments after** a particular **Date**.
    6. Delete/Encrypt all your **Posts after** a particular **Date**.

## Acknowledgments

This script is a fork of [JosemyDuarte's reddit-cleaner](https://github.com/JosemyDuarte/reddit-cleaner).