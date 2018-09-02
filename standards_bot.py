#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw

from code.ResponseBuilder import ResponseBuilder
from code.utils.database import create_table, replied_to, insert
from code.utils.failable import failable
from code.utils.misc import log, load_json


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
    subreddits = load_json("conf")["SUBREDDITS"]
    while 1:
        for sub in subreddits:
            process_subreddit(sub, reddit, rb)


if __name__ == '__main__':
    main()
