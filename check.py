from os import error
import sqlite3
import time


'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0

CHECK file holds functions to actively search through
live price database and record descrepancies found to
a seperate database. 

'''

# Setting up database to store discrepancies
#codes = btc, xrp, ltc, xlm(str for coinspot), ada

def start_discrepancydb():
    try:
        global cursor
        global conn
        conn = sqlite3.connect('discrepancy_data.db')
        cursor = conn.cursor()
        print('Database Connection Successful')
    except:
        print('Error with database:', error)
        exit()

    # Creating tables for databse 

    cursor.execute('''CREATE TABLE IF NOT EXISTS btc(
        dataid TEXT PRIMARY KEY,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS xrp(
        dataid TEXT PRIMARY KEY,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS ltc(
        dataid TEXT PRIMARY KEY,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS xlm(
        dataid TEXT PRIMARY KEY,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT
        size_catagory TEXT);'''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS ada(
        dataid TEXT PRIMARY KEY,
        buy_price REAL,
        sell_price REAL,
        buy_market TEXT,
        sell_market TEXT
        size_catagory TEXT);'''
    )


# Check for and open connection to Live Price Database

def connect_liveprices():
    try:
        global session_start
        global conn_live
        global cursor_live
        session_start = time.strftime('%H:%M:%S')
        conn_live = sqlite3.connect('raw_data.db')
        cursor_live = conn_live.cursor()
        print('Live Price Database Connection Successful')
    except:
        print('Error with database:', error)
        exit()

#Here for testing
#connect_liveprices()

# Starts reading live price database
def start_reading():
    cursor_live.execute('SELECT * FROM btc ORDER BY data_id DESC') # ORDER BY Important to get most recent data
    rows = cursor_live.fetchall()

    for row in rows:
        print(row)

#start_reading()