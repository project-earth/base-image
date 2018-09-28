import os
import logging
from baseimage.config.config import CONFIG


def get_default_logger(name=CONFIG['service_name'], logging_dir=None):
    """ Generates a sensible default python logging object for general logging use in services.
        The logger object is given both a stream handler and a file handler set to warning and info
        levels respectively.

    Args
        name <str>: The name given to the python logging object. Defaults to the service name.
        logginer_dir <str>: The path to which logs will be written to disk. Defaults to the
            following path: <base_path>/<service_name>/logs/<logger_name>
    """
    if logging_dir is None:
        logging_dir = os.path.join(CONFIG['base_path'], "logs", name)

    logger = logging.getLogger(name)
    formatter = logging.Formatter('(%(asctime)s)[%(levelname)s]: %(message)s')

    file_handler = logging.FileHandler(filename=logging_dir)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARN)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
