import requests
import json
import time
import matplotlib.pyplot as plt 

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

USD = response["bpi"]["USD"]["rate"]
EUR = response["bpi"]["EUR"]["rate"]
GBP = response["bpi"]["GBP"]["rate"]


print("USD: $" + USD)
print("EUR: €" + EUR)
print("GBP: £" + GBP)

oldUSD = USD
oldUSD = oldUSD.replace(",", "")
#print("$" + USD)
while True:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    
    USD = response["bpi"]["USD"]["rate"]
    USD = USD.replace(",", "")
    print("Price Collected: $" + USD)
    if float(USD) > float(oldUSD):
        print("$" + USD + "| ↑ "+ str(round((float(USD)/float(oldUSD)-1), 4)) + "%")
    elif float(USD) < float(oldUSD):
        print("$" + USD + "| ↓ "+ str(round((float(USD)/float(oldUSD)-1), 4)) + "%")
    time.sleep(60)
    oldUSD = USD