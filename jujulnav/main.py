"""
Main entry point for the juju-lnav script.
"""

import argparse
import logging
import shutil
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
log = logging.getLogger('juju-lnav')


def parse_commandline() -> argparse.Namespace:
    """
    Parses the command line arguments.

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "unit",
        metavar="UNIT:LOGFILELS",
        nargs="+",
        help="The name of the UNIT and the shell glob of the LOGFILES",
    )
    parser.add_argument(
        "--debug",
        help="Print a lot of debug information",
        action="store_true",
    )
    return parser.parse_args()


def is_command_installed(command: str) -> bool:
    """
    Try to find `command`.

    Returns:
        bool: Whether `command` is installed.
    """
    return shutil.which(command) is not None


def main():
    """
    Main entry point.
    """

    options = parse_commandline()
    if options.debug:
        log.setLevel(logging.DEBUG)

    if not is_command_installed('juju'):
        print('''Please install juju with

sudo snap install juju

And rerun this script.''')
        sys.exit(1)
    log.debug('found juju')

    if not is_command_installed('lnav'):
        print('''Please install lnav with

sudo snap install lnav

or

sudo apt install lnav

And rerun this script.''')
        sys.exit(1)
    log.debug("found lnav")
