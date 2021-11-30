from main import *
import main as m
import functions as fn
import signal
import logging

'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.0

RUN File serves to start program and define exit handler,
stopping threads and search when user wishes to stop.

'''

# Exit handler will need to stop all threads
def exit_handler(signum, frame):
    while True:
        logging.root.setLevel(logging.WARNING)
        fn.message()
        print('Are you sure you want to exit?')
        if fn.user_query(input()) == True:
            print('\nStopping Threads...')
            m.stop_threads()
            print('\nThreads Stopped', '\nNow Exiting view Discrepancy.db for results')
            time.sleep(2.5)
            print('\nExiting...')
            exit()
        else:
            message()
            logging.root.setLevel(logging.INFO)
            break

signal.signal(signal.SIGINT, exit_handler)

if __name__ == '__main__':
    while True:
        m.start()
    
