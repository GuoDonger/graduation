import requests
import pymysql
import time
from lxml import etree
from data.content import HOST, PORT, USER, PASSWORD, CHARSET, DATABASE, HEADERS

clear = lambda x: x.replace('\t', '').replace('\n', '').replace('\u3000', '')

base_url = 'http://www.pm25.com/news/'
connect = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, charset=CHARSET)
cursor = connect.cursor()

cate = ['政府政策', '行业报告', '各地新闻', '特殊人群防护', '疾病防护', 'PM2.5专题', 'PM2.5科普']

for category in cate:
    sql = 'insert into news_category(name) value(%s)'
    cursor.execute(sql, [category])
    connect.commit()

for num in range(60, 1035):# 1035
    try:
        url = base_url + str(num) + '.html'
        response = requests.get(url=url, headers=HEADERS)
        html = response.text
        tree = etree.HTML(html)
        category = tree.xpath('//ul[@class="crumb"]/li[3]/a/text()')[0]
        title = tree.xpath('//div[@class="ncl_title"]/h1/text()')[0]
        source = tree.xpath('//div[@class="nr_copyright"]/p[1]/text()')[0][3:]
        digest = tree.xpath('//div[@class="ncl_brief"]/text()')[0]
        image = tree.xpath('//div[4]/div/div/div[@class="news_content_right"]/p/img/@src')[0]
        image = 'http://www.pm25.com' + image
        add_time = tree.xpath('//div[@class="nr_copyright"]/p[3]/text()')[0][3:]
        add_time = time.mktime(time.strptime(add_time, "%Y-%m-%d  %H:%M:%S"))
        add_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(add_time))
        contents = tree.xpath('//div[@class="news_details"]/p/text()')
    except Exception as error:
        print(error)
        continue
    category_id = '0'
    if category == '政府政策':
        category_id = '1'
    elif category == '行业报告':
        category_id = '2'
    elif category == '各地新闻':
        category_id = '3'
    elif category == '特殊人群防护':
        category_id = '4'
    elif category == '疾病防护':
        category_id = '5'
    elif category == 'PM2.5专题':
        category_id = '6'
    elif category == 'PM2.5科普':
        category_id = '7'
    sql = "insert into news_news(category_id,title,source,add_time,image,digest) values(%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql, [category_id, title, source, add_time, image,digest])
    connect.commit()
    get_id = 'select id from news_news where title=%s;'
    cursor.execute(get_id, [title])
    news_id = cursor.fetchone()
    sql0 = 'insert into news_content(news_id,content) values(%s,%s);'
    for content in contents:
        cursor.execute(sql0, [news_id, content])
        connect.commit()
    print(num, 'success')
connect.close()
