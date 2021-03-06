import time
import json
import requests
import os 
import platform
import logging

'''

Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.1

FUNCTIONS file serves to store functions used by other
parts of the program for ogransiation and ease of use.

'''


#coins = bitcoin, ripple, litecoin, stellar, cardano
#codes = btc, xrp, ltc, xlm(str for coinspot), ada

#Starting the Program

#global sessionstart_btc, requestnumber_xrp, requestnumber_ltc, requestnumber_xlm, requestnumber_ada
#requestnumber_btc = 0

# Y/N question function

def user_query(response):
    while True:
        for i in response:
            if i == 'y' or i == 'Y':
                return True
            elif i == 'n' or i == 'N':
                return False
            else:
                print('Please enter y/n')
                response = input()
                continue


#Check API Status of Exchanges

def checkstatus_marketapi():
    while True:
        response1 = checkstatus_coinspot()
        response2 = checkstatus_swiftx()
        response3 = checkstatus_coinjar()
          
        print('\nCoinSpot API Status:', response1)
        time.sleep(0.3) # Delay just cause it makes it seem cooler
        print('SwiftX API Status:', response2)
        time.sleep(0.3)
        print('CoinJar API Status:', response3)

        if response1 != 'GOOD' or response2 != 'GOOD' or response3 != 'GOOD':
            print('\nAPI status check failed, exiting...')
            exit()
        else:
            break


def checkstatus_coinspot():
    try:
        status_get2 = requests.get('https://www.coinspot.com.au/pubapi/v2/latest').text
        status2 = requests.get('https://www.coinspot.com.au/pubapi/v2/latest')
    except requests.ConnectionError:
        logging.error('No Internet Connection, please check network and try again')
        exit()

    coinspot_status1 = json.loads(status_get2)
    coinspot_status2 = coinspot_status1['status']
    
    if coinspot_status2 == 'ok' and status2.status_code == 200:
        #print('Coinspot API Status: GOOD')
        return 'GOOD'
    else:
        #print('Coinspot API Status: ERROR')
        return 'ERROR'

def checkstatus_coinjar():
    try:
        status_get3 = requests.get('https://data.exchange.coinjar.com/products/BTCAUD/ticker')
    except requests.ConnectionError:
        logging.error('No Internet Connection, please check network and try again')
        exit()
   
    if status_get3.status_code == 200:
        #print('CoinJar API Status: GOOD')
        return 'GOOD'
    else:
        #print('CoinJar API Status: ERROR')
        return 'ERROR'

def checkstatus_swiftx():
    try:
        status_get = requests.get('https://api.swyftx.com.au/info/').text
        status1 = requests.get('https://api.swyftx.com.au/info/')
    except requests.ConnectionError:
        logging.error('No Internet Connection, please check network and try again')
        exit()

    swiftx_status = json.loads(status_get)
    swiftx_maintain = swiftx_status['maintenanceMode']
    swiftx_state = swiftx_status['state']
    swiftx_api = 'blank'
    
    if swiftx_maintain == False and swiftx_state == 1 and status1.status_code == 200:
        swiftx_api = 'good'
    else:
        swiftx_api = 'bad'
    
    if swiftx_api == 'good':
        #print('Swiftx API Status: GOOD')
        return 'GOOD'
    else:
        #print('Swiftx API Status: ERROR')
        return 'ERROR'


#Getting Prices from Exchanges

def getprice_coinspot(coin = 'btc' or 'xrp' or 'ltc' or 'str' or 'ada', type = 'ask' or 'bid'):
    try:
        api = requests.get('https://www.coinspot.com.au/pubapi/v2/latest').text
    except requests.ConnectionError:
        logging.error('No Internet Connection, please check network and try again')
        exit()

    response = json.loads(api)
    price = response['prices'][coin][type]
    #exchange = 'Coinspot'
    #dict = {'price': price, 'exchange': exchange}
    return price

def getprice_swiftx(coin = 'BTC' or 'XRP' or 'LTC' or 'XLM' or 'ADA', type = 'buy' or 'sell'):
    try:
        api = requests.get('https://api.swyftx.com.au/markets/info/basic/{}/'.format(coin)).text
    except requests.ConnectionError:
        logging.error('No Internet Connection, please check network and try again')
        exit()
        
    response = json.loads(api)
    price = response[0][type]
    #exchange = 'Swiftx'
    #dict = {'price': price, 'exchange': exchange}
    return price

def getprice_coinjar(coin = 'BTC' or 'XRP' or 'LTC' or 'XLM', type = 'ask' or 'bid'):
    api = requests.get('https://data.exchange.coinjar.com/products/{}AUD/ticker'.format(coin)).text
    response = json.loads(api)
    price = response[type]
    #exchange = 'CoinJar'
    #dict = {'price': price, 'exchange': exchange}
    return price

# Getting Pricing Data for each asset in lists

# BTC Data 
def getdata_btc():
    #Coinspot Data
    buy_coinspot = getprice_coinspot('btc', 'ask') #Calls function from functions.py
    sell_coinspot = getprice_coinspot('btc', 'bid')

    #Swiftx Data
    buy_swiftx = getprice_swiftx('BTC', 'buy')
    sell_swiftx = getprice_swiftx('BTC', 'sell')

    #Coinjar Data
    buy_coinjar = getprice_coinjar('BTC', 'ask')
    sell_coinjar = getprice_coinjar('BTC', 'bid')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

# XRP Data
def getdata_xrp():
    #Coinspot Data
    buy_coinspot = getprice_coinspot('xrp', 'ask')
    sell_coinspot = getprice_coinspot('xrp', 'bid')

    #Swiftx Data
    buy_swiftx = getprice_swiftx('XRP', 'buy')
    sell_swiftx = getprice_swiftx('XRP', 'sell')

    #Coinjar Data
    buy_coinjar = getprice_coinjar('XRP', 'ask')
    sell_coinjar = getprice_coinjar('XRP', 'bid')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

# LTC Data
def getdata_ltc():
    #Coinspot Data
    buy_coinspot = getprice_coinspot('ltc', 'ask')
    sell_coinspot = getprice_coinspot('ltc', 'bid')

    #Swiftx Data
    buy_swiftx = getprice_swiftx('LTC', 'buy')
    sell_swiftx = getprice_swiftx('LTC', 'sell')

    #Coinjar Data
    buy_coinjar = getprice_coinjar('LTC', 'ask')
    sell_coinjar = getprice_coinjar('LTC', 'bid')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

#XLM Data
def getdata_xlm():
    #Coinspot Data
    buy_coinspot = getprice_coinspot('str', 'ask')
    sell_coinspot = getprice_coinspot('str', 'bid')

    #Swiftx Data
    buy_swiftx = getprice_swiftx('XLM', 'buy')
    sell_swiftx = getprice_swiftx('XLM', 'sell')

    #Coinjar Data
    buy_coinjar = getprice_coinjar('XLM', 'ask')
    sell_coinjar = getprice_coinjar('XLM', 'bid')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

#ADA Data (Coinjar doesn't list ADA)

def getdata_ada():
    #Coinspot Data
    buy_coinspot = getprice_coinspot('ada', 'ask')
    sell_coinspot = getprice_coinspot('ada', 'bid')

    #Swiftx Data
    buy_swiftx = getprice_swiftx('ADA', 'buy')
    sell_swiftx = getprice_swiftx('ADA', 'sell')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx]
    return list


# Checking Profit Margin 

#TEMPORARY CHANGE FOR TESTING PURPOSES
def check_margin(buy, sell):
    difference = (float(sell)) - (float(buy))
    margin = difference*100/(float(buy))
    if margin >= 0.2: # *** SHOULD BE 0.2 ***
        list = [True, margin]
        return list
    else:
        list = [False, margin]
        return list

def check_margin_size(margin):
    if 0.2 <= margin <= 0.49:
        return 'Very Minor'
    elif 0.5 <= margin <= 0.99:
        return 'Minor'
    elif 1 <= margin <= 1.99:
        return 'Moderate'
    elif 2 <= margin <= 2.99:
        return 'Large'
    elif 3 <= margin <= 9.99:
        return 'Very Large'
    elif margin >= 10:
        return 'Extreme'


global os_name
os_name = platform.system()

def message():
    # Clear should work on both not sure why os can't execute it
    if os_name == 'Windows':
        os.system('cls')
        print('Price-Search (C) 2021 Alex Henderson','\nV2.0.1 Alpha\n')
    elif os_name == 'Linux':
        os.system('clear')
        print('Price-Search (C) 2021 Alex Henderson','\nV2.0.1 Alpha\n')