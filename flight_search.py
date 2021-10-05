import requests
from IATA import IATACode
from datetime import *
import os
iata = IATACode()

apikey = os.environ.get("apikey")


class FlightSearch:
    def __init__(self):
        global iata

        self.to_city = iata.return_to_city()
        self.from_city = iata.return_from_city()
        self.date = datetime.now()
        self.date_from = self.date.strftime("%d/%m/%Y")
        flight_search_url = "http://tequila-api.kiwi.com/aggregation_search/price_per_date"
        flight_search_parameters = {
            "fly_from": self.from_city,
            "fly_to": self.to_city,
            "date_from": self.date_from
        }

        flight_search_header = {
            "apikey": apikey
        }

        flight_search_response = requests.post(url=f"{flight_search_url}", headers=flight_search_header,
                                               params=flight_search_parameters)
        self.data = flight_search_response.json()

    def return_from_city(self):
        return self.from_city

    def return_to_city(self):
        return self.to_city

    def return_last_checked_date(self) -> str:
        return self.date_from

    def return_to_city_name(self) -> str:
        global iata
        return iata.city_to

    def return_from_city_name(self) -> str:
        global iata
        return iata.city_from
