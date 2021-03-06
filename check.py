from os import error
import sqlite3
import time
import functions as fn
import logging
import threading


'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.1

CHECK file holds functions to actively search through
live price database and record descrepancies found to
a seperate database. 

'''

# Logging Config
logging.basicConfig()
logging.root.setLevel(level=logging.INFO)


# Setting up database to store discrepancies
#codes = btc, xrp, ltc, xlm(str for coinspot), ada

# Function key to sort dictionaries by price
def sort(price):
    return price['price']


# Create / Open connection to discrepancy database
def start_discrepancydb():
    try:
        global cursor
        global conn
        conn = sqlite3.connect('discrepancy_data.db')
        cursor = conn.cursor()
        print('Price Discrepancy Connection Successful')
        time.sleep(0.5)
    except:
        print('Error with database:', error)
        exit()

    # Creating tables for databse 

    cursor.execute('''CREATE TABLE IF NOT EXISTS btc(
        dataid TEXT PRIMARY KEY,
        margin REAL,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT,
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS xrp(
        dataid TEXT PRIMARY KEY,
        margin REAL,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT,
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS ltc(
        dataid TEXT PRIMARY KEY,
        margin REAL,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT,
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS xlm(
        dataid TEXT PRIMARY KEY,
        margin REAL,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT,
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS ada(
        dataid TEXT PRIMARY KEY,
        margin REAL,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT,
        size_catagory TEXT);'''
    )


'''
Section here fetches the first decending row
from the live price database and does math to
check for discrepancies. Then inputs into new 
discrepancy database. 

Rows returned from database are as follows: 
[0] = dataid
[1] = buy_price_coinspot
[2] = sell_price_coinspot
[3] = buy_price_swiftx
[4] = sell_price_swiftx
[5] = buy_price_coinjar
[6] = sell_price_coinjar

'''

# Checks BTC Table for discrepancies

def check_btc():
    # Needs seperate SQL connection for each thread
    #logging.debug('Starting BTC1')
    conn_btc = sqlite3.connect('discrepancy_data.db') # Connection to discrepancy database
    cursor_btc = conn_btc.cursor()

    conn_btc_live = sqlite3.connect('raw_data.db') # Connection to live price database
    cursor_btc_live = conn_btc_live.cursor()
    time.sleep(4) # Give time for graphics to change before printing starts
    
    while True:
        cursor_btc_live.execute('SELECT * FROM btc ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
        row = list(cursor_btc_live.fetchall())
        row1 = row[0] # Row returns list within a list
        dataid = row1[0]
        
        #Placing prices into dictionaries to determine orgin market
        prices_buy = [{'price': row1[1], 'market': 'CoinSpot'}, {'price': row1[3], 'market': 'Swiftx'}, {'price': row1[5], 'market': 'CoinJar'}]
        prices_sell = [{'price': row1[2], 'market': 'CoinSpot'}, {'price': row1[4], 'market': 'Swiftx'}, {'price': row1[6], 'market': 'CoinJar'}]
        
        #Sorting dictionaries based on price 
        prices_buy.sort(reverse=False, key=sort)
        prices_sell.sort(reverse=True, key= sort)
        
        #Checking for discrepancies
        margin = fn.check_margin(prices_buy[0]['price'], prices_sell[0]['price'])
        margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
        
        #If margin returns true, there is a discrepancy of more than 0.2
        if margin[0] == True:
            #logging.debug('Starting BTC2')
            cursor_btc.execute('INSERT or REPLACE INTO btc VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
            conn_btc.commit()
            # Print does not work right across threads, this will have to do instead
            message = 'Discrepancy found!\nBTC: {0} @ {1}\n'.format(margin_size, dataid )
            logging.info(message)
            time.sleep(3)
        elif margin[0] == False:
            time.sleep(1)
            continue
    

# Checks XRP Table for discrepancies
def check_xrp():
    # Needs seperate SQL connection for each thread
    #logging.debug('Starting XRP1')
    conn_xrp = sqlite3.connect('discrepancy_data.db')
    cursor_xrp = conn_xrp.cursor()

    conn_xrp_live = sqlite3.connect('raw_data.db')
    cursor_xrp_live = conn_xrp_live.cursor()
    time.sleep(4) # See BTC

    while True:
        cursor_xrp_live.execute('SELECT * FROM xrp ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
        row = list(cursor_xrp_live.fetchall())
        row1 = row[0] # Row returns list within a list
        dataid = row1[0]
        
        #Placing prices into dictionaries to determine orgin market
        prices_buy = [{'price': row1[1], 'market': 'CoinSpot'}, {'price': row1[3], 'market': 'Swiftx'}, {'price': row1[5], 'market': 'CoinJar'}]
        prices_sell = [{'price': row1[2], 'market': 'CoinSpot'}, {'price': row1[4], 'market': 'Swiftx'}, {'price': row1[6], 'market': 'CoinJar'}]
        
        #Sorting dictionaries based on price 
        prices_buy.sort(reverse=False, key=sort)
        prices_sell.sort(reverse=True, key= sort)
        
        #Checking for discrepancies
        margin = fn.check_margin(prices_buy[0]['price'], prices_sell[0]['price'])
        margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
        
        #If margin returns true, there is a discrepancy of more than 0.2
        if margin[0] == True:
            #logging.debug('Starting XRP2')
            cursor_xrp.execute('INSERT or REPLACE INTO xrp VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
            conn_xrp.commit()
            # Print does not work right across threads, this will have to do in the meantime
            message = 'Discrepancy found!\nXRP: {0} @ {1}\n'.format(margin_size, dataid ) 
            logging.info(message)
            time.sleep(3)
            continue
        elif margin[0] == False:
            time.sleep(2)
            continue
            
        
    

# Checks LTC Table for discrepancies

def check_ltc():
    # Needs seperate SQL connection for each thread
    #logging.debug('Starting LTC1')
    conn_ltc = sqlite3.connect('discrepancy_data.db')
    cursor_ltc = conn_ltc.cursor()

    conn_ltc_live = sqlite3.connect('raw_data.db')
    cursor_ltc_live = conn_ltc_live.cursor()
    time.sleep(4) # See BTC

    while True:
        cursor_ltc_live.execute('SELECT * FROM ltc ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
        row = list(cursor_ltc_live.fetchall())
        row1 = row[0] # Row returns list within a list
        dataid = row1[0]
        
        #Placing prices into dictionaries to determine orgin market
        prices_buy = [{'price': row1[1], 'market': 'CoinSpot'}, {'price': row1[3], 'market': 'Swiftx'}, {'price': row1[5], 'market': 'CoinJar'}]
        prices_sell = [{'price': row1[2], 'market': 'CoinSpot'}, {'price': row1[4], 'market': 'Swiftx'}, {'price': row1[6], 'market': 'CoinJar'}]
        
        #Sorting dictionaries based on price 
        prices_buy.sort(reverse=False, key=sort)
        prices_sell.sort(reverse=True, key= sort)
        
        #Checking for discrepancies
        margin = fn.check_margin(prices_buy[0]['price'], prices_sell[0]['price'])
        margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
        
        #If margin returns true, there is a discrepancy of more than 0.2
        if margin[0] == True:
            #logging.debug('Starting LTC2')
            cursor_ltc.execute('INSERT or REPLACE INTO ltc VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
            conn_ltc.commit()
            # Print does not work right across threads, this will have to do instead
            message = 'Discrepancy found!\nLTC: {0} @ {1}\n'.format(margin_size, dataid )
            logging.info(message)
            time.sleep(3)
            continue
        elif margin[0] == False:
            time.sleep(1)
            continue

# Checks XLM (STR Coinspot) Table for discrepancies

def check_xlm():
    # Needs seperate SQL connection for each thread
    # logging.debug('Starting XLM1')
    conn_xlm = sqlite3.connect('discrepancy_data.db')
    cursor_xlm = conn_xlm.cursor()

    conn_xlm_live = sqlite3.connect('raw_data.db')
    cursor_xlm_live = conn_xlm_live.cursor()
    time.sleep(4) # See BTC

    while True:
        cursor_xlm_live.execute('SELECT * FROM xlm ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
        row = list(cursor_xlm_live.fetchall())
        row1 = row[0] # Row returns list within a list
        dataid = row1[0]
        
        #Placing prices into dictionaries to determine orgin market
        prices_buy = [{'price': row1[1], 'market': 'CoinSpot'}, {'price': row1[3], 'market': 'Swiftx'}, {'price': row1[5], 'market': 'CoinJar'}]
        prices_sell = [{'price': row1[2], 'market': 'CoinSpot'}, {'price': row1[4], 'market': 'Swiftx'}, {'price': row1[6], 'market': 'CoinJar'}]
        
        #Sorting dictionaries based on price 
        prices_buy.sort(reverse=False, key=sort)
        prices_sell.sort(reverse=True, key= sort)
        
        #Checking for discrepancies
        margin = fn.check_margin(prices_buy[0]['price'], prices_sell[0]['price'])
        margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
        
        #If margin returns true, there is a discrepancy of more than 0.2
        if margin[0] == True:
            # logging.debug('Starting XLM2')
            cursor_xlm.execute('INSERT or REPLACE INTO xlm VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
            conn_xlm.commit()
            # Print does not work right across threads, this will have to do instead
            message = 'Discrepancy found!\nXLM: {0} @ {1}\n'.format(margin_size, dataid )
            logging.info(message)
            time.sleep(3)
            continue
        elif margin[0] == False:
            time.sleep(1)
            continue

# Checks ADA (CoinJar doesn't sell) Table for discrepancies

def check_ada():
    # Need seperate SQL connections for each thread
    #logging.debug(str('Starting ADA1'))
    conn_ada = sqlite3.connect('discrepancy_data.db')
    cursor_ada = conn_ada.cursor()

    conn_ada_live = sqlite3.connect('raw_data.db')
    cursor_ada_live = conn_ada_live.cursor()
    time.sleep(4) # See BTC

    while True:
        cursor_ada_live.execute('SELECT * FROM ada ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
        row = list(cursor_ada_live.fetchall())
        row1 = row[0] # Row returns list within a list
        dataid = row1[0]
        
        #Placing prices into dictionaries to determine orgin market
        prices_buy = [{'price': row1[1], 'market': 'CoinSpot'}, {'price': row1[3], 'market': 'Swiftx'}]
        prices_sell = [{'price': row1[2], 'market': 'CoinSpot'}, {'price': row1[4], 'market': 'Swiftx'}]
        
        #Sorting dictionaries based on price 
        prices_buy.sort(reverse=False, key=sort)
        prices_sell.sort(reverse=True, key= sort)
        
        #Checking for discrepancies
        margin = fn.check_margin(prices_buy[0]['price'], prices_sell[0]['price'])
        margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories
        
        
        #If margin returns true, there is a discrepancy of more than 0.2 *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
        if margin[0] == True:
            #logging.debug(str('Starting ADA2'))
            cursor_ada.execute('INSERT or REPLACE INTO ada VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
            conn_ada.commit()
            # Print does not work right across threads, this will have to do instead
            message = 'Discrepancy found!\nADA: {0} @ {1}\n'.format(margin_size, dataid )
            logging.info(message)
            time.sleep(3)
            continue
        elif margin[0] == False:
            time.sleep(1)
            continue

