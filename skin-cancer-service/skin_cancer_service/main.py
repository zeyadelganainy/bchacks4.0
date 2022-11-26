from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from . import SkinCancerModel

app = Flask(__name__)
api = Api(app)

skin_cancer_model = SkinCancerModel()

skin_cancer_put_args = reqparse.RequestParser()

args_dict = {
	'image': fields.String,
}


class SkinCancerServer(Resource):
    @marshal_with(args_dict)
    def get(self):
        args = skin_cancer_put_args.parse_args()
        img: str = args['image']
        cancer = skin_cancer_model.get_cancer(img)
        return cancer, 200


api.add_resource(SkinCancerServer, "/skin-cancer")

if __name__ == "__main__":
    app.run(debug=True)
