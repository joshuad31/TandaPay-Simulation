import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

DB_DIR = os.path.join(_cur_dir, 'databases')

ROOT_DIR = os.path.expanduser('~/.tandapay')
os.makedirs(ROOT_DIR, exist_ok=True)

RESULT_DIR = os.path.join(_cur_dir, 'result')
os.makedirs(RESULT_DIR, exist_ok=True)

MIN_VARIABLES = {
    'ev': [0, 1000, 25, 10, 10, 20, 2, 0, 0],
    'pv': [20, 1, 30, 5, 0, 0]
}
MAX_VARIABLES = {
    'ev': [100, 1000, 75, 45, 30, 80, 4, 3],
    'pv': [40, 15, 70, 25, 100, 100]
}
try:
    from local_settings import *
except ImportError:
    pass
