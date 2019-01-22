# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:14:49 2019

@author: Justin Ho

This script notifies the user when their chosen stock tickers change in price 
by more than a user-specified percentage.
"""
                                                                                                                
import GUI
from helpers import create_connection, close_connection
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

    #run GUI application                                                                                     
    app = GUI.GUI()
    app.root.mainloop()