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

import os
from litestash.core.config.root import Log

def log_env(env: str = Log.PROD.value) -> str:  # Provide a default value
    """
    Gets the logging environment from the 'RUN_ENV' environment variable.

    Args:
        env:  Optional default environment to use if 'RUN_ENV' is not set.

    Returns:
        The logging environment ('dev' or 'prod').

    Raises:
        ValueError: If an invalid environment value is provided.
    """
    if env not in [Log.DEV.value, Log.PROD.value]:
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
