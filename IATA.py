import requests
import os

airport_codes_url = "https://www.air-port-codes.com/api/v1/multi"

# apcauth = os.environ.get("apcauth")
# apcauthsecret = os.environ.get("apcauthsecret")
airport_codes_header = {
    "APC-Auth": "efbc336f17",
    "APC-Auth-Secret": "7417465e1612e8d"
}


class IATACode:
    global airport_codes_header
    global airport_codes_url

    def __init__(self):
        y = 0
        while y < 2:
            try:
                if y == 0:
                    airport_codes_parameters = {
                        "term": input("Where would you like to go? ")
                    }
                else:
                    airport_codes_parameters = {
                        "term": input("Where are you travelling from? ")
                    }

                airport_code_response = requests.post(url=f"{airport_codes_url}", data=airport_codes_parameters,
                                                      headers=airport_codes_header)
                data = airport_code_response.json()
                if y == 0:
                    self.to_city = data["airports"][0]["iata"]
                    self.city_to = data["airports"][0]["city"]
                else:
                    self.from_city = data["airports"][0]["iata"]
                    self.city_from = data["airports"][0]["city"]
                y += 1
            except KeyError:
                print("Error:\nInvalid city name, check for spelling mistakes and retype again")
                continue

    def return_to_city(self) -> str:
        return self.to_city

    def return_from_city(self) -> str:
        return self.from_city
