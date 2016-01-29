# -*- coding: utf-8 -*-
#下载器
#==============================================================================
# 只提供一个方法download()
#==============================================================================
import urllib2
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if  response.getcode() != 200:
            return

        return response.read()


