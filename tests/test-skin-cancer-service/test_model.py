import pytest
import requests

from image import SKIN_CANCER_IMAGE

BASE = "http://localhost"
PORT = 5001
ENDPOINT = "/skin-cancer"

BASE_URL = BASE + ":" + str(PORT)
ENDPOINT_URL = BASE_URL + ENDPOINT


@pytest.mark.parameterize(["image"], [SKIN_CANCER_IMAGE])
def test_image(image):
    headers = {"Content-type": "application/json"}
    params = {"image": image}
    response = requests.get(ENDPOINT_URL, headers=headers, params=params)
    print(response.json())
