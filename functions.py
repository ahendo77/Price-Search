import time
import json
import requests
import csv


start_time = time.time()

#coins = bitcoin, ripple, litecoin, stellar, cardano
#codes = btc, xrp, ltc, xlm(str for coinspot), ada

#Getting Prices from Exchanges

def getprice_coinspot(coin = 'btc' or 'xrp' or 'ltc' or 'str' or 'ada', type = 'ask' or 'bid'):
    api = requests.get('https://www.coinspot.com.au/pubapi/v2/latest').text
    response = json.loads(api)
    price = response['prices'][coin][type]
    exchange = 'Coinspot'
    dict = {'price': price, 'exchange': exchange}
    return dict

def getprice_swiftx(coin = 'BTC' or 'XRP' or 'LTC' or 'XLM' or 'ADA', type = 'buy' or 'sell'):
    api = requests.get('https://api.swyftx.com.au/markets/info/basic/{}/'.format(coin)).text
    response = json.loads(api)
    price = response[0][type]
    exchange = 'Swiftx'
    dict = {'price': price, 'exchange': exchange}
    return dict

def getprice_coinjar(coin = 'BTC' or 'XRP' or 'LTC' or 'XLM', type = 'ask' or 'bid'):
    api = requests.get('https://data.exchange.coinjar.com/products/{}AUD/ticker'.format(coin)).text
    response = json.loads(api)
    price = response[type]
    exchange = 'CoinJar'
    dict = {'price': price, 'exchange': exchange}
    return dict

def check_margin(buy, sell):
    difference = (float(sell)) - (float(buy))
    margin = difference*100/(float(buy))
    if margin >= 0.5:
        list = [True, margin]
        return list
    else:
        list = [False, margin]
        return list

def check_margin_size(margin):
    if margin >= -0.001:
        return 'Test'
    elif margin >= 0.001:
        return 'Minor'
    elif margin >= 0.7:
        return 'Moderate'
    elif margin >= 1:
        return 'Signifcant'
    elif margin >= 2:
        return 'Extreme'
    elif margin >= 3:
        return 'Holy Shit'
    elif margin >= 5:
        return 'Well fuck me'
    elif margin >= 10:
        return 'Brb buying a lambo'

