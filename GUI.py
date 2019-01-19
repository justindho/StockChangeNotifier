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

class GUI:
    def __init__(self):
        #configure the root window
        self.root = tk.Tk()
        self.root.title('Stock Change Notifier')
#        self.root.configure(bg='green')
        
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
                                               text='See Stock List', \
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
        self.percent_change_label = tk.Label(self.mid_row, font='Times 20', \
                                             text='% Change to Notify: ', \
                                             justify='left')
        self.percent_change_entry = tk.Entry(self.mid_row, justify='left', \
                                             font='Times 20', takefocus=1)
        
        #layout the widgets for the middle row
        self.add_ticker_label.grid(row=0, column=0, sticky='we')
        self.add_ticker_entry.grid(row=0, column=1, sticky='we')
        self.add_price_label.grid(row=1, column=0, sticky='we')
        self.add_price_entry.grid(row=1, column=1, sticky='we')
        self.percent_change_label.grid(row=2, column=0, sticky='we')
        self.percent_change_entry.grid(row=2, column=1, sticky='we')
        
        #create the widgets for the bottom row
        self.add_ticker_button = tk.Button(self.bot_row, \
                                              text='Add Ticker to List',  \
                                              font='Times 20', \
                                              activebackground='blue', bd=2, \
                                              bg='grey', fg='black', \
                                              justify='center', padx=1000, \
                                              pady=25, highlightthickness=10, \
                                              highlightcolor='red')
                                           
        self.remove_ticker_button = tk.Button(self.bot_row, \
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
        self.percent_change_entry.bind('<Tab>', focus_next_widget)
        self.add_ticker_button.bind('<Tab>', focus_next_widget)
        self.remove_ticker_button.bind('<Tab>', focus_next_widget)
        
        #set initial focus to see_stock_list_button
        self.see_stock_list_button.focus()   
        
        #add validation to Entry widgets
#        def isOkay(self, )
#        if len(self.add_ticker_entry.get()) == 0:
#            tk.messagebox.showerror('USER ERROR', 'Enter a symbol!')
        
#allow user to tab to next widget
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return('break')        