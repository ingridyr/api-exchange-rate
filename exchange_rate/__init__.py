from http import HTTPStatus
from flask import Flask
from .models import list_all_conversions, currency_rate

app = Flask(__name__)

@app.get('/')
def home():
    
    return {
        "endpoints" : {"All conversions rate" : "latest/<currency>",
        "Specific rate conversion" : "pair/<currency_to_convert>/<currency_to_be_converted>"}
        }, HTTPStatus.OK

@app.get('/latest/<currency>')
def get_all_conversions(currency):

    return list_all_conversions(currency)

@app.get('/pair/<currency_to_convert>/<currency_to_be_converted>')
def get_specific_conversions(currency_to_convert, currency_to_be_converted):

    return currency_rate(currency_to_convert, currency_to_be_converted)

@app.errorhandler(404)
def error_size_message(error):
   
    return {"message" : "currency not found"}, HTTPStatus.NOT_FOUND