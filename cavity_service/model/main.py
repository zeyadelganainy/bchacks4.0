from flask import Flask
from flask_restful import Api

from cavity_service.model.CavityServer import CavityServer

app = Flask(__name__)
api = Api(app)

ENDPOINT = "/cavity"
PORT = 5003

api.add_resource(CavityServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
