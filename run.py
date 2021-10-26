from main import *
import main as m
import functions as fn
import signal

#Price Dicrepancy Search 
#Version Alpha 1.1.0 by Alex Henderson


def exit_handler(signum, frame):
    print('Exiting...')
    print('Discrepancies found:', m.moderate_discrepancy)
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
    
