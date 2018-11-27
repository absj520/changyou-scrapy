import scrapy
from scrapy import Request
from changyou.items import ChangyouItem
from changyou.settings import DEFAULT_REQUEST_HEADERS
class ChangyouSpider(scrapy.Spider):
    name = 'changyou'
    allowed_domains = ['changyou.com']
    start_urls = [
        'http://tl.cyg.changyou.com/'
    ]
    def parse(self,response):
        for i in range(0,14):
            #这里修改爬取的网址
            purl = response.url + 'goods/public?world_id=0&equipscore=400001-900000&have_chosen=equipscore*400001-900000&page_num='+str(i+1)
            yield scrapy.Request(url=purl,callback=self.links)

    def links(self, response):
        #抓取商品列表的链接
        body = response.body.decode("utf-8","ignore")
        link = response.xpath('//dl[@class="item-info"]/dt[@class="title"]/a/@href').extract()
        for a in range(len(link)):
            url = link[a]
            yield scrapy.Request(url=url,callback=self.datas)


    def datas(self, response):
        item = ChangyouItem()
        menpail = response.xpath('//span[@class= "fn-other-menpai"]/text()').extract()[0]
        menpai = menpail.split(':')[-1]
        namel = response.xpath('//ul/li/p[@class="J-message"]/text()').extract()
        name = namel[0]
        pricel = response.xpath('//ul/li/p/span[@class="ui-money-color ui-money-size"]/text()').extract()[0]
        price = pricel.strip('￥')
        servers = response.xpath('//ul/li/p[@class="server-info J-message"]/text()').extract()[0]
        goodsidl = response.xpath('//ul[@class="info-list"]/li/p/text()').extract()
        goodsid = goodsidl[0].split('：')[1]
        attackl= response.xpath('//div[@class="model"]/div[@class="c-o-l"]/p/text()').extract()
        attackb = attackl[0]
        attackbk = attackl[1]
        attackbj = attackl[2]
        attackbx = attackl[3]
        attackh = attackl[4]
        attackhk = attackl[5]
        attackhj = attackl[6]
        attackhx = attackl[7]
        attackx = attackl[8]
        attackxk = attackl[9]
        attackxj = attackl[10]
        attackxx = attackl[11]
        attackd = attackl[12]
        attackdk = attackl[13]
        attackdj = attackl[14]
        attackdx = attackl[15]
        bloodl = response.xpath('//span[@class="span"]/i[@class="fn-high-light"]/text()').extract()
        blood = bloodl[0]
        gsl = response.xpath('//div[@class="row2"]/span[@class="span"]/text()').extract()
        gs = gsl[11].split(':')[0]

        item['menpai'] = menpai
        item['name'] = name
        item['price'] = price
        item['servers'] = servers
        item["goodsid"] = goodsid
        item['attackb'] = attackb
        item['attackbk'] = attackbk
        item['attackbj'] = attackbj
        item['attackbx'] = attackbx
        item['attackh'] = attackh
        item['attackhk'] = attackhk
        item['attackhj'] = attackhj
        item['attackhx'] = attackhx
        item['attackx'] = attackx
        item['attackxk'] = attackxk
        item['attackxj'] = attackxj
        item['attackxx'] = attackxx
        item['attackd'] = attackd
        item['attackdk'] = attackdk
        item['attackdj'] = attackdj
        item['attackdx'] = attackdx
        item['blood'] = blood
        item['gs'] = gs
        return item
