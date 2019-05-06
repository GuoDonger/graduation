from urllib import request
from lxml import etree
import pymysql

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
connect = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, charset=CHARSET)
cursor = connect.cursor()

url = 'http://www.pm25.in/'
response = request.Request(url=url, headers=HEADERS)
result = request.urlopen(response).read().decode('utf-8')
tree = etree.HTML(result)
uls = tree.xpath('//div[@class="all"]//div[@class="bottom"]/ul')

for ul in uls:
    initial = ul.xpath('.//b/text()')[0]
    city = ul.xpath('.//li/a/text()')
    word = ul.xpath('.//li/a/@href')
    cities = list(zip(city, word))
    for city in cities:
        sql = 'insert into data_city(initial,city,word) values(%s,%s,%s);'
        result = cursor.execute(sql, [initial, city[0], city[1]])
        connect.commit()
        print('success')
