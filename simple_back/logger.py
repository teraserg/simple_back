import logging

ROOT_LOGGER_NAME = __name__.split('.')[0]  # 'simple_back'


def setup_logger(log_level=logging.DEBUG):
    logger = logging.getLogger(ROOT_LOGGER_NAME)
    if logger.hasHandlers():
        logger.handlers.clear()

    log_format = '[%(asctime)s] [%(levelname)s] [%(message)s] [in %(filename)s:%(lineno)d]'
    formatter = logging.Formatter(log_format)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.setLevel(log_level)
    return logger


def get_logger(name=None):
    return logging.getLogger(name or ROOT_LOGGER_NAME)
