import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.worldometers.info/coronavirus/country/bangladesh/')
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='news').get_text()
news_date = soup.find(class_='news_date').get_text()
news = soup.find(class_='news_li').get_text()
source = soup.find(class_='news_source_a').get('href')

print(title, ':', news_date, news, source)