import requests 
import json
import time
import csv
import keyboard
import functions as fn

#Price Dicrepancy Search 
#Version Alpha 2.0 by Alex Henderson

minor_discrepancy = 0
moderate_discrepancy = 0
runs = 0
start = 1
s = time.localtime()
start_time = time.strftime("%H:%M:%S", s)
start_time2 = time.strftime("%H_%M_%S", s)

try:
    output = open('output{}.csv'.format(start_time2), 'x')
except:
    print('Error: Something with the CSV, fuck if I know what')

field = ['coin', 'margin', 'class', 'buy_price', 'sell_price', 'buy_exchange', 'sell_exchange', 'time_found']

with open('output{}.csv'.format(start_time2), 'w', encoding = 'UTF8') as f:
    writer = csv.DictWriter(f, fieldnames = field)
    writer.writeheader()

print('Price Discrepancy Search by Alex Henderson')
print('V2.0 Alpha\n')

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
        print('Search Initiated at:', start_time,'\n')
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

    def sort(a):
        return a['price']


    #Searching for Bitcoin

    #Gets Bitcoin Buy Price and Sorts Prices with cheapest in first place
    btc_buy = [fn.getprice_coinspot('btc', 'ask'), fn.getprice_swiftx('BTC', 'buy'), fn.getprice_coinjar('BTC', 'ask')]
    btc_buy.sort(reverse= False, key= sort)

    #Gets Bitcoin Sell price and sorts with best in first place
    btc_sell = [fn.getprice_coinspot('btc', 'bid'), fn.getprice_swiftx('BTC', 'sell'), fn.getprice_coinjar('BTC', 'bid')]
    btc_sell.sort(reverse = True, key=sort)

    #Check variable calls check_margin from functions and saves True or False depending on whether margin is larger than 0.1
    check_btc = fn.check_margin(btc_buy[0]['price'], btc_sell[0]['price'])[0]

    #Margin variable calls check_margin from functions and saves the profit margin
    margin_btc = fn.check_margin(btc_buy[0]['price'], btc_sell[0]['price'])[1]

    #Exchange Variable creates dictionary with which exchange the appropriate buy and sell price can be found on
    exchange_btc = {'Buy': btc_buy[0]['exchange'], 'Sell': btc_sell[0]['exchange']}



    #Searching for Ripple 

    #See above comments for description

    xrp_buy = [fn.getprice_coinspot('xrp', 'ask'), fn.getprice_swiftx('XRP', 'buy'), fn.getprice_coinjar('XRP', 'ask')]
    xrp_buy.sort(reverse= False, key= sort)

    xrp_sell = [fn.getprice_coinspot('xrp', 'bid'), fn.getprice_swiftx('XRP', 'sell'), fn.getprice_coinjar('XRP', 'bid')]
    xrp_sell.sort(reverse= True, key=sort)

    check_xrp = fn.check_margin(xrp_buy[0]['price'], xrp_sell[0]['price'])[0]

    margin_xrp = fn.check_margin(xrp_buy[0]['price'], xrp_sell[0]['price'])[1]

    exchange_xrp = {'Buy': xrp_buy[0]['exchange'], 'Sell': xrp_sell[0]['exchange']}



    #Searching for Litecoin

    #See above comments for description

    ltc_buy = [fn.getprice_coinspot('ltc', 'ask'), fn.getprice_swiftx('LTC', 'buy'), fn.getprice_coinjar('LTC', 'ask')]
    ltc_buy.sort(reverse= False, key =sort)

    ltc_sell = [fn.getprice_coinspot('ltc', 'bid'), fn.getprice_swiftx('LTC', 'sell'), fn.getprice_coinjar('LTC', 'bid')]
    ltc_sell.sort(reverse= True, key = sort)

    check_ltc = fn.check_margin(ltc_buy[0]['price'], ltc_sell[0]['price'])[0]

    margin_ltc = fn.check_margin(ltc_buy[0]['price'], ltc_sell[0]['price'])[1]

    exchange_ltc = {'Buy': ltc_buy[0]['exchange'], 'Sell': ltc_sell[0]['exchange']}
    
    
    #Searching for Stellar 

    #See above comments for description

    xlm_buy = [fn.getprice_coinspot('str', 'ask'), fn.getprice_swiftx('XLM', 'buy'), fn.getprice_coinjar('XLM', 'ask')]
    xlm_buy.sort(reverse= False, key=sort)

    xlm_sell = [fn.getprice_coinspot('str', 'bid'), fn.getprice_swiftx('XLM', 'sell'), fn.getprice_coinjar('XLM', 'bid')]
    xlm_sell.sort(reverse= True, key=sort)

    check_xlm = fn.check_margin(xlm_buy[0]['price'], xlm_sell[0]['price'])[0]

    margin_xlm = fn.check_margin(xlm_buy[0]['price'], xlm_sell[0]['price'])[1]

    exchange_xlm = {'Buy': xlm_buy[0]['exchange'], 'Sell': xlm_sell[0]['exchange']}

    
    #Searching for Cardano

    #See above comments for description 

    ada_buy = [fn.getprice_coinspot('ada', 'ask'), fn.getprice_swiftx('ADA', 'buy')]
    ada_buy.sort(reverse= False, key=sort)

    ada_sell = [fn.getprice_coinspot('ada', 'bid'), fn.getprice_swiftx('ADA', 'sell')]
    ada_sell.sort(reverse= True, key=sort)

    check_ada = fn.check_margin(ada_buy[0]['price'], ada_sell[0]['price'])[0]

    margin_ada = fn.check_margin(ada_buy[0]['price'], ada_sell[0]['price'])[1]

    exchange_ada = {'Buy': ada_buy[0]['exchange'], 'Sell': ada_sell[0]['exchange']}


    #Begin Saving Data based on previous searches
    
    def csv_row(rows):
        with open('output{}.csv'.format(start_time2), 'a', encoding = 'UTF8') as f:
            writer = csv.DictWriter(f, fieldnames = field)
            writer.writerows(rows)

    #Format Discrepancy Data into usable dictionaries

    rows_btc = [{
        'coin': 'BTC',
        'margin': margin_btc,
        'class': fn.check_margin_size(margin_btc), #Class here refers to the 'size' of any given discrepancy catagorised in functions.py
        'buy_price': btc_buy[0]['price'],
        'sell_price': btc_sell[0]['price'],
        'buy_exchange': exchange_btc['Buy'],
        'sell_exchange': exchange_btc['Sell'],
        'time_found': current_time
        }]
    
    rows_xrp = [{
        'coin': 'XRP',
        'margin': margin_xrp,
        'class': fn.check_margin_size(margin_xrp),
        'buy_price': xrp_buy[0]['price'],
        'sell_price': xrp_sell[0]['price'],
        'buy_exchange': exchange_xrp['Buy'],
        'sell_exchange': exchange_xrp['Sell'],
        'time_found': current_time
    }]

    rows_ltc = [{
        'coin': 'LTC',
        'margin': margin_ltc,
        'class': fn.check_margin_size(margin_ltc), 
        'buy_price': ltc_buy[0]['price'],
        'sell_price': ltc_sell[0]['price'],
        'buy_exchange': exchange_ltc['Buy'],
        'sell_exchange': exchange_ltc['Sell'],
        'time_found': current_time
    }]
    
    rows_xlm = [{
        'coin': 'XLM',
        'margin': margin_xlm,
        'class': fn.check_margin_size(margin_xlm),
        'buy_price': xlm_buy[0]['price'],
        'sell_price': xlm_sell[0]['price'],
        'buy_exchange': exchange_xlm['Buy'],
        'sell_exchange': exchange_xlm['Sell'],
        'time_found': current_time
    }]

    rows_ada = [{
        'coin': 'ADA',
        'margin': margin_ada,
        'class': fn.check_margin_size(margin_ada),
        'buy_price': ada_buy[0]['price'],
        'sell_price': ada_sell[0]['price'],
        'buy_exchange': exchange_ada['Buy'],
        'sell_exchange': exchange_ada['Sell'],
        'time_found': current_time
    }]

    # Check Profit Margin data to determine whether a discrepany has been found and
    # calls the csv write function with the data stored in the given pricing dictionary at that time

    if margin_btc >= 0.5:
        csv_row(rows_btc)
        print('Discrepancy Found: BTC\n', 'Size:', rows_btc[0]['class'], '@', current_time,'\n')
        moderate_discrepancy += 1
        continue
    elif margin_btc >= 0.2:
        minor_discrepancy += 1
        continue

    if margin_xrp >= 0.5:
        csv_row(rows_xrp)
        print('Discrepancy Found: XRP\n', 'Size:', rows_xrp[0]['class'], '@', current_time,'\n')
        moderate_discrepancy += 1
        continue
    elif margin_xrp >= 0.2: 
        minor_discrepancy += 1
        continue

    if margin_ltc >= 0.5:
        csv_row(rows_ltc)
        print('Discrepancy Found: LTC\n', 'Size:', rows_ltc[0]['class'], '@', current_time,'\n')
        moderate_discrepancy += 1
        continue 
    elif margin_ltc >= 0.2:
        minor_discrepancy += 1
        continue

    if margin_xlm >= 0.5:
        csv_row(rows_xlm)
        print('Discrepancy Found: XLM\n', 'Size:', rows_xlm[0]['class'], '@', current_time,'\n')
        moderate_discrepancy += 1
        continue
    elif margin_xlm >= 0.2:
        minor_discrepancy =+1
        continue

    if margin_ada >= 0.5:
        csv_row(rows_ada)
        print('Discrepancy Found: ADA\n', 'Size:', rows_ada[0]['class'], '@', current_time,'\n')
        moderate_discrepancy += 1
        continue
    elif margin_ada >= 0.2:
        minor_discrepancy += 1
        continue 

    runs += 1
  
    if runs == 50:
        print('Moderate Discrepancies Found:', moderate_discrepancy)
        print('Minor Discrepancies Found:', minor_discrepancy,'\n')
        continue
    elif runs == 100:
        print('Search Started:', start_time)
        print('Moderate Discrepancies Found:', moderate_discrepancy)
        print('Minor Discrepancies Found:', minor_discrepancy,'\n')
        runs = 0
        continue