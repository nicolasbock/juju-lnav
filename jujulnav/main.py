"""
Main entry point for the juju-lnav script.
"""

import argparse
import shutil
import sys


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


def is_lnav_installed() -> bool:
    """
    Try to find lnav.

    Returns:
        bool: Whether lnav is installed.
    """
    return shutil.which('lnav') is not None


def main():
    """
    Main entry point.
    """

    if not is_lnav_installed():
        print('''Please install lnav with

sudo snap install lnav

or

sudo apt install lnav

And rerun this script.''')
        sys.exit(1)

    _ = parse_commandline()
