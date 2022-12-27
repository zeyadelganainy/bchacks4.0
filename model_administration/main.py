from flask import Flask
from flask_restful import Api

from model_administration import ENDPOINT, PORT
from model_administration.ModelAdministrationServer import (
    ModelAdministrationServer,
)

app = Flask(__name__)
api = Api(app)

api.add_resource(ModelAdministrationServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
