from flask import Flask
from flask_restful import Api

from skin_cancer_service.model.SkinCancerServer import SkinCancerServer

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/skin-cancer"
PORT = 5001

api.add_resource(SkinCancerServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
