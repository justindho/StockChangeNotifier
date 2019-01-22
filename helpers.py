# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:13:25 2019

@author: Justin Ho

Environmental variables: TWILIO_ACCOUNT_SID, auth_token
"""

import requests
import urllib.parse
import sqlite3 as sql
import os
from twilio.rest import Client
import json
#from bs4 import BeautifulSoup as soup

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['auth_token']

client = Client(account_sid, auth_token)

# to add authenticated phone numbers to send to, add phone no. at url below
# https://www.twilio.com/console/phone-numbers/verified
phone_no_to = '+19252090927'
phone_no_from = '+14086755247'

def get_symbols():
    """Returns a tuple of all valid stock market tickers and how many there are"""
    try:
        response = requests.get(f"https://api.iextrading.com/1.0/ref-data/symbols")
        response.raise_for_status()
        ticker_list = json.loads(response.text) # convert string into list of dicts
        symbol_list = []
        for ticker in ticker_list:
            symbol_list.append(ticker['symbol'])
        num_tickers = len(symbol_list)
        return (set(symbol_list), num_tickers)
        
    except requests.RequestException:
        print('Unable to retrieve ticker symbols.')
        return None

def lookup(symbol):
    """ Look up quote for symbol.
        :param symbol: ticker symbol to lookup
        :return: dictionary of ticker symbol's name, price, and symbol
    """
    
    # Contact API
    try:
        response = requests.get(f"https://api.iextrading.com/1.0/stock/{urllib.parse.quote_plus(symbol)}/quote")
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    # Parse response
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
    """ Format value as USD """
    return f"${value:,.2f}"  

def create_connection(db_file):
    """ Create a connection to the chosen SQLite database specified by the
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
    """ Commit changes and close a connection to a SQLite database specified by
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

def send_sms(body):
    """ Send a SMS to the listed phone number to notify them of a ticker(s) 
        price change that exceeds the user's defined limits
        :param body: string object that contains the message to be sent
    """
    client.messages.create(
            to=phone_no_to, 
            from_=phone_no_from,
            body=body)
    