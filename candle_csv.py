import datetime
from datetime import date
def market_candle_csv():
    import requests
    import csv
    import datetime
    exchange=input("input the name of the exchange you want information from (default is Bitbuy)-") or "bitbuy"
    exchange=exchange.lower()
    crypto=input("input the three letter symbol for your desired cryptocurrency (default is BTC)-") or "btc"
    crypto=crypto.lower()
    currency=input("input the three letter symbol for your desired currency (default is CAD)-") or "cad"
    currency=currency.lower()
    APIkey=input("input API key-")
    endtime=datetime.datetime.now().isoformat(timespec='seconds')
    starttime=(datetime.date.today()-datetime.timedelta(days=1)).isoformat()
    http="https://api.tokendatabase.com/v1/markets/ohlcv?ids={5}_spot_{0}_{1}&start={2}&end={3}&period=12hour&key={4}".format(crypto,currency,starttime,endtime,APIkey,exchange)
    filename=input("input requested name for CSV file (default is csv_candle)-") or "csv_candle"
    response=requests.get(http)
    rcandle=response.json()['results'][0]['candles']
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["time",'high', 'close', 'volume_quote', 'open', 'low', 'volume'])
        for i in rcandle:
            writer.writerow(i)    
            
