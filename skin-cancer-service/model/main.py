from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from SkinCancerModel import SkinCancerModel

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/skin-cancer"
PORT = 5001

skin_cancer_model = SkinCancerModel()

skin_cancer_put_args = reqparse.RequestParser()

args_dict = {
    "image": fields.String,
}


class SkinCancerServer(Resource):
    @marshal_with(args_dict)
    def get(self):
        args = skin_cancer_put_args.parse_args()
        img: str = args["image"]
        cancer = skin_cancer_model.get_skin_cancer(img)
        return cancer, 200


api.add_resource(SkinCancerServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
