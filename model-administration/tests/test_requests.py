import pytest
import requests

from ..api.Model import MODEL_TO_ENDPOINT, MODEL_TO_PORT
from image import IMAGE

LOCALHOST = "http://127.0.0.1"


pytest.mark.parametrize("model", ["skin-cancer", "eye-disease", "cavity"])


def test_valid_request(model):
    port = MODEL_TO_PORT[model]
    endpoint = MODEL_TO_ENDPOINT[model]
    url = LOCALHOST + ":" + port + endpoint
    response = requests.get(url, params={"model": model, "image": IMAGE})
    assert response is not None
