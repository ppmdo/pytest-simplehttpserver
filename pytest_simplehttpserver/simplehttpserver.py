from __future__ import annotations

from typing import *

import time
import pytest
from subprocess import Popen, PIPE


def read_status(buff: IO, index=100) -> str:
    """
    Read an IO buffer until finding a new line, getting an empty string or until index is 0.
    """
    if index == 0:
        return ""
    else:
        char = buff.read(1)
        if char in ["\n", ""]:
            return ""
        else:
            return char + read_status(buff, index-1)


def _simplehttpserver(directory) -> Popen:
    """
    Call python's http.server module as a child process, wait for initialization and yield server for tests.
    """

    server = Popen(['python', '-m', 'http.server', '--directory', directory],
                   stdout=PIPE,
                   encoding='utf-8',
                   universal_newlines=True)

    retries = 3
    while retries > 0:
        status = read_status(server.stdout)
        if 'Serving' in status:
            break
        else:
            time.sleep(0.1)
            retries -= 1

    return server


@pytest.fixture
def simplehttpserver(request):
    directory = request.config.getoption('simplehttpserver_directory')
    server = _simplehttpserver(directory)

    yield server

    server.terminate()
    server.wait()


def pytest_addoption(parser):
    group = parser.getgroup('simplehttpserver')
    group.addoption(
        '--simplehttpserver-directory',
        action='store',
        dest='simplehttpserver_directory',
        required=True,
        help='Path to the directory containing the root (index.html) file to serve.'
    )

    parser.addini('SIMPLEHTTPSERVER_DIRECTORY', 'Directory containing the root (index.html) file to serve.')
