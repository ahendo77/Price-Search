from main import *
import main as m
import functions as fn
import signal

'''
Price-Search Copyright (C) 2021 Alex Henderson
Version Alpha 2.0.0

RUN File serves to start program and define exit handler,
stopping threads and search when user wishes to stop.

'''


def exit_handler(signum, frame):
    
    question = input('\nFinish now? y/n\n')
    while True:
        if question == 'y' or question == 'Y':
            break
        elif question == 'n' or question == 'n':
            print('Now Searching...\n')
            return None
        else:
            print('Please enter y or n')
            question = input()
            continue
    time.sleep(2)
    exit(0)

signal.signal(signal.SIGINT, exit_handler)

if __name__ == '__main__':
    m.main()
    
