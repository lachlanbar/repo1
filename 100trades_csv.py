def trades_csv():
    import requests
    import csv
    exchange=input("input the name of the exchange you want information from (default is Bitbuy)-") or "bitbuy"
    exchange=exchange.lower()
    crypto=input("input the three letter symbol for your desired cryptocurrency (default is BTC)-") or "btc"
    crypto=crypto.lower()
    currency=input("input the three letter symbol for your desired currency (default is CAD)-") or "cad"
    currency=currency.lower()
    APIkey=input("input API key-")
    http="https://api.tokendatabase.com/v1/markets/trades?ids={0}_spot_{1}_{2}&limit=100&key={3}".format(exchange,crypto,currency,APIkey)
    filename=input("input requested name for CSV file (default is csv__hundred_trades)-") or "csv__hundred_trades"
    response=requests.get(http)
    rtrades=response.json()['results'][0]['trades']
    with open(filename,'w') as new_file:
        writer=csv.DictWriter(new_file,fieldnames=["id","id_on_exchange","time","price","quantity","side"])
        for i in rtrades:
            writer.writerow(i)   