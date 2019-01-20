# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:13:35 2019

@author: Justin Ho
"""

try:
    #for Python2
    import Tkinter as tk
except ImportError:
    #for Python3
    import tkinter as tk
    from tkinter import messagebox
    
from helpers import lookup, usd, create_connection, close_connection

class GUI:
    def __init__(self):
        #configure the root window
        self.root = tk.Tk()
        self.root.title('Stock Change Notifier')
        
        #set window size
        (w, h) = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        
        #create all of the main containers
        self.top_row = tk.Frame(self.root, width=w, height=100, bd=10, bg='red')
        self.mid_row = tk.Frame(self.root, width=w, height=100, bd=10, bg='blue')
        self.bot_row = tk.Frame(self.root, width=w, height=100, bd=10, bg='green')
        
        #layout all of the main containers
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.top_row.grid(row=0, columnspan=3)
        self.mid_row.grid(row=1, columnspan=3)
        self.bot_row.grid(row=2, columnspan=3)
        
        #create the widgets for the top row
        self.see_stock_list_button = tk.Button(self.top_row, \
                                               command=self.see_list, \
                                               text='See Stock Watchlist', \
                                               font='Times 20', \
                                               activebackground='blue', bd=2, \
                                               bg='grey', fg='black', \
                                               highlightthickness=10, \
                                               highlightcolor='red')
        
        #layout the widgets in the top row
        self.see_stock_list_button.grid(row=0, sticky='we')
        
        #create the widgets for the middle row
        self.add_ticker_label = tk.Label(self.mid_row, text='Ticker Symbol: ', \
                                         font='Times 20')
        self.add_ticker_entry = tk.Entry(self.mid_row, justify='left', \
                                         font='Times 20', takefocus=1)
        self.add_price_label = tk.Label(self.mid_row, text='Price: ', \
                                        font='Times 20', justify='left')
        self.add_price_entry = tk.Entry(self.mid_row, justify='left', \
                                         font='Times 20', takefocus=1)
        self.get_current_price_button = tk.Button(self.mid_row, \
                                                  command=self.lookup_current_price, \
                                                  text='Get Current Price', \
                                                  font='Times 20', bd=2, \
                                                  activebackground='blue', \
                                                  bg='grey', fg='black', \
                                                  justify='center', padx=5, \
                                                  highlightthickness=10, \
                                                  highlightcolor='red')
        self.percent_inc_label = tk.Label(self.mid_row, font='Times 20', \
                                          text='% Increase to Notify: ', \
                                          justify='left')
        self.percent_inc_entry = tk.Entry(self.mid_row, justify='left', \
                                          font='Times 20', takefocus=1)
        self.percent_dec_label = tk.Label(self.mid_row, font='Times 20', \
                                          text='% Decrease to Notify: ', \
                                          justify='left')
        self.percent_dec_entry = tk.Entry(self.mid_row, justify='left', \
                                          font='Times 20', takefocus=1)
        
        #allow execution of get_current_price_button on 'Enter'
        self.get_current_price_button.bind('<Return>', self.lookup_current_price)
        
        #layout the widgets for the middle row
        self.add_ticker_label.grid(row=0, column=0, sticky='we')
        self.add_ticker_entry.grid(row=0, column=1, sticky='we')
        self.add_price_label.grid(row=1, column=0, sticky='we')
        self.add_price_entry.grid(row=1, column=1, sticky='we')
        self.get_current_price_button.grid(row=1, column=2, sticky='we')
        self.percent_inc_label.grid(row=2, column=0, sticky='we')
        self.percent_inc_entry.grid(row=2, column=1, sticky='we')
        self.percent_dec_label.grid(row=3, column=0, sticky='we')
        self.percent_dec_entry.grid(row=3, column=1, sticky='we')
        
        #create the widgets for the bottom row
        self.add_ticker_button = tk.Button(self.bot_row, \
                                           command=self.ticker2list, \
                                           text='Add Ticker to List',  \
                                           font='Times 20', \
                                           activebackground='blue', bd=2, \
                                           bg='grey', fg='black', \
                                           justify='center', padx=1000, \
                                           pady=25, highlightthickness=10, \
                                           highlightcolor='red')
                                           
        self.remove_ticker_button = tk.Button(self.bot_row, \
                                              command=self.remove_ticker, \
                                              text='Remove Ticker from List',  \
                                              font='Times 20', \
                                              activebackground='blue', bd=2, \
                                              bg='grey', fg='black', \
                                              justify='center', padx=1000, \
                                              pady=25, highlightthickness=10, \
                                              highlightcolor='red')
        
        #layout the widgets for the bottom row
        self.add_ticker_button.grid(row=0, sticky='we')
        self.remove_ticker_button.grid(row=1, sticky='we')
        
        #allow user to tab to next widget
        self.see_stock_list_button.bind('<Tab>', focus_next_widget)
        self.add_ticker_entry.bind('<Tab>', focus_next_widget)
        self.add_price_entry.bind('<Tab>', focus_next_widget)
        self.get_current_price_button.bind('<Tab>', focus_next_widget)
        self.percent_inc_entry.bind('<Tab>', focus_next_widget)
        self.percent_dec_entry.bind('<Tab>', focus_next_widget)
        self.add_ticker_button.bind('<Tab>', focus_next_widget)
        self.remove_ticker_button.bind('<Tab>', focus_next_widget)
        
        
        #set initial focus to add_ticker_entry
        self.add_ticker_entry.focus()  
        
    def lookup_current_price(self):
        """Handle get_current_price_button button click to get stock price. 
        Will return error message upon invalid ticker symbol or empty string
        """
        try:
            symbol = self.add_ticker_entry.get()
            self.add_price_entry.delete(0, 'end')
            self.add_price_entry.insert(0, lookup(symbol)['price'])
        except TypeError:
            tk.messagebox.showinfo('ERROR: INVALID TICKER SYMBOL', \
                                    'User must enter a valid ticker symbol.')
    def ticker2list(self):
        """Add ticker to stock watchlist"""
        try:
            symbol = self.add_ticker_entry.get().upper()
        except ValueError:
            pass            
        try:
            pct_inc = float(self.percent_inc_entry.get())
        except ValueError:
            pass
        try:
            pct_dec = float(self.percent_dec_entry.get())
        except ValueError:
            pass
        try:
            price = float(self.add_price_entry.get())
            price_low = price * (1 - pct_dec/100)
            price_high = price * (1 + pct_inc/100)
        except (ValueError, UnboundLocalError):
            pass
        if len(symbol) == 0 or not price or not pct_dec or not pct_inc:
            tk.messagebox.showinfo('ERROR: MISSING REQUIRED FIELDS', \
                                   "'Ticker Symbol', 'Price', and '% Change to"
                                   " notify are required fields.")
        else: #add ticker to tickers.db
            db = create_connection('tickers.db')
            cursor = db.cursor()    #create cursor to traverse tickers.db
            cursor.execute("""INSERT INTO symbols (ticker, price, pct_dec, pct_inc,
            price_low, price_high) VALUES (?, ?, ?, ?, ?, ?);""", \
            (symbol, price, pct_dec, pct_inc, price_low, price_high)) #add changes for commital
            
            close_connection(db)
            
    
    def remove_ticker(self):
        """Remove ticker from stock watchlist"""
        symbol = self.add_ticker_entry.get().upper()
        db = create_connection('tickers.db')
        cursor = db.cursor()
        cursor.execute("""SELECT count(*) FROM symbols WHERE ticker=?""", (symbol,))
        data = cursor.fetchone()[0]
        
        if data == 0:
            tk.messagebox.showinfo("REMOVAL ERROR", \
                                   "Ticker doesn't exist in your watchlist.")
        else:
            cursor.execute("DELETE FROM symbols WHERE ticker=?;", (symbol,))
        
        close_connection(db)          
        
    
    def see_list(self):
        """Creates table of watchlist to present to the user"""
        top = tk.Toplevel()
        top.title('Your watchlist')        
        (w, h) = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        top.geometry('{}x{}'.format(w, h))
        
        #create containers for widgets
        top_row = tk.Frame(top, width=w, height=round(h*.075), bg='blue')
        mid_row = tk.Frame(top, width=w, height=round(h*.75), bg='green')
        bot_row = tk.Frame(top, width=w, height=round(h*.075), bg='red')
        
        #layout containers
        top.grid_rowconfigure(0, weight=1)
        top.grid_rowconfigure(1, weight=1)
        top.grid_columnconfigure(0, weight=1)
        top.grid_columnconfigure(1, weight=0)
        top_row.grid(row=0, columnspan=1)
        mid_row.grid(row=1, columnspan=1)
        bot_row.grid(row=2, columnspan=1)
        
        #open connection to tickers.db
        db = create_connection('tickers.db')
        cursor = db.cursor()
        
        #create widgets for displaying ticker watchlist
        cursor.execute("""SELECT COUNT(*) FROM symbols""")
        num_rows = cursor.fetchone()[0]
        cursor.execute("""SELECT * FROM symbols""")
        col_names = [name[0] for name in cursor.description] #get column headers
        col_names = list(map(lambda x:x.upper(), col_names)) #convert headers to uppercase
        num_cols = len(col_names)
        
        #create "table" of user's watchlist for display
        title = tk.Label(top_row, text='Your Watchlist', font='Times 40', bd=10, \
                         fg='black', bg='green', relief='raised')
        title.grid(row=0)
        for col_name in range(num_cols):
            h = tk.Label(mid_row, text=col_names[col_name], font='Times 20', \
                         fg='black', bg='yellow', relief='sunken', bd=3)
            h.grid(row=0, column=col_name)
        cursor.execute("""SELECT ticker FROM symbols""")
        portfolio = cursor.fetchall()        
        for row in range(num_rows):
            ticker = portfolio[row][0]
            cursor.execute("""SELECT * FROM symbols WHERE ticker=?""", (ticker,))
            ticker_info = cursor.fetchall()
            for col in range(num_cols):                                
                text = ticker_info[0][col]
                b = tk.Label(mid_row, text=text, bd=1, fg='black', \
                             font='Times 20', bg='yellow', relief='sunken', \
                             padx=20, pady=10)
                b.grid(row=row+1, column=col)
        
        #create 'dismiss' button
        dismiss_button = tk.Button(bot_row, text='Dismiss', command=top.destroy, \
                                   font='Times 20', takefocus=1)
        #layout 'dismiss' button
        dismiss_button.grid(row=0)
        
        #save changes to tickers.db and close connection
        close_connection(db)
        
    
    def check_price(self, symbol):
        """Checks current ticker symbol price to see if price is outside 
        user-defined range
        """
        current_price = lookup(symbol)['price']
        db = create_connection('tickers.db')
        cursor = dbcursor()
        cursor.execute("""SELECT (price_low, price_high) FROM symbols 
                       WHERE symbol=?""", (symbol,))
        price_low, price_high = cursor.fetchone()[0], cursor.fetchone[1]
        if current_price < price_low:
            #TODO (twilio)
            #send user a notification that lower bound has been exceeded
            pass
        elif current_price > price_high:
            pass
            #TODO (twilio)
            #send user a notification that upper bound has been exceeded
            #does check_price need to run every second???? how to do this???
        
        close_connection(db)
        pass
        
        
def focus_next_widget(event):
    """allow user to tab to next widget"""
    event.widget.tk_focusNext().focus()
    event.bind('<FocusIn>', highlight_all)
    return('break')        
    
def highlight_all(event):
    """highlight all text in when tabbing into an Entry widget"""
    event.selection_range(0, 'end')

