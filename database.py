import sqlite3
import time
import datetime

def connect():
    return sqlite3.connect('comments_processed.db')

def close(connection):
    connection.close()

def create_table():
    db_conn = connect()
    db_conn.cursor().execute("CREATE TABLE IF NOT EXISTS replies(author TEXT, citation TEXT, comment_id TEXT, timestamp TEXT)")
    db_conn.commit()
    close(db_conn)

def insert(author, citation, comment_id):
    db_conn = connect()
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

    db_conn.cursor().execute("INSERT INTO replies (author, citation, comment_id, timestamp) VALUES (?, ?, ?, ?)",
          (author, citation, comment_id, date))
    db_conn.commit()
    close(db_conn)
  
def read_all():
    db_conn = connect()
    c = db_conn.cursor()
    c.execute("SELECT * FROM replies")
    data = c.fetchall()
    if(data):
        for d in data:
            print(d)
    else:
        print('Nothing to Read')
    close(db_conn)

def replied_to(comment_id):
    db_conn = connect()
    c = db_conn.cursor()
    c.execute("SELECT comment_id FROM replies WHERE comment_id = '" + comment_id + "'")
    if c.fetchone():
        return True
    else:
        return False
