import requests
import csv
from models.InfectionData import InfectionData


class InfectionService:

    CONFIRMED = "confirmed"
    DEATHS = "deaths"
    RECOVERED = "recovered"
    DAY = "day"
    DATE = "date"
    CONFIRMED_CASES_PER_MILLION = "confirmed_cases_per_million"
    DEATHS_CASES_PER_MILLION = "deaths_cases_per_million"
    RECOVERED_CASES_PER_MILLION = "recovered_cases_per_million"

    def get_infection_data_for_the_countries(self, countries):

        countries_data = {}

        for country in countries:
            if country:
                countries_data[country] = self.get_infection_data_for_the_country(country)

        return countries_data

    def get_infection_data_for_the_country(self, country):

        population_data = self.get_population_data()

        r = requests.get(f"https://covidapi.info/api/v1/country/{country}")

        response = r.json()

        current_day = 1
        infection_data_list = []
        previous_confirmed = 0
        previous_deaths = 0
        previous_recovered = 0

        for date in response["result"]:

            data = response["result"][date]

            confirmed = data[InfectionService.CONFIRMED]
            deaths = data[InfectionService.DEATHS]
            recovered = data[InfectionService.RECOVERED]
            population = population_data[country]
            daily_confirmed = confirmed - previous_confirmed
            daily_deaths = deaths - previous_deaths
            daily_recovered = recovered - previous_recovered

            previous_confirmed = confirmed
            previous_deaths = deaths
            previous_recovered = recovered


            # infected - total
            # x - 1 000 000

            # x = infect * 1 000 000 / total

            if confirmed is 0 and deaths is 0 and recovered is 0:
                continue
            else:
                infection_data = {
                    "name": population["name"],
                    "date": date,
                    "day": ""+str(current_day),
                    "confirmed": confirmed,
                    "deaths": deaths,
                    "recovered": recovered,
                    "confirmed_cases_per_million": round((confirmed * 1000000) / population["value"], 2),
                    "deaths_cases_per_million": round((deaths * 1000000) / population["value"], 2),
                    "recovered_cases_per_million": round((recovered * 1000000) / population["value"], 2),
                    "daily_confirmed": daily_confirmed,
                    "daily_deaths": daily_deaths,
                    "daily_recovered": daily_recovered
                }
                infection_data_list.append(infection_data)
                current_day += 1

        return infection_data_list

    def get_country_chart_data(self, countries):
        country_chart_data = {}
        for country in countries:
            if country:
                country_data = self.get_infection_data_for_the_country(country)

                chart_data = {
                    "data": []
                }

                for day_data in country_data:
                    day = day_data[InfectionService.DAY]
                    date = day_data[InfectionService.DATE]

                    recovered = day_data[InfectionService.RECOVERED]
                    deaths = day_data[InfectionService.DEATHS]
                    confirmed = day_data[InfectionService.CONFIRMED]

                    recovered_per_million = day_data[InfectionService.RECOVERED_CASES_PER_MILLION]
                    death_per_million = day_data[InfectionService.DEATHS_CASES_PER_MILLION]
                    confirmed_per_million = day_data[InfectionService.CONFIRMED_CASES_PER_MILLION]

                    chart_data["data"].append({
                        "day": day,
                        "date": date,
                        "recovered":recovered,
                        "deaths": deaths,
                        "confirmed": confirmed,
                        "recovered_per_million": recovered_per_million,
                        "death_per_million": death_per_million,
                        "confirmed_per_million": confirmed_per_million
                    })
                    country_chart_data[country] = chart_data

        return country_chart_data

    def get_countries_chart_data(self, countries, key_data=CONFIRMED_CASES_PER_MILLION):

        infection_data = {}

        for country in countries:
            if country:
                country_data = self.get_infection_data_for_the_country(country)

                for day_data in country_data:
                    day = day_data[InfectionService.DAY]
                    data = day_data[key_data]

                    if day not in infection_data:
                        infection_data[day] = {
                            country: data
                        }
                    else:
                        infection_data[day][country] = data

        chart_data = []

        for day in infection_data:
            day_data = infection_data[day]
            chart_data_entry = {
                "day": day
            }

            for country in day_data.keys():
                country_value = day_data[country]
                chart_data_entry[country] = country_value
            chart_data.append(chart_data_entry)

        return {
            "data": chart_data,
            "countries": countries
        }

    def get_list_of_countries(self):
        countries = []

        with open('./data/population.csv') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")

            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    line_count += 1
                    country = row[0]
                    country_iso = row[1]
                    year = int(row[2])
                    value = float(row[3])

                    country_entry = {
                        "value": country_iso,
                        "label": country,
                        "color": "#000"
                    }

                    if country_entry not in countries:
                        countries.append(country_entry)

            return countries

    def get_population_data(self):

        population_dict = {}

        with open('../data/population.csv') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")

            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    line_count += 1
                    country = row[0]
                    country_iso = row[1]
                    year = int(row[2])
                    value = float(row[3])

                    if country_iso in population_dict:
                        if year > population_dict[country_iso]["year"]:
                            population_dict[country_iso] = {
                                "year": year,
                                "value": value,
                                "name": country
                            }
                        else:
                            continue
                    else:
                        population_dict[country_iso] = {
                            "year": year,
                            "value": value,
                            "name": country
                        }

            return population_dict