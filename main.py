import requests
from bs4 import BeautifulSoup


def getPrice(x):
    sym=str(x)
    url = 'https://www.marketwatch.com/investing/stock/'+str(sym)
    page = requests.get(url)
    
    
    try:
        rstr=""
        soup = BeautifulSoup(page.text, 'html.parser')
    
        company = soup.find('h1', {'class':'company__name'}).text
        price = soup.find('h2',{'class':'intraday__price'})
        #used to find the price from within the h2
        s=BeautifulSoup(price.text,'html.parser')
        s.find('bg-quote')
        price=s
        rstr+=("company Name: " +company)
        #Get rid of the dollar sign and the extra lines by replacing and spliting
        price=str(price).replace("$","").splitlines()[2]
        rstr+=("\nPrice: " +price)
        return rstr
    except:
        return("Could not find that symbol")




print(getPrice("aapl"))
