from datetime import datetime
from json import load, dump

from pytz import timezone


def log(msg):
    print(str(datetime.now(timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S')) + ": " + str(msg) + "\n", flush=True)


def load_json(std):
    with(open("standards/json/" + std.upper() + ".json", "r")) as infile:
        return load(infile)


def dump_json(std, data):
    with(open("standards/json/" + std.upper() + ".json", "w")) as outfile:
        return dump(data, outfile)
