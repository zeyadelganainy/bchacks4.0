LOCALHOST = "http://127.0.0.1"

MODELS = ["dermatologist", "optometrist", "dentist"]

MODEL_TO_PORT = {
    "dermatologist": 5001,
    "optometrist": 5002,
    "dentist": 5003,
}

MODEL_TO_ENDPOINT = {
    "dermatologist": "/dermatologist",
    "optometrist": "/a-eye",
    "dentist": "/dentist",
}
