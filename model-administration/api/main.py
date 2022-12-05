import requests

from flask import Flask
from flask_restful import Api, Resource, reqparse

from Model import MODEL_TO_ENDPOINT, MODEL_TO_PORT

app = Flask(__name__)
api = Api(app)

LOCALHOST = "http://127.0.0.1"
ENDPOINT = "/admin"
PORT = 5000

model_arg = "model"
image_arg = "image"
admin_get_args = reqparse.RequestParser()
admin_get_args.add_argument(model_arg)
admin_get_args.add_argument(image_arg)


class ModelAdministration(Resource):

    def get(self):
        args = admin_get_args.parse_args()
        model: str = args[model_arg]
        img: str = args[image_arg]

        if model not in MODEL_TO_ENDPOINT:
            return "invalid model", 404

        port = MODEL_TO_PORT[model]
        endpoint = MODEL_TO_ENDPOINT[model]

        url = LOCALHOST + ":" + port + endpoint
        response = requests.get(url, params={"model": model, "image": img})

        return response, 200


api.add_resource(ModelAdministration, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
