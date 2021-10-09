import json
import csv

with open('covid_cases.json'. 'r') as json_file:
    covid_json = json.load(json_file)

with open('parsed_covid_cases.csv', 'w') as covid_write:
    file = csv.writer(covid_write)
    file.writerow(["dateRep","countriesAndTerritories", "cases", "deaths"])

    for parsing in covid_json['records']:
        file.writerow([parsing['dateRep'],parsing['countriesAndTerritories'],parsing['cases'],parsing['deaths']])