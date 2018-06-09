import requests
import json
import pandas as pd


url = "https://api.coinmarketcap.com/v2/listings"


def getListings(link):
    data=requests.get(link)

    if data.status_code != 200:
        print('GET/listing Error {}'.format(data.status_code))
    Text=json.loads(data.content)
    cols=['id','name','symbol']

    df=pd.DataFrame(Text['data'],columns = cols)
    print(df.head())
if __name__ =='__main__':
    getListings(url)
