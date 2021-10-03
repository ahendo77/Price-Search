import requests 
import json
import time
import csv
import functions as fn

#Price Dicrepancy Search 
#Version 2.0 by Alex Henderson


start = 1
s = time.localtime()
start_time = time.strftime("%H:%M:%S", s)
start_time2 = time.strftime("%H_%M_%S", s)

output = open('output{}.csv'.format((str(start_time2)), 'x'))


print('Price Discrepancy Search V2.0 by Alex Henderson\n')

print('Checking API Status...\n')

#Check API Status for CoinJar

status_get3 = requests.get('https://data.exchange.coinjar.com/products/BTCAUD/ticker')
if status_get3.status_code == 200:
    print('CoinJar API Status: GOOD')
else:
    print('CoinJar API Status: ERROR')
    exit()


# Check API Status for Swiftx

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

#Check API Status for Coinspot 

status_get2 = requests.get('https://www.coinspot.com.au/pubapi/v2/latest').text
status2 = requests.get('https://www.coinspot.com.au/pubapi/v2/latest')
coinspot_status1 = json.loads(status_get2)
coinspot_status2 = coinspot_status1['status']

if coinspot_status2 == 'ok' and status2.status_code == 200:
    print('Coinspot API Status: GOOD\n')
else:
    print('Coinspot API Status: ERROR')
    exit()

while start == 1:
    question = input('API Status OK, begin searching? Y/N\n')
    if question == 'y' or question == 'Y':
        print('\nNow Searching...','\n')
        start = 0
        break
    elif question == 'n' or question == 'N':
        exit()
    else:
        print('Please enter y or n\n')
        continue

while start == 0:

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    #Searching for Bitcoin

    #Gets Bitcoin Buy Price and Sorts Prices with cheapest in first place
    btc_buy = [fn.getprice_coinspot('btc', 'ask')[0], fn.getprice_swiftx('BTC', 'buy')[0], fn.getprice_coinjar('BTC', 'ask')[0]]
    btc_buy.sort(reverse= False)
    
    #Gets Bitcoin Sell price and sorts with best in first place
    btc_sell = [fn.getprice_coinspot('btc', 'bid')[0], fn.getprice_swiftx('BTC', 'sell')[0], fn.getprice_coinjar('BTC', 'bid')[0]]
    btc_sell.sort(reverse = True)

    #Check variable calls check_margin from functions and saves True or False depending on whether margin is larger than 0.1
    check_btc = fn.check_margin(btc_buy[0], btc_sell[0])[0]

    #Margin variable calls check_margin from functions and saves the profit margin
    margin_btc = fn.check_margin(btc_buy[0], btc_sell[0])[1]

    #Exchange Variable creates dictionary with which exchange the appropriate buy and sell price can be found on
    exchange_btc = {'Buy': btc_buy[0][1], 'Sell': btc_sell[0][1]}



    #Searching for Ripple 

    #See above comments for description

    xrp_buy = [fn.getprice_coinspot('xrp', 'ask')[0], fn.getprice_swiftx('XRP', 'buy')[0], fn.getprice_coinjar('XRP', 'ask')[0]]
    xrp_buy.sort(reverse= False)

    xrp_sell = [fn.getprice_coinspot('xrp', 'bid')[0], fn.getprice_swiftx('XRP', 'sell')[0], fn.getprice_coinjar('XRP', 'bid')[0]]
    xrp_sell.sort(reverse= True)

    check_xrp = fn.check_margin(xrp_buy[0], xrp_sell[0])[0]

    margin_xrp = fn.check_margin(xrp_buy[0], xrp_sell[0])[1]

    exchange_xrp = {'Buy': xrp_buy[0][1], 'Sell': xrp_sell[0][1]}



    #Searching for Litecoin

    #See above comments for description

    ltc_buy = [fn.getprice_coinspot('ltc', 'ask')[0], fn.getprice_swiftx('LTC', 'buy')[0], fn.getprice_coinjar('LTC', 'ask')[0]]
    ltc_buy.sort(reverse= False)

    ltc_sell = [fn.getprice_coinspot('ltc', 'bid')[0], fn.getprice_swiftx('LTC', 'sell')[0], fn.getprice_coinjar('LTC', 'bid')[0]]
    ltc_sell.sort(reverse= True)

    check_ltc = fn.check_margin(ltc_buy[0], ltc_sell[0])[0]

    margin_ltc = fn.check_margin(ltc_buy[0], ltc_sell[0])[1]

    exchange_ltc = {'Buy': ltc_buy[0][1], 'Sell': ltc_sell[0][1]}
    
    
    #Searching for Stellar 

    #See above comments for description

    xlm_buy = [fn.getprice_coinspot('str', 'ask')[0], fn.getprice_swiftx('XLM', 'buy')[0], fn.getprice_coinjar('XLM', 'ask')[0]]
    xlm_buy.sort(reverse= False)

    xlm_sell = [fn.getprice_coinspot('str', 'bid')[0], fn.getprice_swiftx('XLM', 'sell')[0], fn.getprice_coinjar('XLM', 'bid')[0]]
    xlm_sell.sort(reverse= True)

    check_xlm = fn.check_margin(xlm_buy[0], xlm_sell[0])[0]

    margin_xlm = fn.check_margin(xlm_buy[0], xlm_sell[0])[1]

    exchange_xlm = {'Buy': xlm_buy[0][1], 'Sell': xlm_sell[0][1]}

    
    #Searching for Cardano

    #See above comments for description 

    ada_buy = [fn.getprice_coinspot('ada', 'ask')[0], fn.getprice_swiftx('ADA', 'buy')[0]]
    ada_buy.sort(reverse= False)

    ada_sell = [fn.getprice_coinspot('ada', 'bid')[0], fn.getprice_swiftx('ADA', 'sell')[0]]
    ada_sell.sort(reverse= True)

    check_ada = fn.check_margin(ada_buy[0], ada_sell[0])[0]

    margin_ada = fn.check_margin(ada_buy[0], ada_sell[0])[1]

    exchange_ada = {'Buy': ada_buy[0][1], 'Sell': ada_sell[0][1]}


    #Begin Saving Data based on previous searches
    
    field = ['coin', 'margin', 'buy_price', 'sell_price', 'buy_exchange', 'sell_exchange', 'time_found']
    
    if check_btc == True:
        rows = {
            'coin': 'BTC',
            'margin': margin_btc,
            'buy_price': btc_buy,
            'sell_price': btc_sell,
            'buy_exchange': exchange_btc['Buy'],
            'sell_exchange': exchange_btc['Sell'],
            'time_found': current_time
        }
        














    
    


