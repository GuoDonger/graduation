import requests
import pymysql
import time
from lxml import etree
from bs4 import BeautifulSoup
from celery import shared_task
from data.content import HOST, PORT, USER, PASSWORD, CHARSET, DATABASE, HEADERS


base_url = 'http://www.pm25.in'
sql_select = 'select * from data_city;'
sql_truncate = 'truncate table data_data;'


@shared_task
def get_data():
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
            AQI = tree.xpath('//div[@class="span1"]/div[@class="value"]/text()')[0]
            AQI = int(AQI.strip())
        except Exception as error:
            print(error)
            continue
        sql = "insert into data_data(city_id,time,data,AQI) values(%s,%s,%s,%s);"
        cursor.execute(sql, [city[0], day_time, data, AQI])
        connect.commit()
        print('success')
    connect.close()

