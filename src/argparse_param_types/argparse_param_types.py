import argparse
import logging

logger = logging.getLogger(__name__)


def file_type(val: str, message: str = "Provided file does not exist.") -> str:
    """Argparse type checking that the parameter is an existing file
    on the filesystem.

    :param val: file path to check if it exists
    :param message: (optional) Message string used in raised error
    :return: Same value as param `val`
    :rtype: str
    """
    from os import path

    if path.isfile(val):
        return val
    else:
        logger.error(message)
        raise argparse.ArgumentTypeError(message)


def directory_type(
    val: str,
    message: str = "Provided directory does not exist.",
) -> str:
    """Argparse type checking that the parameter is an existing directory
    on the filesystem.

    :param val: directory path to check if it exists
    :param message: (optional) Message string used in raised error
    :return: Same value as param `val`
    :rtype: str
    """
    from os import path

    if path.isdir(val):
        return val
    else:
        logger.error(message)
        raise argparse.ArgumentTypeError(message)
