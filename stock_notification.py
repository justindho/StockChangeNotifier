# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:14:49 2019

@author: Justin Ho

This script notifies the user when their chosen stock tickers change in price 
by more than a user-specified percentage.
"""

try:
    #for Python2
    import Tkinter as tk
except ImportError:
    #for Python3
    import tkinter as tk

#import library for sending push notifications to browser, Android, or iOS 
    #and/or Windows 10 device
#from pushsafer import init, Client    



#YAHOO STOCKS API



class GUI:
    def __init__(self):
        #configure the root window
        self.root = tk.Tk()
        self.root.title('Stock Change Notifier')
#        self.root.configure(bg='green')
        
        #set window size
        self.root_width = self.root.winfo_screenwidth()
        self.root_height = self.root.winfo_screenheight()
        self.root.geometry('{}x{}'.format(self.root_width, self.root_height))
        
        #create all of the main containers
        self.top_row = tk.Frame(self.root, width=self.root_width, height=500, bg='red')
        self.mid_row = tk.Frame(self.root, width=self.root_width, height=500, bg='blue')
        self.bot_row = tk.Frame(self.root, width=self.root_width, height=500, bg='green')
        
        #layout all of the main containers
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.top_row.grid(row=0, columnspan=2)
        self.mid_row.grid(row=1)
        self.bot_row.grid(row=2)
        
        #create the widgets for the top row
        self.see_stock_list_button = tk.Button(self.top_row, \
                                               text='See Stock List', \
                                               font='14', \
                                               activebackground='blue', bd=2, \
                                               bg='grey', fg='black', \
                                               justify='center', padx=1000)
        
        #layout the widgets in the top row
        self.see_stock_list_button.grid(row=0, sticky='nsew')
        
        #create the widgets for the middle row
        self.add_ticker_label = tk.Label(self.mid_row, text='Add Ticker: ')
        self.add_ticker_entry = tk.Entry(self.mid_row, justify='left', \
                                         takefocus='on')
        self.add_price_label = tk.Label(self.mid_row, text='Add Price: ')
        self.add_price_entry = tk.Entry(self.mid_row, justify='left', \
                                         takefocus='on')
        self.percent_change_label = tk.Label(self.mid_row, \
                                             text='% Change to Notify')
        self.percent_change_entry = tk.Entry(self.mid_row, justify='left')
        
        #layout the widgets for the middle row
        self.add_ticker_label.grid(row=0, column=0)
        self.add_ticker_entry.grid(row=0, column=1)
        self.add_price_label.grid(row=1, column=0)
        self.add_price_entry.grid(row=1, column=1)
        self.percent_change_label.grid(row=2, column=0)
        self.percent_change_entry.grid(row=2, column=1)
        
        #create the widgets for the bottom row
        self.remove_ticker_button = tk.Button(self.bot_row, \
                                              text='Remove Ticker', font='14', \
                                              activebackground='blue', bd=2, \
                                              bg='grey', fg='black', \
                                              justify='center')
        
        #layout the widgets for the bottom row
#        self.remove_ticker_button.grid(row=0, sticky='nsew')
        
if __name__ == '__main__':        
    app = GUI()
    app.root.mainloop()