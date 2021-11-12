from os import error
import requests
import json 
import sqlite3
import time
import threading


def start_temp():
    try:
        sql_tempdb = sqlite3.connect(':memory:')
        cursor = sql_tempdb.cursor()
        print('sick')
    except:
        print('fuck')

def get_btc_data():
    pass


start_temp()