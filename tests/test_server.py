import requests
from simplehttpserver import simplehttpserver


def test_correct(simplehttpserver):
    response = requests.get('http://localhost:8000')
    assert response.status_code == 200
