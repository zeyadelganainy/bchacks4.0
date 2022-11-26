from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

skin_cancer_put_args = reqparse.RequestParser()

class SkinCancerServer(Resource):
    def put(self):
        args = skin_cancer_put_args.parse_args()
        return args, 200

api.add_resource(SkinCancerServer, "/skin-cancer")

if __name__ == "__main__":
	app.run(debug=True)

