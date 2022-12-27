import base64
import io

from flask_restful import Resource
from PIL import Image


class ImageClassificationServer(Resource):
    def get_image_from_image_str(self, image_str: str) -> Image:
        imgdata = base64.b64decode(image_str)
        img = Image.open(io.BytesIO(imgdata))
        return img
