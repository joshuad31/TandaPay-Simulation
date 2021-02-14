import os
import shutil

_cur_dir = os.path.dirname(os.path.realpath(__file__))


ROOT_DIR = os.path.expanduser('~/.tandapay')
os.makedirs(ROOT_DIR, exist_ok=True)

CONFIG_FILE = os.path.expanduser(os.path.join(ROOT_DIR, 'config.json'))
if not os.path.exists(CONFIG_FILE):
    print('No JSON Config File Found! Recovering the default one...')
    shutil.copy(os.path.join(_cur_dir, 'utils', 'default_config.json'), CONFIG_FILE)

RESULT_DIR = os.path.join(_cur_dir, 'result')
os.makedirs(RESULT_DIR, exist_ok=True)

try:
    from local_settings import *
except ImportError:
    pass
