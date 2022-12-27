from flask import Flask
from flask_restful import Api

import cavity_service
import eye_disease_service
import model_administration
import reception_service
import skin_cancer_service

from cavity_service.CavityServer import CavityServer
from model_administration import ModelAdministrationServer
from skin_cancer_service.SkinCancerServer import SkinCancerServer

from . import PORT

app = Flask(__name__)
api = Api(app)

api.add_resource(CavityServer, cavity_service.ENDPOINT)
api.add_resource(ModelAdministrationServer, model_administration.ENDPOINT)
api.add_resource(SkinCancerServer, skin_cancer_service.ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
