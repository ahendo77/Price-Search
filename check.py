from os import error
import sqlite3
import time
import functions as fn


'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.0

CHECK file holds functions to actively search through
live price database and record descrepancies found to
a seperate database. 

'''

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

#Here for testing 
#start_discrepancydb()

# Check for and open connection to Live Price Database

def connect_liveprices():
    try:
        global session_start
        global conn_live
        global cursor_live
        session_start = time.strftime('%H:%M:%S')
        conn_live = sqlite3.connect('raw_data.db')
        cursor_live = conn_live.cursor()
        print('Live Price Connection 2 Successful')
        time.sleep(0.5)
    except:
        print('Error with database:', error)
        exit()

#Here for testing
#connect_liveprices()

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
    cursor_live.execute('SELECT * FROM btc ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
    row = list(cursor_live.fetchall())
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
        print('Discrepancy found!')
        print('placeholder')
        cursor.execute('INSERT INTO btc VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
        conn.commit()
    elif margin[0] == False:
        return False
    

# Checks XRP Table for discrepancies

def check_xrp():
    cursor_live.execute('SELECT * FROM xrp ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
    row = list(cursor_live.fetchall())
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
    margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories

    #If margin returns true, there is a discrepancy of more than 0.2 *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
    if margin[0] == True:
        print('Discrepancy found!')
        print('placeholder')
        cursor.execute('INSERT INTO xrp VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
        conn.commit()
    elif margin[0] == False:
        return False

# Checks LTC Table for discrepancies

def check_ltc():
    cursor_live.execute('SELECT * FROM ltc ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
    row = list(cursor_live.fetchall())
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
    margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories

    #If margin returns true, there is a discrepancy of more than 0.2 *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
    if margin[0] == True:
        print('Discrepancy found!')
        print('placeholder')
        cursor.execute('INSERT INTO ltc VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
        conn.commit()
    elif margin[0] == False:
        return False


# Checks XLM (STR Coinspot) Table for discrepancies

def xlm_check():
    cursor_live.execute('SELECT * FROM xlm ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
    row = list(cursor_live.fetchall())
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
    margin_size = fn.check_margin_size(margin[1]) # Need to fix margin size function for more catagories

    #If margin returns true, there is a discrepancy of more than 0.2 *** MARGIN HAS TEMPORARY LOW FOR TESTING ***
    if margin[0] == True:
        print('Discrepancy found!')
        print('placeholder')
        cursor.execute('INSERT INTO xlm VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
        conn.commit()
    elif margin[0] == False:
        return False


# Checks ADA (CoinJar doesn't sell) Table for discrepancies

def check_ada():
    cursor_live.execute('SELECT * FROM ada ORDER BY ROWID DESC LIMIT 1') # FUCK YEAH THIS WORKS FINALLY 
    row = list(cursor_live.fetchall())
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
        print('Discrepancy found!')
        print('placeholder')
        cursor.execute('INSERT INTO ada VALUES(?, ?, ?, ?, ?, ?, ?)', (dataid, margin[1], prices_buy[0]['price'], prices_sell[0]['price'], prices_buy[0]['market'], prices_sell[0]['market'], margin_size))
        conn.commit()
    elif margin[0] == False:
        return False


