# import all the libraries required
import csv
import requests
import time
import datetime
import smtplib
import getpass
from bs4 import BeautifulSoup


def check_price():
    # scraping the name and price of the stock from Google
    def scrape(url_arg):
        url = url_arg
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/102.0.0.0 Safari/537.36'}
        req = requests.get(url, headers=headers)
        htmlContent = req.content

        soup = BeautifulSoup(htmlContent, 'html.parser')

        return soup

    soup = scrape('https://www.google.com/search?q=tata+stock')


    # Initializing variables using the data we scraped
    name = soup.find(class_="wx62f PZPZlf x7XAkb").get_text()
    current_price = soup.find(class_="IsqQVc NprOob wT3VGc").get_text()
    currency = soup.find(class_="knFDje").get_text()

    # Initializing time and date to be used in the csv file
    now = datetime.datetime.now()
    current_time = now.time()
    date = datetime.date.today()

    start = datetime.time(9, 15, 0)
    end = datetime.time(15, 30, 0)

    # Since the stock market is open for a certain time, we want to run the code during that time period only
    # This function returns True if the current time is in that range
    def time_in_range(start, end, current_time):
        return start <= current_time <= end


    # CSV file header and data
    header = ['Stock Name', 'Price', 'Currency', 'Time', 'Date']
    data = [name[5:], current_price, currency, current_time, date]

    # Appending new data to the CSV file
    with open('StockPrice.csv', "a+", newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    # Function to send an e-mail when current price is less than or equal to the target price
    def send_mail():
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, sender_pass)

        subject = f'{name} stock is below INR {target_price}, here is your chance to buy it for {current_price}'
        #   body = 'Go to groww now and invest in the stock'
        msg = f'Subject: {subject}'

        server.sendmail(sender_email, receiver_email, msg)

    if (current_price <= target_price):
        send_mail()

# Initializing the time
now = datetime.datetime.now()
start = datetime.time(9, 15, 0).strftime("%H:%M:%S")
end = datetime.time(15, 30, 0).strftime("%H:%M:%S")
current_time = now.strftime("%H:%M:%S")
print(current_time)

sender_email = input("Enter the sender e-mail: ")
sender_pass = getpass.getpass("Enter the password for this email: ")
receiver_email = input("Enter the receiver e-mail: ")

# Target stock price when we want to trigger the email
target_price = input("Enter the price: ")

#How often do you want it to run
interval = input("Enter, in minutes, how frequently you want the data: ")
time = interval*60

# Will check for the price once every hour between 9:15am and 3:30pm
while(time_in_range(start, end, current_time)):
    check_price()
    time.sleep(time)
