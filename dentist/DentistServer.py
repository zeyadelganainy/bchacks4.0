from flask_restful import reqparse
from PIL import Image

from ImageClassificationServer import ImageClassificationServer
from dentist.model.Dentist import Dentist


dentist = Dentist(new_model=False)

image_arg = "image"

dentist_get_args = reqparse.RequestParser()
dentist_get_args.add_argument(image_arg)


class DentistServer(ImageClassificationServer):
    def get(self):
        args = dentist_get_args.parse_args()
        img: str = args[image_arg]
        image: Image = self.get_image_from_image_str(img)
        is_dentist = dentist.is_dentist(image)
        return is_dentist, 200
