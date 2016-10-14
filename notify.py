from plumbum import local
from plumbum.cmd import grep
import yagmail
from time import sleep
from config import GMAILUSER, GMAILPASS, SMSEMAILGATEWAY

#time to sleep between checks. Cuts down on cpu cycles and adds wait time
wait_time = 5*60
# define the controler to supervisord
supervisorctl = local["/usr/bin/supervisorctl"]

#set up command to check the status of the processes that supervisord is watching
status = supervisorctl["status"] | grep["-i","standardsbot\s*RUNNING"]



def bot_crashed():
    sleep(wait_time)
    try:
        status() # if this does not raise an exception then the process is running
        return False
    except:
        return True

while(1):
    #If bot is up loop and check again else if bot is down twice send a text
    #Funciton sleeps before status check so there will be time inbetween checks
    if bot_crashed() and bot_crashed():
        yagmail.SMTP(GMAILUSER, GMAILPASS).send(SMSEMAILGATEWAY,"", "StandardsBot is down")
        exit(0) # program wil be restared when I manually reload supervisor
