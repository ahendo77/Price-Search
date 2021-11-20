from os import error
from sqlite3.dbapi2 import DatabaseError 
import sqlite3
import time
import functions as fn

'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.0

GET file holds database connection and functions to request pricing
data and write to the database.

'''

# Asset order: btc, xrp, ltc, xlm(str for coinspot), ada
# Create and connect to database and create tables if they dont already exist

def start_rawdb():
    try:
        global cursor
        global conn
        conn = sqlite3.connect('raw_data.db')
        cursor = conn.cursor()
        print('Live Price Connection 1 Successful')
        time.sleep(0.3)
    except:
        print('Database Error:', error)
        exit()
  
    
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


#Here for testing
#start_rawdb()

'''

Threads make request for market data for each asset and write it to the database.

'''

def btc_thread():
    # Threading module throws an error when sharing sql connections so will need a seperate one in each thread
    conn_btc = sqlite3.connect('raw_data.db')
    cursor_btc = conn_btc.cursor()

    while True:
        list = fn.getdata_btc()
        data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        cursor_btc.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?, ?)", (data_id, list[0], list[1], list[2], list[3], list[4], list[5]))
        conn_btc.commit()

def xrp_thread():
    conn_xrp = sqlite3.connect('raw_data.db')
    cursor_xrp = conn_xrp.cursor()

    while True:
        list = fn.getdata_xrp()
        data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        cursor_xrp.execute("INSERT INTO xrp VALUES (?, ?, ?, ?, ?, ?, ?)", (data_id, list[0], list[1], list[2], list[3], list[4], list[5]))
        conn_xrp.commit()

def ltc_thread():
    conn_ltc = sqlite3.connect('raw_data.db')
    cursor_ltc = conn_ltc.cursor()

    while True:
        list = fn.getdata_ltc()
        data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        cursor_ltc.execute("INSERT INTO ltc VALUES (?, ?, ?, ?, ?, ?, ?)", (data_id, list[0], list[1], list[2], list[3], list[4], list[5]))
        conn_ltc.commit()

def xlm_thread():
    conn_xlm = sqlite3.connect('raw_data.db')
    cursor_xlm = conn_xlm.cursor()

    while True:
        list = fn.getdata_xlm()
        data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        cursor_xlm.execute("INSERT INTO xlm VALUES (?, ?, ?, ?, ?, ?, ?)", (data_id, list[0], list[1], list[2], list[3], list[4], list[5]))
        conn_xlm.commit()

def ada_thread():
    conn_ada = sqlite3.connect('raw_data.db')
    cursor_ada = conn_ada.cursor()

    while True:
        list = fn.getdata_ada()
        data_id = time.strftime("%Y-%m-%d %H:%M:%S")
        cursor_ada.execute("INSERT INTO ada VALUES (?, ?, ?, ?, ?)", (data_id, list[0], list[1], list[2], list[3]))
        conn_ada.commit()

# Here for testing
#while True:
#btc_thread()
