from unittest.mock import patch

from jujulnav.main import is_command_installed
from jujulnav.main import parse_commandline
import sys


def test_is_command_installed_found():
    with patch('shutil.which', return_value='/usr/bin/juju'):
        assert is_command_installed('juju') is True


def test_is_command_installed_not_found():
    with patch('shutil.which', return_value=None):
        assert is_command_installed('nonexistentcommand') is False


def test_parse_commandline_single_unit():
    test_args = ["script_name", "unit1:logfile1"]
    sys.argv = test_args
    args = parse_commandline()
    assert args.unit == ["unit1:logfile1"]
    assert args.debug is False


def test_parse_commandline_multiple_units():
    test_args = ["script_name", "unit1:logfile1", "unit2:logfile2"]
    sys.argv = test_args
    args = parse_commandline()
    assert args.unit == ["unit1:logfile1", "unit2:logfile2"]
    assert args.debug is False


def test_parse_commandline_with_debug():
    test_args = ["script_name", "unit1:logfile1", "--debug"]
    sys.argv = test_args
    args = parse_commandline()
    assert args.unit == ["unit1:logfile1"]
    assert args.debug is True
