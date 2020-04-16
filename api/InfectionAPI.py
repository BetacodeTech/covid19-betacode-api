from flask_restful import Resource, reqparse
from services.InfectionService import InfectionService


class Countries(Resource):

    ENDPOINT = "/countries"

    def __init__(self):
        self.infection_service = InfectionService()

    def get(self):
        return self.infection_service.get_list_of_countries()


class InfectionConfirmedPerMillion(Resource):

    ENDPOINT = "/infection/confirmed/per_million"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):

        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_countries_chart_data(countries=countries)


class InfectionDeathsPerMillion(Resource):

    ENDPOINT = "/infection/deaths/per_million"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):

        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_countries_chart_data(countries=countries, key_data=InfectionService.DEATHS_CASES_PER_MILLION)
