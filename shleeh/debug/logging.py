import os
from datetime import datetime


def logging(message, fname=None, path=None):
    now = datetime.now()
    date = now.strftime("%Y%m%d")

    if path is None:
        path = os.path.expanduser('~')
    if fname is None:
        fname = f'debug_{date}'
    with open(os.path.join(path, fname), 'a') as f:
        f.write(message)
