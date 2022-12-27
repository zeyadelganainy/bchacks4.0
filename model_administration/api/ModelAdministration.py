from model_administration.api import LOCALHOST, MODEL_TO_ENDPOINT


class ModelAdministration:
    def is_valid_model(model) -> bool:
        return model in MODEL_TO_ENDPOINT

    def get_url_from_model(self, model: str) -> str:
        # port = MODEL_TO_PORT[model]
        endpoint = MODEL_TO_ENDPOINT[model]
        # url = LOCALHOST + ":" + port + endpoint
        url = LOCALHOST + endpoint
        return url
