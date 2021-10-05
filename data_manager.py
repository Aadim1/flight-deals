import requests
from flight_search import FlightSearch

import os


class DataManager:
    def __init__(self):
        flight_search = FlightSearch()
        self.max_willing_price = input("What is the maximum amount of price you will be willing to pay? ")
        token = os.environ.get("token")
        sheety_url = "https://api.sheety.co/657254289800d599a73bbb744818c68a/flightPrices/workouts"
        sheety_parameters = {
            "workout":
                {
                    "firstName": input("What is your first name? "),
                    "lastName": input("Now your last name? "),
                    "email": "email",
                    "fromCity": flight_search.return_from_city_name(),
                    "toCity": flight_search.return_to_city_name(),
                    "maxWillingPrice": self.max_willing_price,
                    "lastUpdated": str(flight_search.return_last_checked_date())
                }
        }
        sheety_headers = {
            "Authorization": f"Bearer {token}"
        }

        sheety_response = requests.post(
            url=f"{sheety_url}",
            json=sheety_parameters, headers=sheety_headers)
