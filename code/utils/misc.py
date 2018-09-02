from datetime import datetime
from json import load, dump
import os
import sys

from pytz import timezone


def log(msg):
    print(str(datetime.now(timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S')) + ": " + str(msg) + "\n", flush=True)


def __get_full_path__(path):
    return sys.path[0] + "/json/" + path.lower() + ".json"


def load_json(path):
    with(open(__get_full_path__(path), "r")) as infile:
        return load(infile)


def dump_json(path, data):
    with(open(__get_full_path__(path), "w")) as outfile:
        return dump(data, outfile)
