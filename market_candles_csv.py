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
    enddate=input("input the date of the stopping point for which the candles will be generated in the form yyyy-mm-dd (default is current date)-") or datetime.date.today().isoformat()
    endtime=input("input the time on the given date of the stopping point for which the candles will be generated in the form hh-mm (default is current time)-") or datetime.datetime.now().time().isoformat(timespec='minutes')
    starttime=input("input the date of the starting point for which the candles will be generated in the form yyyy-mm-dd (default is one day before ending date)-") or (datetime.datetime.strptime(enddate, '%Y-%m-%d')-datetime.timedelta(days=1)).isoformat()[:10]
    http="https://api.tokendatabase.com/v1/markets/ohlcv?ids={5}_spot_{0}_{1}&start={2}&end={6}T{3}&period=12hour&key={4}".format(crypto,currency,starttime,endtime,APIkey,exchange,enddate)
    print(http)
    filename=input("input requested name for CSV file (default is csv_market_candle)-") or "csv_market_candle"
    response=requests.get(http)
    rcandle=response.json()['results'][0]['candles']
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["time",'high', 'close', 'volume_quote', 'open', 'low', 'volume'])
        for i in rcandle:
            writer.writerow(i)    
            
