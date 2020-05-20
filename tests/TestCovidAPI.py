import unittest
import requests

from services.InfectionService import InfectionService


class TestCovidAPI(unittest.TestCase):

    def setUp(self):
        self.infection_service = InfectionService()

    def tearDown(self):
        pass

    def testAPIAcess(self):
        r = requests.get('https://covidapi.info/api/v1/global')

        self.assertEqual(r.status_code, 200)

    def testGetPortugueseData(self):
        r = requests.get("https://covidapi.info/api/v1/country/PRT")

        data = r.json()

        self.assertEqual(r.status_code, 200)

    def testGetInfectionData(self):
        r = requests.get("https://covidapi.info/api/v1/country/PRT")
        data = r.json()

        count = data["count"]

        infection_data = self.infection_service.get_infection_data_for_the_country("PRT")

        for i in range(1, len(infection_data)):
            self.assertEqual(infection_data[i]["daily_confirmed"],
                             infection_data[i][InfectionService.CONFIRMED] -
                             infection_data[i - 1][InfectionService.CONFIRMED])

            self.assertEqual(infection_data[0]["daily_confirmed"], infection_data[0][InfectionService.CONFIRMED])

            self.assertGreaterEqual(infection_data[0][InfectionService.CONFIRMED], 0)

            self.assertEqual(infection_data[i]["daily_deaths"],
                             infection_data[i][InfectionService.DEATHS] -
                             infection_data[i - 1][InfectionService.DEATHS])

            self.assertEqual(infection_data[0]["daily_deaths"], infection_data[0][InfectionService.DEATHS])

            self.assertEqual(infection_data[i]["daily_recovered"],
                             infection_data[i][InfectionService.RECOVERED] -
                             infection_data[i - 1][InfectionService.RECOVERED])

            self.assertEqual(infection_data[0]["daily_recovered"], infection_data[0][InfectionService.RECOVERED])

        self.assertNotEqual(len(infection_data), count)
        self.assertGreater(infection_data[0][InfectionService.CONFIRMED], 0)

    def testGetCountriesChartData(self):
        infection_data = self.infection_service.get_countries_chart_data(countries=["PRT", "IND"])

        self.assertEqual(len(infection_data["countries"]), 2)
        self.assertGreater(infection_data["data"][0]["PRT"], 0)
        self.assertGreater(infection_data["data"][0]["IND"], 0)
