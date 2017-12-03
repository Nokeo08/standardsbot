from time import sleep

import yagmail
from plumbum import local

from Config import GMAIL_USER, GMAIL_PASS, SMS_EMAIL_GATEWAY

# time to sleep between checks. Cuts down on cpu cycles and adds wait time
wait_time = 5 * 60
# define the controller to supervisord
supervisorctl = local["/usr/bin/supervisorctl"]
grep = local["/usr/bin/grep"]

# set up command to check the status of the processes that supervisord is watching
status = supervisorctl["status"] | grep["-i", "standardsbot\s*RUNNING"]


def bot_crashed():
    sleep(wait_time)
    try:
        status()  # if this does not raise an exception then the process is running
        return False
    except:
        return True


while 1:
    # If bot is up loop and check again else if bot is down twice send a text
    # Function sleeps before status check so there will be time in between checks
    if bot_crashed() and bot_crashed():
        yagmail.SMTP(GMAIL_USER, GMAIL_PASS).send(SMS_EMAIL_GATEWAY, "", "StandardsBot is down")
        exit(0)  # program wil be restarted when I manually reload supervisor
