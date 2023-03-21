#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw

from code.ResponseBuilder import ResponseBuilder
from code.utils.database import create_table, replied_to, insert
from code.utils.failable import failable
from code.utils.misc import log, load_json
import re
import time


def authenticate():
    log("Authenticating...")
    conf = load_json("conf")
    reddit = praw.Reddit(username=conf["AUTH"]["USERNAME"],
                         password=conf["AUTH"]["PASSWORD"],
                         client_id=conf["AUTH"]["CLIENT_ID"],
                         client_secret=conf["AUTH"]["CLIENT_SECRET"],
                         user_agent="StandardsBot v" + conf["VERSION"] + " for reddit. /u/Nokeo08")
    log("Authenticated as {}".format(reddit.user.me()))
    return reddit


def prepare_database():
    create_table()
    log("Database Ready")


@failable
def process_subreddit(sub, reddit, rb):
    for comment in reddit.subreddit(sub).comments(limit=None):
        if not replied_to(comment.id) and comment.archived is False:
            text, citation, malformed = rb.fetch(comment.body)
            if len(text) > 0:
                try:
                    log(f"Attempting to respond to {comment.author.name} on {sub} with {citation} at https://reddit.com{comment.permalink}")
                    comment.reply(text)
                    insert(comment.id, sub, comment.author.name, citation)
                    log(f"Responded to {comment.author.name} on {sub} with {citation}")
                    if malformed:
                        log(f"{comment.author.name} submitted a malformed request. Some of all of their " \
                            "request was not fulfilled")
                except praw.exceptions.RedditAPIException as e:
                    if 'RATELIMIT' in str(e):
                        ## If we're ratelimited, then we must wait and try again
                        x = re.search("Take a break for (\d+) (\w+) before trying again", str(e))
                        time_amount = x.group(1)
                        time_type = x.group(2)
                        if 'minute' in time_type:
                            time_multiplier = 60
                        elif 'second' in time_type:
                            time_multiplier = 1
                        else:
                            raise Exception(f"Don't know time type: {time_type}")
            
                        time_to_wait = (int(time_amount) + 1) * time_multiplier
                        log(f"Ratelimited for {time_amount} {time_type}. Sleeping...")
                        time.sleep(time_to_wait)
                        continue
                    else:
                        log(f"Don't know the RedditAPIException type for this: {e}")
                        continue

def main():
    prepare_database()
    reddit = authenticate()
    rb = ResponseBuilder()
    subreddits = load_json("conf")["SUBREDDITS"]
    while 1:
        for sub in subreddits:
            process_subreddit(sub, reddit, rb)


if __name__ == '__main__':
    main()
