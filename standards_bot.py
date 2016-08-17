import praw
import pdb
import re
import os
from config_bot import *
import time

comments_file_name = "comments_processed.txt"

# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print "You must create a config file with your username and password."
    print "Please see config_bot.py"
    exit(1)

# Create the Reddit instance
user_agent = ("StandardsBot v0.1 for reddit. /u/Nokeo08")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)

# Have we run this code before? If not, create an empty list
if not os.path.isfile(comments_file_name):
    comments_processed = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open(comments_file_name, "r") as f:
        comments_processed = f.read()
        comments_processed = comments_processed.split("\n")
        comments_processed = filter(None, comments_processed)

# Get the top 5 values from our subreddit
subreddit = r.get_subreddit(SUBREDDIT)
for submission in subreddit.get_hot(limit=5):
    flat_comments = praw.helpers.flatten_tree(submission.comments)

    for comment in flat_comments:
        if comment.id not in comments_processed:
            with open(comments_file_name, "a") as f:
                f.write(comment.id + "\n")
            comments_processed.append(comment.id)
            if "i love python" in comment.body:
                comment.reply("python sucks")
