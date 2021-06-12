from subprocess import Popen

import pytest

from pytest_simplehttpserver.simplehttpserver import http_server_process


@pytest.fixture
def simplehttpserver(request):
    directory: str = request.config.getoption('simplehttpserver_directory')

    if directory is None:
        raise TypeError('The following pytest arguments are required: --simplehttpserver-directory')
    server_process: Popen = http_server_process(directory)

    yield server_process

    server_process.terminate()
    server_process.wait()


def pytest_addoption(parser):
    group = parser.getgroup('simplehttpserver')
    group.addoption(
        '--simplehttpserver-directory',
        action='store',
        dest='simplehttpserver_directory',
        required=False,
        help='Path to the directory containing the root (index.html) file to serve.'
    )

    parser.addini('SIMPLEHTTPSERVER_DIRECTORY', 'Directory containing the root (index.html) file to serve.')
