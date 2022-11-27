import base64
import io

from flask import Flask
from flask_restful import Api, Resource, reqparse
from CavityModel import CavityModel

from PIL import Image

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/cavity"
PORT = 5003

cavity_model = CavityModel()

image_arg = "image"

cavity_get_args = reqparse.RequestParser()
cavity_get_args.add_argument(image_arg)


class CavityServer(Resource):
    def get(self):
        args = cavity_get_args.parse_args()
        img: str = args[image_arg]
        imgdata = base64.b64decode(img)
        img = Image.open(io.BytesIO(imgdata))
        is_cavity = cavity_model.get_is_cavity(img)
        return is_cavity, 200


api.add_resource(CavityServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
