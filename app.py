from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api.VersionAPI import Version
from api.InfectionAPI import InfectionConfirmedPerMillion, InfectionDeathsPerMillion, Countries, InfectionDataRaw

API_PREFIX = "/v1"

app = Flask(__name__)
CORS(app)
api = Api(app=app, prefix=API_PREFIX)

api.add_resource(Version, Version.ENDPOINT)
api.add_resource(InfectionConfirmedPerMillion, InfectionConfirmedPerMillion.ENDPOINT)
api.add_resource(InfectionDeathsPerMillion, InfectionDeathsPerMillion.ENDPOINT)
api.add_resource(Countries, Countries.ENDPOINT)
api.add_resource(InfectionDataRaw, InfectionDataRaw.ENDPOINT)

if __name__ == "__main__":
    app.run(debug=True, port=5010)
