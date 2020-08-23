import sys
import __main__
import traceback

from copy import copy

import logging
from logging.handlers import RotatingFileHandler

import colorama
from colorama import Back, Fore, Style

FORMAT = "[%(asctime)s][%(levelname)8s] %(message)s"

COLORS = {
    'WARNING': Fore.YELLOW,
    'INFO': Fore.WHITE,
    'DEBUG': Fore.BLUE,
    'CRITICAL': Back.RED,
    'ERROR': Fore.RED
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_color = kwargs.get('use_color', True)

    def format(self, record):
        record = copy(record) # if we modify the original it will mess up all other formatters that use the same level name
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            record.levelname = f'{COLORS[levelname]}{levelname:>8s}{Style.RESET_ALL}'
        return super().format(record)


def makeLogger(name):
    color_formatter = ColoredFormatter(f'{FORMAT}{Style.RESET_ALL}', '%Y-%m-%d %H:%M:%S')
    formatter = logging.Formatter(FORMAT, '%Y-%m-%d %H:%M:%S')

    log = logging.getLogger(name)

    console = logging.StreamHandler()
    console.setFormatter(color_formatter)
    log.addHandler(console)

    file = RotatingFileHandler(__main__.__file__ + '.log', mode='a', maxBytes=5*1024*1024, backupCount=0, encoding=None, delay=0)
    file.setFormatter(formatter)
    file.setLevel(logging.DEBUG)
    log.addHandler(file)

    def except_handler(type, value, tb):
        log.critical("FATAL ERROR:\n{1}, Traceback:\n{0}\n{2}".format(''.join(traceback.format_tb(tb)), str(type.__name__), value))

    sys.excepthook = except_handler

    return log
