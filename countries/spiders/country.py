# -*- coding: utf-8 -*-
import scrapy


class CountrySpider(scrapy.Spider):
    name = 'country'
    # allowed_domains = ['https://scrapethissite.com/pages/simple/']
    start_urls = ['http://scrapethissite.com/pages/simple/']

    def parse(self, response):
        lenxp = '(//div[@id="page"]/section/div/div)'
        lngth = len(response.xpath(lenxp))
        counamexp = '(//div[@id="page"]/section/div/div)[{}]/div/h3/text()'
        capnamexp = '(//div[@id="page"]/section/div/div)[{}]/div/div/span[@class="country-capital"]/text()'
        popxp = '(//div[@id="page"]/section/div/div)[{}]/div/div/span[@class="country-population"]/text()'
        areaxp = '(//div[@id="page"]/section/div/div)[{}]/div/div/span[@class="country-area"]/text()'
        for i in range(lngth):
            counamexpath = counamexp.format(i+4)
            capnamexpath = capnamexp.format(i+4)
            popxpath = popxp.format(i+4)
            areaxpath = areaxp.format(i+4)
            couname = response.xpath(counamexpath).getall()
            capname = response.xpath(capnamexpath).getall()
            population = response.xpath(popxpath).getall()
            area = response.xpath(areaxpath).getall()
            d = []
            for i in couname:
                a = i.strip()
                if a == '':
                    continue
                d.append(a)
            for i in range(len(capname)):
                yield {"Capital":capname[i],"Country":(d[i]).strip(),"Population":population[i],"Area (km2)":area[i]}
