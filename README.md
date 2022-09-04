# StockPriceAlert
Get an alert on your email when your stock hits the target price


With the help of web scraping, the price of the stock is scraped every x minutes (x being the time set by the user), which if becomes equal to or less than the target price, sends an email notification to the user-specified email.


Some features that I tried to take care of to make the code more dynamic, and also make more sense:-
  1. User has to enter the sender email ID and the password, along with the receiver email ID just once (until the      program is terminated).
  2. The price, and duration of data collection, can be set by the user so that it works uniquely for every user.
  3. It collects the information ONLY when during the Trading time.


The data also gets stored in a csv file, everytime it is collected.
The images attached include:-
  1. A snippet of what it looks like once the code is run.
  2. Excel data of the collected information.	
  3. E-mail notification.
  
  
- The currency in the email needs to be USD instead of INR
