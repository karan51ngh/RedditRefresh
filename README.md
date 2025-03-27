# RedditRefresh
## Reddit Bulk Comment/Post Management Tool

This script allows you to Mass **Delete**, **Cryptographically Hash**, **Encrypt** or **Decrypt** your Reddit posts or comments for better privacy and security.

## Setting up the script

1. Clone the repository: `git clone https://github.com/karan51ngh/RedditRefresh.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and create a new "script" type application. You can name it whatever you like and set the description and about url to anything you want. You can add http://localhost:8080/ as the **redirect uri**. 
4. Open `authentication.py` in a text editor and edit the following information:

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
6. It creates a file called `LOGS.md` that saves all your comments and posts before hashing or deletion.

## How to Use

1. **Choose a Mode:** The script operates in four different modes:
   - **DELETE Mode**: Hashes your content using SHA-256 before deleting it.
   - **HASH Mode**: Only hashes your content without deleting it.
   - **ENCRYPT Mode**: Encrypts your content using the AES algorithm, allowing future decryption.
   - **DECRYPT Mode**: Decrypts previously encrypted content.

2. **Select Content Type:** Decide whether to process:
   - **COMMENTS**
   - **POSTS**

3. **Specify a Subreddit (Optional):**
   - Enter a subreddit name to restrict the script to that specific subreddit.
   - Leaving this blank will make the script apply to all subreddits.

4. **Set a Time Range (Optional):**
   - Enter a **start date** and **end date** to filter content within a specific time range.
   - If left empty, the script will apply to all content regardless of date.
   - **Note:** The time for each date is set to **00:00:00 UTC**.

5. **Confirm Execution:**
   - After providing the necessary inputs, confirm the execution, and the script will process your Reddit content accordingly.

## How it works

It uses the [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw) library to access the Reddit API and process the your posts and comments based on a particular sub-reddit you posted to, or on a given time threshold.

## License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](https://github.com/karan51ngh/RedditRefresh/blob/master/LICENSE) file for more details.

## Contributing

1. Fork the repository.
2. Clone your fork: `git clone https://github.com/your-username/RedditRefresh.git`
3. Create a new branch: `git checkout -b feature-name`
4. Commit your changes and push.
5. Open a pull request.

## Contact

Have questions or suggestions? Feel free to reach out!

- GitHub Issues: [Open an issue](https://github.com/karan51ngh/RedditRefresh/issues)
- Email: [karansingh9535@gmail.com](mailto\:karansingh9535@gmail.com)
- LinkedIn: [karan51ngh](https://www.linkedin.com/in/karan51ngh/)
- X / Twitter: [karan_51ngh](https://x.com/karan_51ngh)

## Disclaimer

Use this tool responsibly. If you choose the mode as **HASH** or **DELETE**, the changes will be permanent and irreversible.