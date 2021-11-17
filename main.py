import check as check
import get as get
import threading 
import time 
import sqlite3

'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0

MAIN file organises threading to use functions in GET and CHECK
to simultaneously perfom all program functions. Including: 
writing live pricing data to raw.db and actively checking live
raw.db to find discrepancies and write to new database. 

'''

# Getting live pricing data

def get_live_data():
    pass