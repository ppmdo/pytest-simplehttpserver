=======================
pytest-simplehttpserver
=======================

.. image:: https://img.shields.io/pypi/v/pytest-simplehttpserver.svg
    :target: https://pypi.org/project/pytest-simplehttpserver
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-simplehttpserver.svg
    :target: https://pypi.org/project/pytest-simplehttpserver
    :alt: Python versions

.. image:: https://travis-ci.org/ppmdo/pytest-simplehttpserver.svg?branch=master
    :target: https://travis-ci.org/ppmdo/pytest-simplehttpserver
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/ppmdo/pytest-simplehttpserver?branch=master
    :target: https://ci.appveyor.com/project/ppmdo/pytest-simplehttpserver/branch/master
    :alt: See Build Status on AppVeyor

Simple fixture to spin up an HTTP server to serve static files for testing
---
I needed and easy and practical way to test web scraping functionalities against a real HTTP server.
This is what I came up with.

Features
--------

* The fixture spins up a HTTP server that serves static files on port 8000.


Usage
------------

When running your tests you need to point pytest-simplehttpserver to root
directory with the static files you want to serve:
```
pytest --simplehttpserver-directory /home/user/mock_website/
```

In your code, just pass the fixture to your tests:
```

```

Installation
------------

You can install "pytest-simplehttpserver" via `pip`_ from `PyPI`_::

    $ pip install pytest-simplehttpserver


Usage
-----

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-simplehttpserver" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/ppmdo/pytest-simplehttpserver/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
