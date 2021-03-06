import requests
import pymysql
import time
from lxml import etree
from bs4 import BeautifulSoup

HOST = '123.56.23.97'
PORT = 3306
USER = 'root'
PASSWORD = '111111'
CHARSET = 'utf8'
DATABASE = 'wumai'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
}

base_url = 'http://www.pm25.in'
sql_select = 'select * from data_city;'
sql_truncate = 'truncate table data_data;'

while True:
    print('start')
    connect = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, charset=CHARSET)
    cursor = connect.cursor()
    cursor.execute(sql_select, [])
    cities = cursor.fetchall()
    cursor.execute(sql_truncate, [])
    for city in cities:
        try:
            url = base_url + str(city[3])
            response = requests.get(url=url, headers=HEADERS)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            tree = etree.HTML(html)
            day_time = tree.xpath('//div[@class="live_data_time"]/p/text()')[0][7:]
            day_time = time.mktime(time.strptime(day_time, "%Y-%m-%d %H:%M:%S"))
            day_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(day_time))
            data = str(soup.select('div .table > table')[0])
            AQI = tree.xpath('//div[@class="value"]/text()')[0]
            AQI = int(AQI.strip())
            rank = tree.xpath('//div[@class="level"]/h4/text()')[0]
            rank = rank.strip()
            PM25 = tree.xpath('//div[@class="value"]/text()')[1]
            PM25 = int(PM25.strip())
        except Exception as error:
            print(error)
            continue
        sql = "insert into data_data(city_id,time,data,AQI,rank,PM25) values(%s,%s,%s,%s,%s,%s);"
        cursor.execute(sql, [city[0], day_time, data, AQI, rank, PM25])
        connect.commit()
        print('success')
    connect.close()
    print('end')
    time.sleep(7200)
