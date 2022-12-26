from flask import Flask
from flask_restful import Api

from skin_cancer_service import ENDPOINT, PORT
from skin_cancer_service.SkinCancerServer import SkinCancerServer

app = Flask(__name__)
api = Api(app)

api.add_resource(SkinCancerServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
