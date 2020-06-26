import datetime
from datetime import date
def indices_candle_csv():
    import requests
    import csv
    import datetime
    exchange=input("input the name of the exchange you want information from (default is Bitbuy)-") or "bitbuy"
    exchange=exchange.lower()
    crypto=input("input the three letter symbol for your desired cryptocurrency (default is BTC)-") or "btc"
    crypto=crypto.lower()
    APIkey=input("input API key-")
    endtime=datetime.datetime.now().isoformat(timespec='seconds')
    starttime=(datetime.date.today()-datetime.timedelta(days=1)).isoformat()
    http="https://api.tokendatabase.com/v1/indices/vwap5/ohlcv?ids={1}&end=2020-01-14T12:00:00.000&start=2020-01-10T12:00:00.000&period=12hour&key={}".format(crypto,currency,starttime,endtime,APIkey,exchange)
    filename=input("input requested name for CSV file (default is csv_candle)-") or "csv_candle"
    response=requests.get(http)
    rcandle=response.json()['results'][0]['candles']
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["time",'high', 'close', 'volume_quote', 'open', 'low', 'volume'])
        for i in rcandle:
            writer.writerow(i)    