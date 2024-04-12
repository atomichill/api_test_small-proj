import pytest
import requests


def test_get(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200
