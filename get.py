from os import error
import requests
import json 
import sqlite3
import time
import threading
import functions as fn

'''
GET files serves sole purpose of getting the data from the API and storing it in the database
in a raw format to be actively used by the program. 

'''


# Asset order: btc, xrp, ltc, xlm(str for coinspot), ada
# Create and connect to database and create tables if they dont already exist

def start_tempdb():
    
    try:
        conn = sqlite3.connect('raw_data.db')
        cursor = conn.cursor()
        print('Database Connection Successful')
    except:
        print('Database Error:', error)
        exit
    
    # Create Tables for the database
    cursor.execute('''CREATE TABLE IF NOT EXISTS btc(
        data_id TEXT PRIMAY KEY,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS xrp(
        data_id TEXT PRIMAY KEY,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ltc(
        data_id TEXT PRIMAY KEY,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS xlm(
        data_id TEXT PRIMAY KEY,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ada(
        data_id TEXT PRIMAY KEY,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL);
    ''')


'''
Getting data from API and saving to database, will use seperate function for each asset to allow
simultaneous execution with multiple threads.

'''

# BTC Data 
def getdata_btc():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('btc', 'ask')
    sell_coinspot = fn.getprice_coinspot('btc', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('BTC', 'buy')
    sell_swiftx = fn.getprice_swiftx('BTC', 'sell')

    #Coinjar Data
    buy_coinjar = fn.getprice_coinjar('BTC', 'ask')
    sell_coinjar = fn.getprice_coinjar('BTC', 'bid')

# XRP Data
def getdata_xrp():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('xrp', 'ask')
    sell_coinspot = fn.getprice_coinspot('xrp', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('XRP', 'buy')
    sell_swiftx = fn.getprice_swiftx('XRP', 'sell')

    #Coinjar Data
    buy_coinjar = fn.getprice_coinjar('xrp', 'ask')
    sell_coinjar = fn.getprice_coinjar('xrp', 'bid')

# LTC Data
def getdata_ltc():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('ltc', 'ask')
    sell_coinspot = fn.getprice_coinspot('ltc', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('LTC', 'buy')
    sell_swiftx = fn.getprice_swiftx('LTC', 'sell')

    #Coinjar Data
    buy_coinjar = fn.getprice_coinjar('ltc', 'ask')
    sell_coinjar = fn.getprice_coinjar('ltc', 'bid')

#XLM Data
def getdata_xlm():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('str', 'ask')
    sell_coinspot = fn.getprice_coinspot('str', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('XLM', 'buy')
    sell_swiftx = fn.getprice_swiftx('XLM', 'sell')

    #Coinjar Data
    buy_coinjar = fn.getprice_coinjar('xlm', 'ask')
    sell_coinjar = fn.getprice_coinjar('xlm', 'bid')

#ADA Data (Coinjar doesn't list ADA)

def getdata_ada():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('ada', 'ask')
    sell_coinspot = fn.getprice_coinspot('ada', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('ADA', 'buy')
    sell_swiftx = fn.getprice_swiftx('ADA', 'sell')



