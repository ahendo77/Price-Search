import pyodbc

'''
Class will manage connections to SQL Server database.

'''

devmode = True


class SQLConnection:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None

    def connect():
        if devmode == True:
            try:
                conn = pyodbc.connect(
                driver = '{SQL Server}',
                Server = 'ALEX-DESKTOP-PC',
                Database = 'master',
                Trusted_Connection = 'yes',
                )
                print('Success')
            except:
                raise Exception('Error')
        else:
            print('DEVMODE OFF')
            exit()


SQLConnection.connect()
          

