import json
from unittest.mock import MagicMock, patch

import pytest

from jujulnav.main import Status


@pytest.fixture
def mock_juju_status():
    with patch('subprocess.Popen') as mock_popen:
        mock_proc = MagicMock()
        with open('artifacts/juju-status.json', encoding='utf-8') as fd:
            mock_proc.stdout.read.return_value = "\n".join(fd.readlines())
        mock_popen.return_value.__enter__.return_value = mock_proc
        yield


def test_machine_IPs(mock_juju_status):
    status = Status()
    assert status.machine_IPs == [
        (0, ['10.149.133.151', '252.46.0.1']),
        (1, ['10.149.133.241', '252.226.0.1']),
        (2, ['10.149.133.164', '252.72.0.1']),
        (3, ['10.149.133.217', '252.178.0.1']),
        (4, ['10.149.133.232', '252.208.0.1']),
    ]


def test_container_IPs(mock_juju_status):
    status = Status()
    assert status.container_IPs == [
        ('0/lxd/0', ['252.47.139.203']),
        ('2/lxd/0', ['252.72.1887.73']),
        ('3/lxd/0', ['252.178.0.1']),
        ('4/lxd/0', ['252.208.0.1']),
    ]


def test_unit_IPs(mock_juju_status):
    status = Status()
    assert status.unit_IPs == [
        ("unit/0", ["10.0.0.3"]),
        ("unit/1", ["10.0.0.4"]),
    ]