import requests
import json


class GetCountryId:
    def __init__(self):
        self.__countries = {}

    def get_id(self, country):
        if country in self.__countries.keys():
            return self.__countries[country]
        try:
            req = requests.get(f"https://restcountries.eu/rest/v2/name/{country}")
            return req.json()[0]['alpha2Code']
        except (json.JSONDecodeError, KeyError) as e:
            return "Country404"
