import main as m
import functions as fn


#Price Dicrepancy Search 
#Version Alpha 1.1.0 by Alex Henderson

if __name__ == '__main__':
    print('Price Discrepancy Search by Alex Henderson')
    print('V1.1.0 Alpha\n')
    print('Checking API Status...\n')
    fn.checkstatus_coinspot()
    fn.checkstatus_coinjar()
    fn.checkstatus_swiftx()
    fn.user_input()
    m.main()
