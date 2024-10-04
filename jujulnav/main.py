"""
Main entry point for the juju-lnav script.
"""

import argparse
from functools import lru_cache
import json
import logging
import shutil
import subprocess
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
log = logging.getLogger('juju-lnav')


class Status():
    """
    The current status of the Juju model.
    """

    def __init__(self):
        """
        Initialize by fetching the current juju status.
        """
        with subprocess.Popen(['juju', 'status', '--format', 'json'],
                              stdout=subprocess.PIPE) as juju:
            juju.wait()
            self.juju_parsed = json.loads(juju.stdout.read())

    @property
    @lru_cache
    def machine_IPs(self) -> list[tuple[int, list[str]]]:
        """
        Get the IP addresses of all machines in the current model.

        Returns:
            list[tuple[int, list[str]]]: A list of tuples of the form (ID,
            [Address, Address, ...]).
        """
        if 'machines' not in self.juju_parsed:
            return []
        return [(int(machine_id), machine_details['ip-addresses'])
                for machine_id, machine_details
                in self.juju_parsed['machines'].items()]

    @property
    @lru_cache
    def container_IPs(self) -> list[tuple[str, list[str]]]:
        """
        Get the IP addresses of all containers in the current model.

        Returns:
            list[tuple[str, list[str]]]: A list of typles of the form (ID,
            [Address, Address, ...])
        """
        if 'machines' not in self.juju_parsed:
            return []
        return [(container_id, container_details['ip-addresses'])
                for container_id, container_details
                in self.juju_parsed['machines'].items()]

    @property
    @lru_cache
    def unit_IPs(self) -> list[tuple[str, list[str]]]:
        """
        Get the IP addresses of all units in the current model.

        Returns:
            list[tuple[str, list[str]]]: A list of typles of the form (ID,
            [Address, Address, ...])
        """
        if 'units' not in self.juju_parsed:
            return []
        return [(container_id, container_details['ip-addresses'])
                for container_id, container_details
                in self.juju_parsed['units'].items()]


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
        bool: Whether the command is installed.
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

    status = Status()
    print(f'machine addresses:   {status.machine_IPs}')
    print(f'container addresses: {status.container_IPs}')
    print(f'unit addresses:      {status.container_IPs}')
