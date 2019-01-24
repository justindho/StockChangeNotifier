# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:14:49 2019

@author: Justin Ho

This script notifies the user when their chosen stock tickers change in price 
by more than a user-specified percentage.
"""                                                                                                              

from helpers import (create_connection, close_connection)

from GUI import thread_run_GUI, thread_check_price, GUI

import os
  
if __name__ == '__main__':  
    # create SQLite3 database to store user's stock market information if not 
    # created already
    if not os.path.exists('tickers.db'):
        # create connection to database and create a table to store data
        db = create_connection('tickers.db')
        cursor= db.cursor()      
        create_sql_db = """
        CREATE TABLE symbols (
        ticker TEXT PRIMARY KEY, 
        price REAL,
        pct_dec REAL,
        pct_inc REAL,
        price_low REAL,
        price_high REAL);"""           
        cursor.execute(create_sql_db)
        close_connection(db)                
        
    # create new threads
#    thread1 = thread_run_GUI(1, 'GUI Thread', 1)
#    thread2 = thread_check_price(2, 'Check Ticker Prices', 2)
    
    # start new threads
#    thread1.start()
#    thread2.start()
    
#    print('Exiting main thread.\n')
    
    # run GUI application                                                                                     
#    app = GUI()
#    app.root.mainloop()
    
    app = GUI()
    app.run()