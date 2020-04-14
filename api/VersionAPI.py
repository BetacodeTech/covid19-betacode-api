from flask_restful import Resource

class Version(Resource):

    ENDPOINT = "/version"

    def get(self):
        return "Covid19 API @Betacode Version: 1"
