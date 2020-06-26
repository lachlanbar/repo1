import datetime
from datetime import date
def indices_candle_csv():
    import requests
    import csv
    import datetime
    crypto=input("input the three letter symbol for your desired cryptocurrency (default is BTC)-") or "btc"
    crypto=crypto.lower()
    APIkey=input("input API key-")
    enddate=input("input the date of the stopping point for which the candles will be generated in the form yyyy-mm-dd (default is current date)-") or datetime.date.today().isoformat()
    endtime=input("input the time on the given date of the stopping point for which the candles will be generated in the form hh-mm (default is current time)-") or datetime.datetime.now().time().isoformat(timespec='minutes')
    startdate=input("input the date of the starting point for which the candles will be generated in the form yyyy-mm-dd (default is one day before ending date)-") or (datetime.datetime.strptime(enddate, '%Y-%m-%d')-datetime.timedelta(days=1)).isoformat()[:10]
    starttime=input("input the time on the given date of the stopping point for which the candles will be generated in the form hh-mm (default is ending time)-") or endtime
    http="https://api.tokendatabase.com/v1/indices/vwap5/ohlcv?ids={0}&end={5}T{2}&start={4}T{1}&period=12hour&key={3}".format(crypto,starttime,endtime,APIkey,startdate,enddate)
    print(http)
    filename=input("input requested name for CSV file (default is csv_indices_candle)-") or "csv_indices_candle"
    response=requests.get(http)
    rcandle=response.json()['results'][0]['candles']
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["time","open","high","low","close","volume","volume_quote"])
        for i in rcandle:
            writer.writerow(i)    