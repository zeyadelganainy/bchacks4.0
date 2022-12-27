from administration.api import LOCALHOST, MODEL_TO_ENDPOINT


class Administration:
    def is_valid_model(model) -> bool:
        return model in MODEL_TO_ENDPOINT

    def get_url_from_model(self, model: str) -> str:
        endpoint = MODEL_TO_ENDPOINT[model]
        url = LOCALHOST + endpoint
        return url
