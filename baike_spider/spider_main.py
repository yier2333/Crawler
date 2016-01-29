# -*- coding: utf-8 -*-
#总的调度器
#==============================================================================
# 提供对各个模块的调度————craw（）函数
#==============================================================================
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain():
    def __init__(self):

        self.urls = url_manager.UrlManager() #初始化url管理器对象
        self.downloader = html_downloader.HtmlDownloader() #初始化url下载器对象
        self.parser = html_parser.HtmlParser()  #初始化html解析器对象
        self.outputer = html_outputer.HtmlOutputer() #初始化html输出对象

    def craw(self, root_url):

        count = 1 #记录爬取的url数目

        self.urls.add_new_url(root_url) #将源url添加到url管理器中

        while self.urls.has_new_url(): #若url管理器中有待爬取的url，则进行循环爬取
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d :%s' %(count, new_url)
                html_cont = self.downloader.download(new_url) #将url送到下载器中，返回html_cont
                new_urls,new_data = self.parser.parse(new_url, html_cont) #将html_cont送到解析器中进行解析，返回新的urls和data
                self.urls.add_new_urls(new_urls) #将新的urls添加到url管理器中
                self.outputer.collect_data(new_data) #将新的数据添加到输出器中
                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.output_html()

if __name__=="__main__":
    root_url = 'http://baike.baidu.com/view/21087.htm'
    spider = SpiderMain()
    spider.craw(root_url)


#