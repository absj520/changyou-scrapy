# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from changyou import settings
from changyou.items import ChangyouItem

class ChangyouPipeline(object):
    def __init__(self):

        self.connect = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",database='changyou')
        self.cursor = self.connect.cursor()



    def process_item(self, item, spider):
#如果是非数字的数据，%s两边一定要加单引号
        insert_sql="""insert into gongshi(goodsid,blood,gs,menpai,name,price,servers,attackb,attackbk,attackbj,attackbx,attackh,attackhk,attackhj,attackhx,attackx,attackxk,attackxj,attackxx,attackd,attackdk,attackdj,attackdx)Value('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(
        item['goodsid'],item['blood'],item['gs'],item['menpai'],item['name'],item['price'],item['servers'],item['attackb'],item['attackbk'],item['attackbj'],item['attackbx'],item['attackh'],item['attackhk'],item['attackhj'],item['attackhx'],item['attackx'],item['attackxk'],item['attackxj'],item['attackxx'],item['attackd'],item['attackdk'],item['attackdj'],item['attackdx'])
        self.cursor.execute(insert_sql)
        self.connect.commit()
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
