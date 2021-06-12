# pytest-simplehttpserver

Simple fixture to spin up a simple HTTP server to serve static files for testing.

Can be used for testing web scrapers, etc.

Features
--------

* The fixture spins up a HTTP server that serves static files on port 8000.

Usage
-----

When running your tests you need to point pytest-simplehttpserver to root
directory with the static files you want to serve:


```shell
$ pytest --simplehttpserver-directory /home/user/mock_website/
```

In your code, just pass the fixture to your tests:

```python
import requests

def mytest(simplehttpserver):
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200
```


Installation
------------

You can install "pytest-simplehttpserver" via pip from PyPI:

```shell
$ pip install pytest-simplehttpserver
```

Contributing
------------
Contributions are very welcome. Tests can be run with pytest, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the MIT license, "pytest-simplehttpserver" is free and open source software
