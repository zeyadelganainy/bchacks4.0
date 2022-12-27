from flask import Flask
from flask_restful import Api

from administration import ENDPOINT, PORT
from administration.AdministrationServer import AdministrationServer

app = Flask(__name__)
api = Api(app)

api.add_resource(AdministrationServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
