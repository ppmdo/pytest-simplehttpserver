import os
import urllib.request


def test_pytest_plugin(testdir):
    """Make sure that our plugin works."""

    # create a temporary conftest.py file
    testdir.makeconftest(
        """
        import pytest
        """
    )

    # create a temporary pytest test file
    testdir.makepyfile(
        """
        import urllib
        
        def test_server_ok(simplehttpserver):
            response = urllib.request.urlopen('http://localhost:8000/')
            content = response.read().decode()
            assert response.status == 200
            assert len(content) > 0
    """
    )

    # run all tests with pytest
    file_dir, _ = os.path.split(__file__)

    result = testdir.runpytest(
        '--simplehttpserver-directory=' + os.path.join(file_dir, 'datadir')
    )

    # check that all tests passed
    result.assert_outcomes(passed=1)


def test_pytest_plugin_fail(testdir):
    """Make sure that our plugin fails if the required options are not passed."""

    # create a temporary conftest.py file
    testdir.makeconftest(
        """
        import pytest
        """
    )

    # create a temporary pytest test file
    testdir.makepyfile(
        """
        import urllib
        import pytest
        
        def test_server_ok(simplehttpserver):
            response = urllib.request.urlopen('http://localhost:8000/')
            content = response.read().decode()
            assert response.status == 200
            assert len(content) > 0
    """
    )

    # run all tests with pytest
    file_dir, _ = os.path.split(__file__)

    result = testdir.runpytest()

    # check that all tests passed
    result.assert_outcomes(errors=1)


def test_dummy(simplehttpserver):
    pass
