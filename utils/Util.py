from datetime import datetime
from json import load, dump
import os
import sys

from pytz import timezone


def log(msg):
    print(str(datetime.now(timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S')) + ": " + str(msg) + "\n", flush=True)


def __get_path__(std):
    return os.path.join(sys.path[0], "standards/json/" + std.upper() + ".json")


def load_json(std):
    with(open(__get_path__(std), "r")) as infile:
        return load(infile)


def dump_json(std, data):
    with(open(__get_path__(std), "w")) as outfile:
        return dump(data, outfile)
