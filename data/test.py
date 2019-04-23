import requests
import pymysql
import time
from lxml import etree
from bs4 import BeautifulSoup

base_url = 'http://www.pm25.in/api/querys/aqi_ranking.json?token=5j1znBVAsnSf5xQyNQyq'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
}

request = requests.get(url=base_url, headers=HEADERS)
html = request.text
print(html)



