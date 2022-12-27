import requests

from flask_restful import Resource, reqparse

from administration.api.Administration import Administration


model_arg = "model"
image_arg = "image"
admin_get_args = reqparse.RequestParser()
admin_get_args.add_argument(model_arg)
admin_get_args.add_argument(image_arg)

admin = Administration()


class AdministrationServer(Resource):
    def get(self):
        args = admin_get_args.parse_args()
        model: str = args[model_arg]
        img: str = args[image_arg]

        if admin.is_valid_model(model):
            url = admin.get_url_from_model(model)
        else:
            return "invalid model", 404

        response = requests.get(url, {image_arg: img})

        return response, 200
