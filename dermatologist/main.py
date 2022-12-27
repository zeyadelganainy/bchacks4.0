from flask import Flask
from flask_restful import Api

from dermatologist import ENDPOINT, PORT
from dermatologist.DermatologistServer import DermatologistServer

app = Flask(__name__)
api = Api(app)

api.add_resource(DermatologistServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
