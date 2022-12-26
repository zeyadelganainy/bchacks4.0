import base64
import io

from flask_restful import Resource, reqparse
from PIL import Image

from cavity_service import NEW_MODEL
from cavity_service.model.CavityModel import CavityModel


cavity_model = CavityModel(NEW_MODEL)

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
