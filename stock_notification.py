# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:14:49 2019

@author: Justin Ho

This script notifies the user when their chosen stock tickers change in price 
by more than a user-specified percentage.
"""

import yahoo_finance_pynterface as yf_py
import alpha_vantage as av
from helpers import lookup, usd
import GUI

#import library for sending push notifications to browser, Android, or iOS 
    #and/or Windows 10 device
#from pushsafer import init, Client    
  
if __name__ == '__main__':        
    quote = lookup('FB')
    print(usd(quote["price"]))
    app = GUI.GUI()
    app.root.mainloop()