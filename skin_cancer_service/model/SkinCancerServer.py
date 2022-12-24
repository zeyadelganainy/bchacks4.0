import base64
import io

from flask_restful import Resource, reqparse
from PIL import Image

from SkinCancerModel import SkinCancerModel


skin_cancer_model = SkinCancerModel()

image_arg = "image"
skin_cancer_get_args = reqparse.RequestParser()
skin_cancer_get_args.add_argument(image_arg)


def get_image_from_image_str(image_str: str) -> Image:
    imgdata = base64.b64decode(image_str)
    img = Image.open(io.BytesIO(imgdata))
    return img


class SkinCancerServer(Resource):
    def get(self):
        args = skin_cancer_get_args.parse_args()
        img_str: str = args[image_arg]
        img = get_image_from_image_str(img_str)
        cancer = skin_cancer_model.get_skin_cancer(img)
        return cancer, 200
