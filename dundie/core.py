"""Core module of dundie"""
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database
    
    >>> len(load('assets/people.csv'))
    2
    """
    try:
        with open(filepath) as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError as e:
        print(f"File not found {e}")
