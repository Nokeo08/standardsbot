import sqlite3
from datetime import datetime

from pytz import timezone


def __connect():
    return sqlite3.connect('comments_processed.db')


def __close(connection):
    connection.close()


def create_table():
    db_conn = __connect()
    db_conn.cursor().execute(
        "CREATE TABLE IF NOT EXISTS replies("
        "comment_id TEXT PRIMARY KEY UNIQUE NOT NULL, "
        "subreddit TEXT NOT NULL, "
        "author TEXT NOT NULL, "
        "citation TEXT NOT NULL, "
        "timestamp TEXT NOT NULL)")
    db_conn.commit()
    __close(db_conn)


def insert(comment_id, subreddit, author, citation):
    db_conn = __connect()
    date = str(datetime.now(timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S'))

    db_conn.cursor().execute("INSERT INTO replies (comment_id, subreddit, author, citation, timestamp) "
                             "VALUES (?, ?, ?, ?, ?)",
                             (comment_id, subreddit.lower(), author.lower(), citation, date))
    db_conn.commit()
    __close(db_conn)


def read_all():
    db_conn = __connect()
    c = db_conn.cursor()
    c.execute("SELECT * FROM replies")
    data = c.fetchall()
    if data:
        for d in data:
            print(d)
    else:
        print('Nothing to Read')
    __close(db_conn)


def replied_to(comment_id):
    db_conn = __connect()
    c = db_conn.cursor()
    c.execute("SELECT comment_id FROM replies WHERE comment_id = '" + comment_id + "'")
    if c.fetchone():
        __close(db_conn)
        return True
    else:
        __close(db_conn)
        return False
