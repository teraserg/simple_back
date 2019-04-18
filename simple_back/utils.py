import traceback
import logging


def exception_traceback_str(e):
    traceback_str = (str(e) + ':' + ''.join(traceback.format_tb(e.__traceback__))).replace('\n', ' ')
    return traceback_str


def setup_logger(log_level='DEBUG'):
    """
    Setup transcriber logger and log format.
    :param log_level: string
    :return:
    """
    logger = logging.getLogger(__name__.split('.')[0])

    if logger.hasHandlers():
        logger.handlers.clear()

    stream_handler = logging.StreamHandler()

    log_format = '%(asctime)s %(levelname)s: %(message)s ' \
                 '[in %(filename)s:%(lineno)d]'

    stream_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(stream_handler)

    logger.setLevel(log_level)
    return logger
