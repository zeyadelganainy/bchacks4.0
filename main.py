from flask import Flask
from flask_restful import Api

import dentist
import optometrist
import administration
import reception
import dermatologist

from dentist.DentistServer import DentistServer
from reception.ReceptionServer import ReceptionServer
from optometrist.OptometristServer import OptometristServer
from dermatologist.DermatologistServer import DermatologistServer
from administration.AdministrationServer import AdministrationServer

from . import PORT

app = Flask(__name__)
api = Api(app)

# ML chatbot
api.add_resource(ReceptionServer, reception.ENDPOINT)

# ML model admin
api.add_resource(AdministrationServer, administration.ENDPOINT)

# ML models
api.add_resource(DentistServer, dentist.ENDPOINT)
api.add_resource(DermatologistServer, dermatologist.ENDPOINT)
api.add_resource(OptometristServer, optometrist.ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
