import base64
import io

from flask import Flask
from flask_restful import Api, Resource, reqparse
from SkinCancerModel import SkinCancerModel

from PIL import Image

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/skin-cancer"
PORT = 5001

skin_cancer_model = SkinCancerModel()

image_arg = "image"
skin_cancer_get_args = reqparse.RequestParser()
skin_cancer_get_args.add_argument(image_arg)


class SkinCancerServer(Resource):
    def get(self):
        args = skin_cancer_get_args.parse_args()
        img: str = args[image_arg]
        print("hi")
        imgdata = base64.b64decode(img)
        img = Image.open(io.BytesIO(imgdata))
        cancer = skin_cancer_model.get_skin_cancer(img)
        print("hi")
        print(cancer)
        return cancer, 200


api.add_resource(SkinCancerServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
