import requests

from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/model-administration"
PORT = 5000

skin_cancer_put_args = reqparse.RequestParser()

args_dict = {
    "model": fields.String,
    "image": fields.String,
}


class ModelAdministration(Resource):

    MODEL_TO_ENDPOINT = {
        "eye-disease": "/a-eye",
        "cavity": "/cavity",
        "skin-cancer": "/skin-cancer"
    }

    @marshal_with(args_dict)
    def get(self):
        args = skin_cancer_put_args.parse_args()
        model: str = args["model"]
        img: str = args["image"]

        if model not in self.MODEL_TO_ENDPOINT:
            return "invalid model", 404

        url = self.MODEL_TO_ENDPOINT[model]
        response = requests.get(
            url, {"image": img}
        )

        return response, 200


api.add_resource(ModelAdministration, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
