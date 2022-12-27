from flask_restful import reqparse

from ImageClassificationServer import ImageClassificationServer
from dermatologist.model.Dermatologist import Dermatologist


dermatologist = Dermatologist(new_model=True)

image_arg = "image"
skin_cancer_get_args = reqparse.RequestParser()
skin_cancer_get_args.add_argument(image_arg)


class DermatologistServer(ImageClassificationServer):
    def get(self):
        args = skin_cancer_get_args.parse_args()
        img_str: str = args[image_arg]
        img = self.get_image_from_image_str(img_str)
        cancer = dermatologist.get_skin_cancer(img)
        return cancer, 200
