import pytest
import requests
import cerberus


def test_get_all_breeds(base_url):
    r = requests.get(base_url + "/breeds/list/all")

    assert r.status_code == 200


def test_get_rnd_img(base_url):
    r = requests.get(base_url + "/breeds/image/random")
    v = cerberus.Validator()

    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }

    assert r.status_code == 200
    assert v.validate(r.json(), schema)


@pytest.mark.parametrize("breed", ["hound", "beagle", "bouvier", "borzoi"])
def test_get_imgs_breed(base_url,breed):

    r = requests.get(base_url + "/breed/" + breed + "/images")

    assert r.status_code == 200


@pytest.mark.parametrize("breed", ["hound", "beagle", "bouvier", "borzoi"])
def test_get_rnd_img_breed(base_url, breed):
    r = requests.get(base_url + "/breed/" + breed + "/images" + "/random")
    v = cerberus.Validator()

    scheme = {
            "message": {"type": "string"},
            "status": {"type":"string"}
    }

    assert r.status_code == 200
    assert v.validate(r.json(),scheme)

@pytest.mark.parametrize("breed", ["hound", "beagle", "bouvier", "borzoi"])
def test_get_subbreed(base_url, breed):
    r = requests.get(base_url + "/breed/" + breed + "/list")

    assert r.status_code == 200

