from enum import Enum


class Model(Enum):
    SKIN_CANCER = (0,)
    CAVITY = (1,)
    EYE = 2


MODEL_TO_PORT = {
    "skin-cancer": "5001",
    "eye-disease": "5002",
    "cavity": "5003",
}

MODEL_TO_ENDPOINT = {
    "skin-cancer": "/skin-cancer",
    "eye-disease": "/a-eye",
    "cavity": "/cavity",
}
