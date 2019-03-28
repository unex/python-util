import sys
import __main__
import traceback
import logging
from logging.handlers import RotatingFileHandler
import colorama
from colorama import Back, Fore, Style

colorama.init()

COLORS = {
    'WARNING': Fore.YELLOW,
    'INFO': Fore.WHITE,
    'DEBUG': Fore.BLUE,
    'CRITICAL': Back.RED,
    'ERROR': Fore.RED
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg, "%Y%m%d %H:%M:%S")
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            record.levelname = f'[{COLORS[levelname]}{levelname}{Style.RESET_ALL}]{" " * (8 - len(levelname))}'
        return logging.Formatter.format(self, record)

class ColoredLogger(logging.Logger):
    COLOR_FORMAT = f'[%(asctime)s]%(levelname)s %(message)s{Style.RESET_ALL}'
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)
        self.addHandler(console)

        file = RotatingFileHandler(__main__.__file__ + '.log', mode='a', maxBytes=5*1024*1024, backupCount=0, encoding=None, delay=0)
        file.setFormatter(color_formatter)
        self.addHandler(file)

        return

logging.setLoggerClass(ColoredLogger)
log = logging.getLogger(__name__)

def except_handler(type, value, tb):
    log.critical("FATAL ERROR:\n{1}, Traceback:\n{0}\n{2}".format(''.join(traceback.format_tb(tb)), str(type.__name__), value))

sys.excepthook = except_handler
