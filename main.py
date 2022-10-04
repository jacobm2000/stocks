import requests
from bs4 import BeautifulSoup

sym=input("enter a symbol name: ")
url = 'https://www.marketwatch.com/investing/stock/'+str(sym)
page = requests.get(url)


try:
    soup = BeautifulSoup(page.text, 'html.parser')

    company = soup.find('h1', {'class':'company__name'}).text
    price = soup.find('h2',{'class':'intraday__price'})
    #used to find the price from within the h2
    s=BeautifulSoup(price.text,'html.parser')
    s.find('bg-quote')
    price=s
    print("company Name: " +company)
    #Get rid of the dollar sign and the extra lines by replacing and spliting
    price=str(price).replace("$","").splitlines()[2]
    print("price: " +price)
except:
    print("Could not find that symbol")

