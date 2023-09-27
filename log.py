from datetime import datetime

INFO = 'INFO '
DEBUG = 'DEBUG'

def log(level, message):
    print(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f") + '|' + level + '|' + message)