import datetime
import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()

def currency_mapper(currency):
    return {
        "name": currency["name"],
        "price": currency["current_price"],
        "image":currency["image"]
    }

token = os.getenv("TOKEN")
res = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=1000&page=1&sparkline=false&locale=en").json()

cleaned = list(map(currency_mapper,res))

cleaned.sort(key=lambda x:x["price"],reverse=True)

for i,value in enumerate(cleaned):
    value["rank"] = i+1

date_now = datetime.datetime.now().strftime("%d/%m/%Y, %Hh%M")

with open("currency.js","w") as file:
    file.write(f"const data={str(cleaned)} \n const now = '{date_now}'")