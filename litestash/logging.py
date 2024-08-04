"""The logging Module

Setup the root logger.

Logger modes:
Debug
Info
"""
import os
import logging
from logging import config
from litestash.core.config.root import Log

def log_env(env=None):
    """Functionla set and return for ENV"""
    if env not in [Log.DEV.value, Log.PROD.value] and env is not None:
        raise ValueError("Invalid environment")
    return os.getenv('RUN_ENV', env)

ENV = log_env()

def load_config(config_file=""):
    """Load the config function

    Loads the default configuration or a custom config file.
    """
    if ENV == Log.DEV.value:
        config_file = Log.DEV_FILE.value
    elif ENV == Log.PROD.value:
        config_file = Log.PROD_FILE.value
    else:
        config_file = Log.DEV_FILE.value
    try:
        config.fileConfig(config_file)
    except (FileNotFoundError, ValueError) as e:
        logging.error(f'Error loading logging configuration: {e}')

load_config()
root_logger = logging.getLogger()
if ENV == Log.DEV.value:
    root_logger.setLevel(logging.DEBUG)
elif ENV == Log.PROD.value:
    root_logger.setLevel(logging.INFO)
