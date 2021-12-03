from main import *
import main as m
import functions as fn
import signal
import logging

'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.1

RUN File serves to start program and define exit handler,
stopping threads and search when user wishes to stop.

'''

# Exit handler will need to stop all threads
def exit_handler(signum, frame):
    while True:
        logging.root.setLevel(logging.WARNING)
        fn.message()
        print('Are you sure you want to exit? y/n')
        if fn.user_query(input()) == True:
            print('\nView Discrepancy.db for results')
            print('\nExiting...')
            time.sleep(2.5)
            exit()
        else:
            message()
            logging.root.setLevel(logging.INFO)
            print('\nNow Searching...\n')
            break

signal.signal(signal.SIGINT, exit_handler)

if __name__ == '__main__':
    m.start()
    
