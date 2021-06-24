from subprocess import Popen

import pytest

from pytest_simplehttpserver.simplehttpserver import http_server_process


def determine_scope(fixture_name, config):
    scope = config.getoption("--simplehttpserver-scope", None)
    if scope is None:
        return "function"
    else:
        if scope not in ("function", "class", "module", "package", "session"):
            raise ValueError("--simplehttpserver must be set to one of: function, class, module, package or session.")
        return scope

@pytest.fixture(scope=determine_scope)
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

    group.addoption(
        '--simplehttpserver-scope',
        action='store',
        dest='simplehttpserver_scope',
        required=False,
        default="function",
        help='If using the server for multiple tests, set the scope for "reusage": '
             'function, class, module, package, session'
    )

    parser.addini('SIMPLEHTTPSERVER_DIRECTORY', 'Directory containing the root (index.html) file to serve.')
    parser.addini('SIMPLEHTTPSERVER_SCOPE', 'Scope for server reusage: function, class, module, package, session.')
