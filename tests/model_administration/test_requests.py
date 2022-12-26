import pytest
import requests
from typing import Tuple

from model_administration import LOCALHOST, MODEL_TO_ENDPOINT, MODELS
from model_administration.ModelAdministrationServer import ModelAdministration

from tests.cavity_service.images.examples import CAVITY, NO_CAVITY
from tests.eye_disease_service.images.examples import (
    EYE_DISEASE,
    NO_EYE_DISEASE,
)
from tests.skin_cancer_service.images.examples import (
    SKIN_CANCER,
    NO_SKIN_CANCER,
)


@pytest.fixture()
def admin() -> ModelAdministration:
    return ModelAdministration()


@pytest.mark.parametrize(
    ["model", "image"],
    MODELS,
    [
        (SKIN_CANCER, NO_SKIN_CANCER),
        (EYE_DISEASE, NO_EYE_DISEASE),
        (CAVITY, NO_CAVITY),
    ],
)
def test_valid_request(
    admin: ModelAdministration, images: Tuple[str], model: str
):
    url = admin.get_url_from_model(model)
    assert url == LOCALHOST + MODEL_TO_ENDPOINT[model]

    for image in images:
        response = requests.get(url, {"image": image})

        assert response.status_code == 200
