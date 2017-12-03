from datetime import datetime
from pytz import timezone


def log(msg):
    print(str(datetime.now(timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S')) + ": " + str(msg) + "\n", flush=True)
