from flask import Flask
from flask_restful import Api

from reception import ENDPOINT, PORT
from reception.ReceptionServer import ReceptionServer

app = Flask(__name__)
api = Api(app)

api.add_resource(ReceptionServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
