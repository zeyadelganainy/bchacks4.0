from flask import Flask
from flask_restful import Api

from reception_service import ENDPOINT, PORT
from reception_service.model.ReceptionServer import ReceptionServer

app = Flask(__name__)
api = Api(app)

api.add_resource(ReceptionServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)