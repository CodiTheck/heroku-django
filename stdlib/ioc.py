import logging
from django.conf import settings


logger_format = "[%(asctime)s %(msecs)03dms] [PID %(process)d %(threadName)s] %(message)s";
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%Y-%m-%d %I:%M:%S %p %Z%z");


def log(message):
    """ Function that is used to print the logs. """
    if settings.DEBUG:
        logging.info(message);


pass;
