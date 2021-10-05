from twilio.rest import Client
from data_manager import *
import os


class FlightData:
    def __init__(self):
        check_max_willing_price = DataManager()
        account_sid = "ACfa81d7fef4810e74f372a5883dce84b2"
        auth_token = "578b071889b665226d8328cdf7937b27"
        flight_search = FlightSearch()
        flight_data = flight_search.data["data"]
        for data in flight_data:
            if data["price"] < int(check_max_willing_price.max_willing_price):
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body=f"Low price alert! Only ${data['price']} to fly from "
                         f"{flight_search.return_from_city_name()}-{flight_search.return_from_city()} "
                         f"to {flight_search.return_to_city_name()}-{flight_search.return_to_city()}, "
                         f"on {flight_search.date_from}",
                    from_="+17039977843",
                    to="+15623878344"
                )
                break
