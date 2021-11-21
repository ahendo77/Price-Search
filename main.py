import check as check
import get as get
import functions as fn
import threading 
import time 
import sqlite3
import os
import platform

'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.0

MAIN file organises threading to use functions in GET and CHECK
to simultaneously perfom all program functions. Including: 
writing live pricing data to raw.db and actively checking live
raw.db to find discrepancies and write to new database. 

'''

# This section covers inital startup and Menu selection
# os.system('cmd') to perform system commands

# Program name and version to be displayed at all times

global os_name
os_name = platform.system()

def message():
    if os_name == 'Windows':
        os.system('cls')
        print('Price-Search (C) 2021 Alex Henderson','\nV2.0.0 Alpha')
    elif os_name == 'Linux':
        os.system('clear')
        print('Price-Search (C) 2021 Alex Henderson','\nV2.0.0 Alpha')

# Serve as general program start function (maybe?)
def start(): 
    message()

    # Later versions will inlcude options to view database data and perfom basic analysis
    while True:
        print('\nPlease select desired option:\n', '\n1. Live Search')
        response = int(input())
        if response == 1:
            live_search_selected()
            break
        else:
            continue
    

def live_search_selected():
    message()

    #Control Flow here, confirms user choices, checks API Database Connection
    # Confirms Choice with query function

    print('\nLive Search Selected\n', '\nBegin Now? y/n')
    if fn.user_query(input()) == True:
        pass
    else:
        start()
    
    # Check Market API Status
    message()
    print('\nChecking Market API Status...')
    fn.checkstatus_marketapi()
    print('\nSuccess!')
    time.sleep(2.5)

    #Establish Database Connection
    message()
    print('\nEstablishing Database Connection...\n')
    time.sleep(0.5)
    get.start_rawdb()
    check.connect_liveprices()
    check.start_discrepancydb()
    print('\nSuccess!')
    time.sleep(2.5)
    live_search_thread()

'''

Main program with threading organisation is written
in these functions here.

'''

# Live Price threading function 
#codes = btc, xrp, ltc, xlm(str for coinspot), ada

def live_search_thread():
    message()
    print('\nLive Price Threads Starting...')

    #Creating threads to get prices for each coin
    try:
        btcthread_get = threading.Thread(target=get.btc_thread)
        btcthread_get.start()
        print('\nBTC Live Price Thread Now Working')
    except:
        print('\nBTC Live Price Thread Error', '\nExiting...')
        exit()
    
    try:
        xrpthread_get = threading.Thread(target=get.xrp_thread)
        xrpthread_get.start()
        print('XRP Live Price Thread Now Working')
    except:
        print('\nXRP Live Price Thread Error', '\nExiting...')
        exit()

    try:
        ltcthread_get = threading.Thread(target=get.ltc_thread)
        ltcthread_get.start()
        print('LTC Live Price Thread Now Working')
    except:
        print('\nLTC Live Price Thread Error', '\nExiting...')
        exit()
    
    try:
        xlmthread_get = threading.Thread(target=get.xlm_thread)
        xlmthread_get.start()
        print('XLM Live Price Thread Now Working')
    except:
        print('\nXLM Live Price Thread Error', '\nExiting...')
        exit()

    try:
        adathread_get = threading.Thread(target=get.ada_thread)
        adathread_get.start()
        print('ADA Live Price Thread Now Working')
    except:
        print('\nADA Live Price Thread Error', '\nExiting...')
        exit()
    live_check_thread()

def live_check_thread():
    message()
    print('\nLive Check Threads Now Starting')

    # Creating Threads to Check with each coin

    try:
        btcthread_check = threading.Thread(target=check.check_btc)
        btcthread_check.start()
        print('BTC Check Thread Now Working')
    except:
        print('\nBTC Check Thread Error', '\nExiting...')
        exit()
    
    try:
        xrpthread_check = threading.Thread(target=check.check_xrp)
        xrpthread_check.start()
        print('XRP Check Thread Now Working')
    except:
        print('\nXRP Check Thread Error', '\nExiting...')
        exit()
    
    try:
        ltcthread_check = threading.Thread(target=check.check_ltc)
        ltcthread_check.start()
        print('LTC Check Thread Now Working')
    except:
        print('\nLTC Check Thread Error', '\nExiting...')
        exit()
    
    try:
        xlmthread_check = threading.Thread(target=check.check_xlm)
        xlmthread_check.start()
        print('XLM Check Thread Now Working')
    except:
        print('\nXLM Check Thread Error', '\nExiting...')
        exit()
    
    try:
        adathread_check = threading.Thread(target=check.check_ada)
        adathread_check.start()
        print('ADA Check Thread Now Working')
    except:
        print('\nADA Check Thread Error', '\nExiting...')
        exit()







#Here for testing
start()