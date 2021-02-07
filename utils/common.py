import json
import os
import sys
import threading

from utils.logger import logger

_cur_dir = os.path.dirname(os.path.realpath(__file__))
_par_dir = os.path.join(_cur_dir, os.path.pardir)
if _par_dir not in sys.path:
    sys.path.append(_par_dir)


from settings import CONFIG_FILE


def update_dict_recursively(dest, updated):
    """
    Update dictionary recursively.
    :param dest: Destination dict.
    :type dest: dict
    :param updated: Updated dict to be applied.
    :type updated: dict
    :return:
    """
    for k, v in updated.items():
        if isinstance(dest, dict):
            if isinstance(v, dict):
                r = update_dict_recursively(dest.get(k, {}), v)
                dest[k] = r
            else:
                dest[k] = updated[k]
        else:
            dest = {k: updated[k]}
    return dest


lock = threading.Lock()


def update_config_file(data):
    old_data = update_dict_recursively(dest=get_config(), updated=data)
    with lock:
        with open(CONFIG_FILE, 'w') as jp:
            json.dump(old_data, jp, indent=2)


def get_config():
    with lock:
        try:
            conf = json.loads(open(CONFIG_FILE).read())
        except Exception as e:
            logger.error(f"Failed to read config file ({e})")
    return conf


def number_to_ordinal(n):
    """
    Convert number to ordinal number string
    """
    return "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
