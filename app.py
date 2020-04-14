from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api.VersionAPI import Version
from api.InfectionAPI import Infection, Countries

API_PREFIX = "/v1"

app = Flask(__name__)
CORS(app)
api = Api(app=app, prefix=API_PREFIX)

api.add_resource(Version, Version.ENDPOINT)
api.add_resource(Infection, Infection.ENDPOINT)
api.add_resource(Countries, Countries.ENDPOINT)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
