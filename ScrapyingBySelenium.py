from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.daraz.com.bd/smartphones/?spm=a2a0e.home.cate_1.1.735212f7kSHAld")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div', attrs={'class':'c3KeDq'}):
    name=a.find('a')
    price=a.find('span', attrs={'class':'c13VH6'})
    #rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text) if price else "N/A"
    #ratings.append(rating.text) if ratings else "N/A"
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
