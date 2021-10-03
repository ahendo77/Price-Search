import time
import json
import requests


start_time = time.time()

#coins = bitcoin, ripple, litecoin, stellar, cardano
#codes = btc, xrp, ltc, xlm(str for coinspot), ada

#Getting Prices from Exchanges

def getprice_coinspot(coin = 'btc' or 'xrp' or 'ltc' or 'str' or 'ada', type = 'ask' or 'bid'):
    api = requests.get('https://www.coinspot.com.au/pubapi/v2/latest').text
    response = json.loads(api)
    price = response['prices'][coin][type]
    exchange = 'Coinspot'
    list = [price, exchange]
    return list

def getprice_swiftx(coin = 'BTC' or 'XRP' or 'LTC' or 'XLM' or 'ADA', type = 'buy' or 'sell'):
    api = requests.get('https://api.swyftx.com.au/markets/info/basic/{}/'.format(coin)).text
    response = json.loads(api)
    price = response[0][type]
    exchange = 'Swiftx'
    list = [price, exchange]
    return list

def getprice_coinjar(coin = 'BTC' or 'XRP' or 'LTC' or 'XLM', type = 'ask' or 'bid'):
    api = requests.get('https://data.exchange.coinjar.com/products/{}AUD/ticker'.format(coin)).text
    response = json.loads(api)
    price = response[type]
    exchange = 'CoinJar'
    list = [price, exchange]
    return list

def check_margin(buy, sell):
    difference = (float(sell)) - (float(buy))
    margin = difference*100/(float(buy))
    if margin >= 0.1:
        list = [True, margin]
        return list
    else:
        list = [False, margin]
        return list


        
