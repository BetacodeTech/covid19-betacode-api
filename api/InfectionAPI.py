from flask_restful import Resource, reqparse
from services.InfectionService import InfectionService


class Countries(Resource):

    ENDPOINT = "/countries"

    def __init__(self):
        self.infection_service = InfectionService()

    def get(self):
        return self.infection_service.get_list_of_countries()


class InfectionDataRaw(Resource):

    ENDPOINT = "/infection/all"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):
        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_infection_data_for_the_countries(countries=countries)


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


class InfectionRecoveredPerMillion(Resource):
    ENDPOINT = "/infection/recovered/per_million"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):
        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_countries_chart_data(countries=countries,
                                                               key_data=InfectionService.RECOVERED_CASES_PER_MILLION)


class InfectionConfirmed(Resource):

    ENDPOINT = "/infection/confirmed"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):
        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_countries_chart_data(countries=countries,
                                                               key_data=InfectionService.CONFIRMED)


class InfectionDeaths(Resource):

    ENDPOINT = "/infection/deaths"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):
        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_countries_chart_data(countries=countries,
                                                               key_data=InfectionService.DEATHS)


class InfectionRecovered(Resource):

    ENDPOINT = "/infection/recovered"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):
        args = self.reqparse.parse_args()

        countries = args["countries"].split(",")

        return self.infection_service.get_countries_chart_data(countries=countries,
                                                               key_data=InfectionService.RECOVERED)


class InfectionCountry(Resource):

    ENDPOINT = "/infection/chartdata"

    def __init__(self):
        self.infection_service = InfectionService()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("countries", type=str)

    def get(self):
        args = self.reqparse.parse_args()
        countries = args["countries"].split(",")

        return self.infection_service.get_country_chart_data(countries)
