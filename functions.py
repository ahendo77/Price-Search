import time
import json
import requests
import keyboard


#Price Dicrepancy Search 
#Version Alpha 1.1.0 by Alex Henderson

#coins = bitcoin, ripple, litecoin, stellar, cardano
#codes = btc, xrp, ltc, xlm(str for coinspot), ada


#Starting the Program

def user_input():
    s = time.localtime()
    start_time = time.strftime("%H:%M:%S", s)
    start = 1
    question = input('\nAPI Status OK, begin searching? Y/N\n')
    
    while start == 1:
        if question == 'y' or question == 'Y':
            print('\nNow Searching...','\n')
            print('Search Initiated at:', start_time,'\n')
            break
        elif question == 'n' or question == 'N':
            exit()
        else:
            print('Please enter y or n\n')
            continue


#Check API Status of Exchanges

def checkstatus_coinspot():
    status_get2 = requests.get('https://www.coinspot.com.au/pubapi/v2/latest').text
    status2 = requests.get('https://www.coinspot.com.au/pubapi/v2/latest')
    coinspot_status1 = json.loads(status_get2)
    coinspot_status2 = coinspot_status1['status']
    
    if coinspot_status2 == 'ok' and status2.status_code == 200:
        print('Coinspot API Status: GOOD')
    else:
        print('Coinspot API Status: ERROR')
        exit()

def checkstatus_coinjar():
    status_get3 = requests.get('https://data.exchange.coinjar.com/products/BTCAUD/ticker')
    if status_get3.status_code == 200:
        print('CoinJar API Status: GOOD')
    else:
        print('CoinJar API Status: ERROR')
        exit()

def checkstatus_swiftx():
    status_get = requests.get('https://api.swyftx.com.au/info/').text
    status1 = requests.get('https://api.swyftx.com.au/info/')
    swiftx_status = json.loads(status_get)
    swiftx_maintain = swiftx_status['maintenanceMode']
    swiftx_state = swiftx_status['state']
    swiftx_api = 'blank'
    
    if swiftx_maintain == False and swiftx_state == 1 and status1.status_code == 200:
        swiftx_api = 'good'
    else:
        swiftx_api = 'bad'
    
    if swiftx_api == 'good':
        print('Swiftx API Status: GOOD')
    else:
        print('Swiftx API Status: ERROR')
        exit()


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


# Checking Profit Margin 

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
    if margin >= 0.5:
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