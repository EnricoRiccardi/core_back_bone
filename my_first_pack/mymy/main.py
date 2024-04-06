import datetime
import sys

_DATE_FMT = '%d.%m.%Y %H:%M:%S'

def hello_world():
    """
    Greets.

    """
    timestart = datetime.datetime.now().strftime(_DATE_FMT)
    pyversion = sys.version.split()[0]
    print(f'Start of execution: {timestart}')
    print(f'Python version: {pyversion}')
    return timestart, pyversion
