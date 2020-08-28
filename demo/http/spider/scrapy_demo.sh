#coding:utf-8

""""
爬虫框架
pip install scrapy
demo
#https://github.com/scrapy/quotesbot.git
"""

scrapy startprojec spider_demo         #创建项目
cd spider_demo
scrapy genspider myspider  baidu.com   #创建爬虫
vim spider_demo/spiders/myspider.py    #编辑爬虫文件


vim spider_demo/settings.py            #如修改robots.txt规则 ROBOTSTXT_OBEY = False



scrapy crawl myspider                  #运行爬虫
scrapy list                            #列出所有爬虫
#scrapy settings [options]             #获得配置信息


