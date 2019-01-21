# -*- coding: utf-8 -*-
import scrapy
from JavSpider.items import JavspiderItem
import logging
import re
from JavSpider import settings

# logger = logging.getLogger(__name__)

class WumaSpider(scrapy.Spider):
    name = 'wuma'
    allowed_domains = ['xwb2uooia5o59avwxb.com/uncensored', 'xwb2uooia5o59avwxb.com']
    start_urls = ['https://www.xwb2uooia5o59avwxb.com/uncensored']
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    # cookie = {'4fJN_2132_lastact': '1546160245%09misc.php%09seccode', 'HstCla4127494': '1546171197997', 'existmag': 'all', 'PHPSESSID': '6ln21mg1n6nrhc3m5t9q9eqt04', 'HstPt4127494': '137', '__guid': '35400359.4113806376697964000.1545555738264.177', '4fJN_2132_seccode': '7942.ba32df629914d0e609', 'HstCfa4127494': '1545555756697', 'starinfo': 'glyphicon%20glyphicon-plus', '4fJN_2132_lastvisit': '1546156644', '4fJN_2132_sid': 'TRLVHQ', '__cfduid': 'd761cee020cec276f507132139addc7421545555734', 'HstPn4127494': '74', 'monitor_count': '136', '4fJN_2132_saltkey': 'HJJ2dBHW', 'HstCnv4127494': '3', 'HstCmu4127494': '1545555756697', 'HstCns4127494': '7'}
    cookie = settings.COOKIES
    count = 0

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, cookies=self.cookie)  # 这里带着cookie发出请求

    def parse(self, response):
        # print(response)
        # number = response.xpath("//*[@id='waterfall']//div/a/div[2]/span/date[1]/text()").extract()
        # title = response.xpath("//*[@id='waterfall']//div/a/div[1]/img/@title").extract()
        li_list = response.xpath("//*[@id='waterfall']/div")
        # print(li_list)
        for li in li_list:
            item = JavspiderItem()
            item["number"] = li.xpath(".//a/div[2]/span/date[1]/text()").extract_first()
            item["title"] = li.xpath(".//a/div[1]/img/@title").extract_first()
            item["pdate"] = li.xpath(".//a/div[2]/span/date[2]/text()").extract_first()
            item["detail_link"] = li.xpath(".//a/@href").extract_first()
            # print(item)

            yield scrapy.Request(
                item["detail_link"],
                callback=self.parse_detail1,
                meta={'a': item}
            )
        #找到下一页的url地址
        next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        # print(next_url)
        if next_url is not None:
            next_url = 'https://www.xwb2uooia5o59avwxb.com' + next_url
            print(next_url)
            yield scrapy.Request(next_url,
                                 callback=self.parse,
                                 )


    def parse_detail1(self, response):
        item = response.meta['a']

        pic_link = response.xpath("/html/body/div[5]/div[1]/div[1]/a/img/@src").extract_first()
        item['cover'] = ''
        if not pic_link:
            item['cover'] = '暂时没有图片'
        else:
            item['cover'] = pic_link

        fenlei = response.xpath(
            "/html/body/div[5]/div[1]/div[2]/p[@class='star-show']/preceding-sibling::p/span[@class='genre']/a/text()").extract()
        # print(fenlei)
        item['fenlei'] = ''
        if not fenlei:
            item['fenlei'] = '暂时没有分类信息'
        else:
            for t in fenlei:
                item['fenlei'] = item['fenlei'] + t + ','

        actor = response.xpath(
            "/html/body/div[5]/div[1]/div[2]/p[@class='star-show']/following-sibling::p/span[@class='genre']/a/text()").extract()
        # print(actor)
        item['actor'] = ''
        if not actor:
            item['actor'] = '暂时没有演员信息'
        else:
            for t in actor:
                item['actor'] = item['actor'] + t + ','
        # print(response.body)
        movie_id = re.search(r'\d{11}|\d{10}', response.body.decode('utf-8', 'ignore')).group()
        # print(movie_id)
        yield scrapy.Request(
            'https://www.xwb2uooia5o59avwxb.com/ajax/uncledatoolsbyajax.php?gid=%s&lang=zh&uc=1' % movie_id,
            callback=self.parse_detail2,
            meta={'b': item}
        )

    def parse_detail2(self, response):
        item = response.meta['b']

        maglist = response.xpath('//td//a[@title="滑鼠右鍵點擊並選擇【複製連結網址】"]/@href').extract()
        # print(len(maglist))
        maglinks = []
        item['maglinks'] = ''
        for n in range(1, len(maglist), 3):
            maglinks.append(maglist[n - 1])
        if not maglinks:
            item['maglinks'] = '暂时没有磁力链接'
        else:
            for t in maglinks:
                item['maglinks'] = item['maglinks'] + t + ','
        yield item

