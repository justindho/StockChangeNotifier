# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:13:25 2019

@author: Justin Ho
"""

import requests
import urllib.parse
import sqlite3 as sql

def lookup(symbol):
    """Look up quote for symbol.
    :param symbol: ticker symbol to lookup
    :return: dictionary of ticker symbol's name, price, and symbol
    """
    
    #Contact API
    try:
        response = requests.get(f"https://api.iextrading.com/1.0/stock/{urllib.parse.quote_plus(symbol)}/quote")
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    #Parse response
    try:
        quote = response.json()
        return {
                "name": quote["companyName"],
                "price": float(quote["latestPrice"]),
                "symbol": quote["symbol"]
                }
    except (KeyError, TypeError, ValueError):
        return None
          
def usd(value):
    """Format value as USD"""
    return f"${value:,.2f}"  

def create_connection(db_file):
    """ create a connection to the chosen SQLite database specified by the
        db_file
        :param db_file: database file
        :return: Connection object or None
    """
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return None

def close_connection(connection):
    """ commit changes and close a connection to a SQLite database specified by
        the connection object to that database
        :param connection: connection object to a SQLite database
        :return: None
    """
    try:
        connection.commit()
        connection.close()
    except Error as e:
        print(e)
        
    return None  