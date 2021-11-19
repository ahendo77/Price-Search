import check as check
import get as get
import functions as fn
import threading 
import time 
import sqlite3
import os

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
def message():
    print('Price-Search (C) 2021 Alex Henderson','\nV2.0.0 Alpha')


def start():
    os.system('cls')
    message()

    # Later versions will inlcude options to view database data and perfom basic analysis
    while True:
        print('\nPlease select desired option:\n', '\n1. Live Search')
        response = int(input())
        if response == 1:
            live_search()
            break
        else:
            continue
    

def live_search():
    os.system('cls')
    message()

    print('\nLive Search Selected', '\nBegin Now? y/n')
    if fn.user_query(input()) == True:
        pass
    else:
        start()
    
    
    
start()