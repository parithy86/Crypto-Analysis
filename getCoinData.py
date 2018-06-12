import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://coinmarketcap.com/currencies/"
url_extn="/#markets"



def getCoinDtls(data,coinName):
    soup= BeautifulSoup(data.content,'html.parser')
    pageBody=soup.body
    dataFields=pageBody.find('div', {'class':'col-sm-4 col-sm-pull-8'})
    cols=['website_slug','data','links']
    coinDtlsArry = []


    for i in dataFields.find_all('li'):
        for x in i.find_all('a'):
            coinDataFields=[coinName,i.text,x.get('href')]
            coinDtlsArry.append(coinDataFields)

    df=pd.DataFrame(coinDtlsArry,columns = cols)
    print(df.tail())

if __name__ =='__main__':
    website_slug = ['hurify','mirq']

    for coinName in website_slug:
        actualLink=url+coinName+url_extn
        coinData=requests.get(actualLink)
        getCoinDtls(coinData,coinName)
