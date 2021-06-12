from __future__ import annotations

from typing import *

import time
from http.client import HTTPConnection

from subprocess import Popen, PIPE


def http_server_process(directory: str) -> Popen:
    """
    Call python's http.server module as a child process, wait for initialization and yield server for tests.
    """

    server = Popen(['python', '-m', 'http.server', '--directory', directory],
                   stdout=PIPE,
                   encoding='utf-8',
                   universal_newlines=True)

    retries = 5
    while retries > 0:
        conn = HTTPConnection('localhost:8000')
        try:
            conn.request('HEAD', '/')
            response = conn.getresponse()
            if response is not None:
                return server
        except ConnectionRefusedError:
            time.sleep(0.5)
            retries -= 1

    raise RuntimeError('Failed to start http server')

