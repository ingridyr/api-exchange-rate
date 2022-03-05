import os
import requests
from http import HTTPStatus

base_url = os.getenv("REQUEST")

def list_all_conversions(currency):

    data = requests.get(f'http://{base_url}latest/{currency}').json()
    result = {}
    
    for item in data["conversion_rates"].items():
        if item[0] != currency:
            result[item[0]] = item[1]
            
    return {
        currency : 1,
        "all_conversions" : result
        }, HTTPStatus.OK

def currency_rate(currency_to_convert, currency_to_be_converted):
    data = requests.get(f'http://{base_url}pair/{currency_to_convert}/{currency_to_be_converted}').json()

    return {
        "currencies" : f"{currency_to_convert} to {currency_to_be_converted}",
        "currency_conversion_rate" : data["conversion_rate"]
        }, HTTPStatus.OK