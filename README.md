# StockChangeNotifier
This program, at its completion, will notify the user via text message when a ticker symbol's price in the stock market changes by a user-defined percentage.
## Setup
Use [pip](https://pip.pypa.io/en/stable/) to install the following packages if not already installed on your computer.
```
pip install tkinter 
pip install threading
pip install requests
pip install twilio
pip install sqlite3
pip install urllib
pip install os
pip install json
```
To receive text messages, you will need to create a [Twilio](https://www.twilio.com/try-twilio) account. Once you get your Twilio phone number, you will need to make some modifications to ```helpers.py```. 
In lines 28-29, update the following:
```
phone_no_to = '1234567890'  # the number you want to send notifications to
phone_no_from = '1098765432'  # your Twilio phone number
```
Keep in mind that with the trial version of Twilio, you will only be able to sends text messages to [verified numbers](https://www.twilio.com/console/phone-numbers/verified).
## Usage
In your command propmt (Windows key + 'r'), run stock_notification.py
```
python stock_notification.py
```
## Home Screen
![Home Screen](/Images/Home.png)
## Adding a Ticker to Your Watchlist
![Adding a Ticker to Your Watchlist](/Images/Stock_Info.png)
## Watchlist
![Watchlist](/Images/Watchlist.png)
## SMS Notification
![SMS Notification](/Images/sms.PNG)
## License
[MIT](https://choosealicense.com/licenses/mit/)
## Project Status
The project is still a work in progress. The foundation has been laid, but there is still functionality and user interface that I am tweaking in my spare time to make for a better user experience.
## Contact Information
If you have suggestions on how to improve this application, please email Justin Ho at <justinho515@gmail.com>.
