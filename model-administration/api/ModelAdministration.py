import requests

from flask_restful import Resource, reqparse

from api import LOCALHOST, MODEL_TO_ENDPOINT


model_arg = "model"
image_arg = "image"
admin_get_args = reqparse.RequestParser()
admin_get_args.add_argument(model_arg)
admin_get_args.add_argument(image_arg)


class ModelAdministration(Resource):
    def get_url_from_model(self, model: str) -> str:
        # port = MODEL_TO_PORT[model]
        endpoint = MODEL_TO_ENDPOINT[model]

        # url = LOCALHOST + ":" + port + endpoint
        url = LOCALHOST + endpoint
        return url

    def get(self):
        args = admin_get_args.parse_args()
        model: str = args[model_arg]
        img: str = args[image_arg]

        if model not in MODEL_TO_ENDPOINT:
            return "invalid model", 404

        url = self.get_url_from_model(model)

        response = requests.get(url, {image_arg: img})

        return response, 200
