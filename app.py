from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api.VersionAPI import Version
from api.InfectionAPI import InfectionConfirmedPerMillion, InfectionDeathsPerMillion, Countries, InfectionDataRaw, \
    InfectionRecoveredPerMillion, InfectionConfirmed, InfectionDeaths, InfectionRecovered, InfectionCountry,\
    InfectionDailyConfirmed, InfectionDailyDeaths, InfectionDailyRecovered

API_PREFIX = "/v1"

app = Flask(__name__)
CORS(app)
api = Api(app=app, prefix=API_PREFIX)

api.add_resource(Version, Version.ENDPOINT)

api.add_resource(InfectionConfirmedPerMillion, InfectionConfirmedPerMillion.ENDPOINT)
api.add_resource(InfectionDeathsPerMillion, InfectionDeathsPerMillion.ENDPOINT)
api.add_resource(InfectionRecoveredPerMillion, InfectionRecoveredPerMillion.ENDPOINT)

api.add_resource(InfectionConfirmed, InfectionConfirmed.ENDPOINT)
api.add_resource(InfectionDeaths, InfectionDeaths.ENDPOINT)
api.add_resource(InfectionRecovered, InfectionRecovered.ENDPOINT)

api.add_resource(InfectionCountry, InfectionCountry.ENDPOINT)

api.add_resource(InfectionDailyConfirmed, InfectionDailyConfirmed.ENDPOINT)
api.add_resource(InfectionDailyDeaths, InfectionDailyDeaths.ENDPOINT)
api.add_resource(InfectionDailyRecovered, InfectionDailyRecovered.ENDPOINT)

api.add_resource(Countries, Countries.ENDPOINT)
api.add_resource(InfectionDataRaw, InfectionDataRaw.ENDPOINT)

if __name__ == "__main__":
    app.run(debug=True, port=5010)
