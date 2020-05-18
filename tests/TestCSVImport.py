import unittest
import csv

from services.InfectionService import InfectionService


class TestCSVPopulation(unittest.TestCase):

    def setUp(self):
        self.infection_service = InfectionService()

    def tearDown(self):
        pass

    def testParseCSVFIle(self):

        with open('./data/population.csv') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")

            self.assertIsNotNone(csv_reader)

    def testParseCountriesFile(self):

        population_data = self.infection_service.get_population_data()

        self.assertIsNotNone(population_data)
        self.assertEqual(population_data["PRT"]["value"], 10324611)
        self.assertEqual(population_data["PRT"]["year"], 2016)

    def testGetListOfCountries(self):

        countries = self.infection_service.get_list_of_countries()

        self.assertIsNotNone(countries)
