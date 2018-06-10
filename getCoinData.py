import requests
from bs4 import BeautifulSoup

url ="https://coinmarketcap.com/currencies/"
url_extn="/#markets"

website_slug = ['hurify','mirq']

for i in website_slug:
    actualLink=url+i+url_extn
    coinData=requests.get(actualLink)
    soup= BeautifulSoup(coinData.content,'html.parser')
    x=soup.body
    y=x.find('div', {'class':'col-sm-4 col-sm-pull-8'})
    for i in y.findAll('li'):
        print(i.text,i.a)
