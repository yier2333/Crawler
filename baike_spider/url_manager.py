# -*- coding: utf-8 -*-
#URL管理器

#==============================================================================
#                需要提供四个方法：
# 1.添加一个url
# 2.添加一组urls(可以循环利用上一个添加一个url函数)
# 3.判断new_urls中是否还有待爬取的url
# 4.从new_urls中提取一个待爬取的url,并且将此url添加到old_urls中
#==============================================================================
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



