import socket
import traceback

from requests.exceptions import ConnectionError, HTTPError, Timeout

from utils.Util import log


def failable(f):
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ConnectionError:
            full = traceback.format_exc()
            log("Connection error: %s" % full)
        except (Timeout, socket.timeout, socket.error):
            full = traceback.format_exc()
            log("Socket timeout! %s" % full)
            return None
        except HTTPError:
            full = traceback.format_exc()
            log("HTTP error %s" % full)
            return None

    return wrapped
