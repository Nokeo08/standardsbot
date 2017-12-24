#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw

from Config import USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, SUBREDDITS
from utils import ResponseBuilder
from utils.Database import create_table, replied_to, insert
from utils.Failable import failable
from utils.Util import log


def authenticate():
    log("Authenticating...")
    reddit = praw.Reddit(username=USERNAME,
                         password=PASSWORD,
                         client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent="StandardsBot v1.2 for reddit. /u/Nokeo08")
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
                comment.reply(text)
                insert(comment.id, sub, comment.author.name, citation)
                log("Responded to " + comment.author.name + " on " + sub + " with " + citation)
                if malformed:
                    log(comment.author.name + "submitted a malformed request. Some of all of their "
                                              "request was not fulfilled")


def main():
    prepare_database()
    reddit = authenticate()
    rb = ResponseBuilder()
    while 1:
            for sub in SUBREDDITS:
                process_subreddit(sub, reddit, rb)


if __name__ == '__main__':
    main()
