#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw
from parser import fetchCitations, log
import os
from config import *
from time import sleep
from warnings import filterwarnings
from requests.exceptions import ConnectionError

# Ignores ResourceWarnings caused by praw issue #329
filterwarnings("ignore", category=ResourceWarning)
#Ignores UserWarning caused by having 'bot' in user agent
filterwarnings("ignore", category=UserWarning)
# Ignores DeprecationWarnings caused by PRAW
filterwarnings("ignore", category=DeprecationWarning)

comments_file_name = "comments_processed.txt"


# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    log("You must create a config file with your username and password.")
    log("Please see config_bot.py")
    exit(1)

# Create the Reddit instance
user_agent = ("StandardsBot v0.1 for reddit. /u/Nokeo08")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USER, REDDIT_PASS, disable_warning=True)
log("Logged in.")
# Have we run this code before? If not, create an empty list
if not os.path.isfile(comments_file_name):
    comments_processed = []
# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open(comments_file_name, "r") as f:
        comments_processed = f.read()
        comments_processed = comments_processed.split("\n")
        comments_processed = list(filter(None, comments_processed))
    log("comments_processed read in")
while(1):
    try:
        subreddit = r.get_subreddit(SUBREDDIT)
        all_comments = subreddit.get_comments()
        for comment in all_comments:
            if comment.id not in comments_processed:
                response, citation = fetchCitations(comment.body)
                if len(response) > 0:
                    with open(comments_file_name, "a") as f:
                        f.write(comment.id + "\n")
                    comments_processed.append(comment.id)
                    try:
                        comment.reply(response)
                    except praw.errors.RateLimitExceeded as error:
                        log("Rate Limit Exceeded. Sleeping for %d seconds" % error.sleep_time)
                        sleep(error.sleep_time)
                        comment.reply(response)
                    log("Responded to: " + comment.author.name + " with citations for " + citation)
        sleep(30)
    except ConnectionError as e:
        log("ConnectionError")
        pass
