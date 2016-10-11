import datetime 

def log(msg):
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " + str(msg) + "\n", flush=True)
