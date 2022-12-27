from enum import Enum


class Model(Enum):
    SKIN_CANCER = (0,)
    CAVITY = (1,)
    EYE = 2


MODEL_TO_PORT = {
    "dermatologist": "5001",
    "optometrist": "5002",
    "dentist": "5003",
}

MODEL_TO_ENDPOINT = {
    "dermatologist": "/dermatologist",
    "optometrist": "/a-eye",
    "dentist": "/dentist",
}
