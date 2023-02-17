from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

service = webdriver.chrome.service.Service('/usr/local/bin/chromedriver')
service.start()
driver = webdriver.Chrome(service.service_url)


products = []
prices = []
ratings = []

driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content,features="lxml")
#print(soup.findAll('div', attrs={'class':'_3pLy-c row'}))
for a in soup.findAll('div', attrs={'class':'_3pLy-c row'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'gUuXy-'})
    try:
        rating.find('span', attrs={'class':'_1lRcqv'})
        span=rating.find('span', attrs={'class':'_1lRcqv'})
        rating_value = span.find('div', attrs={'class':'_3LWZlK'})
        rating = rating_value.get_text()
    except:
        rating =  ""

    products.append(name.get_text())
    prices.append(price.get_text())
    ratings.append(rating)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding="utf-8")
