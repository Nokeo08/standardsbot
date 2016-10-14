#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw
from standards import standards, log
import os
from config import *
from database import create_table, replied_to, insert
from time import sleep
from warnings import filterwarnings
from requests.exceptions import ConnectionError, ChunkedEncodingError

# Ignores ResourceWarnings caused by praw issue #329
filterwarnings("ignore", category=ResourceWarning)
#Ignores UserWarning caused by having 'bot' in user agent
filterwarnings("ignore", category=UserWarning)
# Ignores DeprecationWarnings caused by PRAW
filterwarnings("ignore", category=DeprecationWarning)

# Check that the file that contains our username exists
if not os.path.isfile("config.py"):
    log("You must create a config file with your username and password.")
    log("Please see config.py")
    exit(1)

# Create the Reddit instance
user_agent = ("StandardsBot v0.1 for reddit. /u/Nokeo08")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USER, REDDIT_PASS, disable_warning=True)
log("Logged In.")
create_table()
log("Database Ready")

stds = standards()
log("Standards Loaded")

while(1):
    try:
        subreddit = r.get_subreddit(SUBREDDIT)
        all_comments = subreddit.get_comments(limit=None)
        for comment in all_comments:
            if not replied_to(comment.id):
                response, citation, malformed = stds.fetch(comment.body)
                if len(response) > 0:
                    try:
                        comment.reply(response)
                        insert(comment.author.name, citation, comment.id)
                    except praw.errors.RateLimitExceeded as error:
                        log("Rate Limit Exceeded. Sleeping for %d seconds" % error.sleep_time)
                        sleep(error.sleep_time)
                        comment.reply(response)
                        insert(comment.author.name, citation, comment.id)
                    log("Responded to: " + comment.author.name + " with citations for " + citation)
                    if malformed:
                        log(comment.author.name + " submitted a malformed request. Some of all of their request was not fulfilled")
        sleep(30)
    except (ConnectionError, ConnectionResetError, ChunkedEncodingError) as e:
        pass
