import requests
from pytest_simplehttpserver.simplehttpserver import _simplehttpserver


def test_server():
    proc = _simplehttpserver('datadir')
    response = requests.get('http://localhost:8000')
    assert response.status_code == 200
    proc.terminate()
    proc.wait(5)


def test_hello(testdir):
    """Make sure that our plugin works."""

    # create a temporary conftest.py file
    testdir.makeconftest(
        """
        import pytest

        @pytest.fixture(params=[
            "Brianna",
        ])
        def name(request):
            return request.param
    """
    )

    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_server_ok(simplehttpserver):
            assert simplehttpserver

    """
    )

    # run all tests with pytest
    result = testdir.runpytest(
        '--simplehttpserver-directory=datadir'
    )

    # check that all 4 tests passed
    result.assert_outcomes(passed=1)