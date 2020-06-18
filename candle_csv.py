import datetime
from datetime import date
def candle_csv():
    import requests
    import csv
    import datetime
    crypto=input("input the three letter symbol for your desired cryptocurrency-")
    currency=input("input the three letter symbol for your desired currency-")
    APIkey=input("input API key-")
    filename=input("input requested name for CSV file-")
    endtime=datetime.datetime.now().isoformat(timespec='seconds')
    starttime=(datetime.date.today()-datetime.timedelta(days=1)).isoformat()
    http="https://api.tokendatabase.com/v1/markets/ohlcv?ids=bitbuy_spot_{0}_{1}&start={2}&end={3}&period=12hour&key={4}".format(crypto,currency,starttime,endtime,APIkey)
    response=requests.get(http)
    rcandle=response.json()['results'][0]['candles']
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["time",'high', 'close', 'volume_quote', 'open', 'low', 'volume'])
        for i in rcandle:
            writer.writerow(i)    
            
##add default values
##change file name (alphanumeric values only)
##print default value
##ake exchange variable (default bitbuy")
##autolowercase
   