def candle_csv():
    import requests
    import csv
    exchange=input("input the name of the exchange you want information from (default is Bitbuy)-") or "bitbuy"##change defaults?
    exchange=exchange.lower()
    crypto=input("input the three letter symbol for your desired cryptocurrency (default is BTC)-") or "btc"
    crypto=crypto.lower()
    currency=input("input the three letter symbol for your desired currency (default is CAD)-") or "cad"
    currency=currency.lower()
    APIkey=input("input API key-")
    http="https://api.tokendatabase.com/v1/markets/trades?ids={}_spot_{}_{}&limit=100&key={}".format(market,crypto,currency,APIkey)
    filename=input("input requested name for CSV file (default is csv_candle)-") or "csv_candle"##change default
    response=requests.get(http)
    rtrades=response.json()['results'][0]['candles']##change
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["time",'high', 'close', 'volume_quote', 'open', 'low', 'volume'])
        for i in rcandle:
            writer.writerow(i)   