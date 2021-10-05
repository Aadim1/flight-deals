import requests
import html_to_json


class NotificationManager:
    airport_codes_url = "https://www.air-port-codes.com/api/v1/multi"

    airport_codes_header = {
        "APC-Auth": "efbc336f17",
        "APC-Auth-Secret": "7417465e1612e8d"
    }
    airport_codes_parameters = {
        "term": "Los Angeles"
    }

    airport_code_response = requests.post(url=f"{airport_codes_url}", data=airport_codes_parameters,
                                          headers=airport_codes_header)
    # try:
    # data = airport_code_response.json()
    # except:
    data = html_to_json.convert(airport_code_response.text)
    print(data)
