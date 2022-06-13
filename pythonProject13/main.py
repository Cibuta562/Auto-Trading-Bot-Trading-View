
###########imports############

import json, config
from flask import Flask, request, jsonify
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

##########initiate order on Binance########

client = Client(config.API_KEY, config.SECRET_KEY)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"Sending the order {order_type} - {side} of {quantity} {symbol} to Binance")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("An exception has occured - {}".format(e))
        return False
    return order




@app.route('/')
def main():
    return "Merge !! "


@app.route('/auto_trade', methods=['POST'])
def auto_trade():
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error"
        }

    info = client.get_symbol_info('ADAUSDT')
    print(info['filters'][2]['minQty'])


    print(data['ticker'])

    buy_or_sell = data['strategy']['order_action'].upper()
    quantity = data['strategy']['order_contracts']

    order_response = order(buy_or_sell, quantity, "ADAUSDT")
    print(order_response)

    if order_response:
        return{
            "code": "success",
            "message": "Order has been executed <3"
        }
    else:

        print("Order failed")

        return{
            "code": "error",
            "message": "Order has not been executed :("
        }

##########just to start the app###########

if __name__ == '__main__':
    app.run()
