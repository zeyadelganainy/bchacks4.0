import pytest
import requests

BASE = "http://localhost"
PORT = 5000
ENDPOINT = "/admin"

BASE_URL = BASE + ":" + str(PORT)
ENDPOINT_URL = BASE_URL + ENDPOINT

model = "cavity"
IMAGE = """
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
JwAAAABJRU5ErkJggg=="""

params = {"image": IMAGE, "model": model}
headers = {"Content-type": "application/json"}
response = requests.get(ENDPOINT_URL, params=params, headers=headers)
print(response.json())


@pytest.mark.parameterize(["image"], [IMAGE])
def test_image(image):
    params = {"image": image}
    response = requests.get(ENDPOINT_URL, params=params)
    print(response.json())
