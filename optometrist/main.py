from flask import Flask
from flask_restful import Api

from optometrist import ENDPOINT, PORT
from optometrist.OptometristServer import OptometristServer

app = Flask(__name__)
api = Api(app)

api.add_resource(OptometristServer, ENDPOINT)

if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True)
