import requests

from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/admin"
PORT = 5000

model_arg = "model"
image_arg = "image"
admin_get_args = reqparse.RequestParser()
admin_get_args.add_argument(model_arg)
admin_get_args.add_argument(image_arg)


class ModelAdministration(Resource):

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

    def get(self):
        args = admin_get_args.parse_args()
        model: str = args[model_arg]
        img: str = args[image_arg]

        if model not in self.MODEL_TO_ENDPOINT:
            return "invalid model", 404
        
        port = self.MODEL_TO_PORT[model]
        endpoint = self.MODEL_TO_ENDPOINT[model]

        url = "http://127.0.0.1" + ":" + port + endpoint
        response = requests.get(
            url, {"image": img}
        )

        return response, 200


api.add_resource(ModelAdministration, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
