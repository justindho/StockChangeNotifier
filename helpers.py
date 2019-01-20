# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:13:25 2019

@author: Justin Ho
"""

import requests
import urllib.parse

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

  