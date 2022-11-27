from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from CavityModel import CavityModel

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/cavity"
PORT = 5003

cavity_model = CavityModel()

skin_cancer_put_args = reqparse.RequestParser()

args_dict = {
    "image": fields.String,
}


class CavityServer(Resource):
    @marshal_with(args_dict)
    def get(self):
        args = skin_cancer_put_args.parse_args()
        img: str = args["image"]
        is_cavity = cavity_model.get_is_cavity(img)
        return is_cavity, 200


api.add_resource(CavityServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
