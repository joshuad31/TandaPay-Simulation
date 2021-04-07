import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

DB_DIR = os.path.join(_cur_dir, 'databases')

ROOT_DIR = os.path.expanduser('~/.tandapay')
os.makedirs(ROOT_DIR, exist_ok=True)

RESULT_DIR = os.path.join(_cur_dir, 'result')
os.makedirs(RESULT_DIR, exist_ok=True)

try:
    from local_settings import *
except ImportError:
    pass
