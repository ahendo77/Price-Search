from main import *
import main as m
import functions as fn
import signal
import time 

#Price Dicrepancy Search 
#Version Alpha 1.1.0 by Alex Henderson


def exit_handler(signum, frame):
    print('Minor Descrepancies Found:', m.minor_discrepancy)
    print('Moderate Discrepancies found:', m.moderate_discrepancy)
    print('Searching Since:', m.start_time)
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
    print('Price Discrepancy Search by Alex Henderson')
    print('V1.1.0 Alpha\n')
    print('Checking API Status...\n')
    fn.checkstatus_coinspot()
    fn.checkstatus_coinjar()
    fn.checkstatus_swiftx()
    fn.user_input()
    m.main()
    
