from os import error
from sqlite3.dbapi2 import DatabaseError
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
        global cursor
        global conn
        conn = sqlite3.connect('raw_data.db')
        cursor = conn.cursor()
        print('Database Connection Successful')
    except:
        print('Database Error:', error)
        exit
    
    # Create Tables for the database
    cursor.execute('''CREATE TABLE IF NOT EXISTS btc(
        data_id TEXT PRIMAY KEY,
        request_number INT,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS xrp(
        data_id TEXT PRIMAY KEY,
        request_number INT,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ltc(
        data_id TEXT PRIMAY KEY,
        request_number INT,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS xlm(
        data_id TEXT PRIMAY KEY,
        request_number INT,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL,
        market_coinjar_buy REAL,
        market_coinjar_sell REAL);
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ada(
        data_id TEXT PRIMAY KEY,
        request_number INT,
        market_coinspot_buy REAL,
        market_coinspot_sell REAL,
        market_swiftx_buy REAL,
        market_swiftx_sell REAL);
    ''')

#Here for testing
start_tempdb()

'''
Getting data from API and saving to database, will use seperate function for each asset to allow
simultaneous execution with multiple threads.

'''

# BTC Data 
def getdata_btc():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('btc', 'ask') #Calls function from functions.py
    sell_coinspot = fn.getprice_coinspot('btc', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('BTC', 'buy')
    sell_swiftx = fn.getprice_swiftx('BTC', 'sell')

    #Coinjar Data
    buy_coinjar = fn.getprice_coinjar('BTC', 'ask')
    sell_coinjar = fn.getprice_coinjar('BTC', 'bid')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

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

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

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

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

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

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx, buy_coinjar, sell_coinjar]
    return list

#ADA Data (Coinjar doesn't list ADA)

def getdata_ada():
    #Coinspot Data
    buy_coinspot = fn.getprice_coinspot('ada', 'ask')
    sell_coinspot = fn.getprice_coinspot('ada', 'bid')

    #Swiftx Data
    buy_swiftx = fn.getprice_swiftx('ADA', 'buy')
    sell_swiftx = fn.getprice_swiftx('ADA', 'sell')

    list = [buy_coinspot, sell_coinspot, buy_swiftx, sell_swiftx]
    return list

'''
Central program function uses threading to make requests for all markets/assets
and write results to database simultaneously.

'''
# This will be useful later: data_id = time.strftime("%Y-%m-%d %H:%M:%S")

# System for tracking request cycles is ticker that counts up with each thread and writes the new number to the database column on completion    

def main_get():
    
    #This is a placeholder will need to change once complete structure is worked out
    def btc_thread():
        list = getdata_btc()
        #data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        #cursor.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (data_id,1, list[0], list[1], list[2], list[3], list[4], list[5]))
        #conn.commit()
        return list

    def xrp_thread():
        list = [True, getdata_xrp()]
        #data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        #cursor.execute("INSERT INTO xrp VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (data_id,1, list[0], list[1], list[2], list[3], list[4], list[5]))
        #conn.commit()
        return list
    
    def ltc_thread():
        list = [True, getdata_ltc()]
        #data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        #cursor.execute("INSERT INTO ltc VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (data_id,1, list[0], list[1], list[2], list[3], list[4], list[5]))
        #conn.commit()
        return list
    
    def xlm_thread():
        list = [True, getdata_xlm()]
        #data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        #cursor.execute("INSERT INTO xlm VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (data_id,1, list[0], list[1], list[2], list[3], list[4], list[5]))
        #conn.commit()
        return list
    
    def ada_thread():
        list = [True, getdata_ada()]
        #data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        #cursor.execute("INSERT INTO ada VALUES (?, ?, ?, ?, ?, ?)", (data_id,1, list[0], list[1], list[2], list[3]))
        #conn.commit()
        return list 
    
    #t1 = threading.Thread(target=btc_thread)
    #t2 = threading.Thread(target=xrp_thread)
    #t3 = threading.Thread(target=ltc_thread)
    #t4 = threading.Thread(target=xlm_thread)
    #t5 = threading.Thread(target=ada_thread)

    def main_thread():
        pass


    #Here for testing
    btc_thread()

#Here for testing 
main_get()    
