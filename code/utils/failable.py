import socket
import traceback
from time import sleep

from prawcore import RequestException
from requests.exceptions import ConnectionError, HTTPError, Timeout

from code.utils.misc import log


def failable(f):
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ConnectionError:
            full = traceback.format_exc()
            log("Connection error: %s" % full)
            pass
        except (Timeout, socket.timeout, socket.error):
            full = traceback.format_exc()
            log("Socket timeout! %s" % full)
            pass
        except HTTPError:
            full = traceback.format_exc()
            log("HTTP error %s" % full)
            pass
        except RequestException:
            full = traceback.format_exc()
            log("Request Exception %s" % full)
            sleep(60)
            pass

    return wrapped
