from flask_restful import reqparse

from ImageClassificationServer import ImageClassificationServer
from optometrist.model.Optometrist import Optometrist


optometrist = Optometrist(new_model=True)

image_arg = "image"
optometrist_get_args = reqparse.RequestParser()
optometrist_get_args.add_argument(image_arg)


class OptometristServer(ImageClassificationServer):
    def get(self):
        args = optometrist_get_args.parse_args()
        img_str: str = args[image_arg]
        img = self.get_image_from_image_str(img_str)
        eye_disease = optometrist.get_eye_disease(img)
        return eye_disease, 200
