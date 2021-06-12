import os
import urllib.request
import urllib.error

from pytest_simplehttpserver.simplehttpserver import http_server_process

file_dir = os.path.abspath(os.path.join(__file__, os.pardir))


def test_server():
    test_dir = os.path.join(file_dir, 'datadir')
    proc = http_server_process(test_dir)

    try:
        response = urllib.request.urlopen('http://localhost:8000/')
        content = response.read().decode()

        assert response.status == 200
        assert len(content) > 0

    except urllib.error.HTTPError:
        pass

    finally:
        proc.terminate()
        proc.wait(5)

