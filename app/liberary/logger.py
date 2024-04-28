# -*- coding: utf-8 -*-
import logging


def get_logger(logger_level):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(module)s - [%(levelname)s] : %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S %p', )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logger_level)
    return logger
