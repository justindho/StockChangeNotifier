            # -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:14:49 2019

@author: Justin Ho

This script notifies the user when their chosen stock tickers change in price 
by more than a user-specified percentage.
"""
                                                                                                                
import GUI
import helpers
import sqlite3 as sql

#import library for sending push notifications to browser, Android, or iOS 
    #and/or Windows 10 device
#from pushsafer import init, Client    
  
if __name__ == '__main__':  
    connection = sql.connect('tickers.db')
    cursor= connection.cursor()
    create_sql_db = """
    CREATE TABLE symbols (
    ticker_number INTEGER PRIMARY KEY, 
    ticker TEXT, 
    price REAL);"""           
    cursor.execute(create_sql_db)

                                                                                     
    app = GUI.GUI()
    app.root.mainloop()