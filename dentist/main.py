from flask import Flask
from flask_restful import Api

from dentist import ENDPOINT, PORT
from dentist.DentistServer import DentistServer

app = Flask(__name__)
api = Api(app)

api.add_resource(DentistServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
