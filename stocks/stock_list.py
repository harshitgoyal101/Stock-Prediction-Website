import os

import fileinput
import requests

def download_file(url, filename):
    ''' Downloads file from the url and save it as filename '''
    # check if file already exists
    if not os.path.isfile(filename):
        print('Downloading File')
    else:
        os.remove(filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response:
                file.write(chunk)


def run1():
    stocks1 = ["BSESN","INFY","NSEI","RELIANCE","SBI","TATASTEEL","TCS","TTM"]
    stocks = ["^BSESN","INFY_NS","AAPL","RELIANCE_NS","SBIN_NS","TATASTEEL_NS","TCS_NS","TTM"]

    for i in range(len(stocks)):
        url_name = stocks[i]
        url_name = url_name.replace("_",".")
        url = "https://query1.finance.yahoo.com/v7/finance/download/"+url_name+"?period1=1584866143&period2=1616402143&interval=1d&events=history&includeAdjustedClose=true"
        filename = "stock_list/"+stocks1[i]+".csv"
        download_file(url,filename)
        print("download_file"+stocks[i])
