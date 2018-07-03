# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:35:26 2018

@author: Mr.Lu
"""

import urllib
import re
def get_url_list(url):#得到url列表
    #url1 = 'http://www.quanshuwang.com/book/9/9055/'
    #headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'} 
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}    
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req)
    html = html.read()
    html = html.decode("gbk").encode("utf-8")
    html = str(html,encoding = "utf-8",errors = "ignore")#字符串转化，设置编码，转码中遇到错误的字符忽略
    #print (html)
    reg = r'<a href="(.*?)" class="reader" title="(.*?)">开始阅读</a>'
    reg = re.compile(reg)
    list1 = re.findall(reg,html)
    for i,j in list1:
        html1 = urllib.request.urlopen(i)
        html1 = html1.read()
        html1 = html1.decode("gbk").encode("utf-8")
        html1 = str(html1,encoding = "utf-8",errors = "ignore")
        reg1 = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
        reg1 = re.compile(reg1)
        urllist = re.findall(reg1,html1)#正则匹配
        return urllist 
def data_mining(url1):
    #headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    req = urllib.request.Request(url1, headers=headers)
    html2 = urllib.request.urlopen(req)
    html2 = html2.read()
    html2 = html2.decode("gbk").encode("utf-8")
    html2 = str(html2,encoding = "utf-8",errors = "ignore")
    space = '&nbsp;'
    space1 = '<br />'
    html2 = html2.replace(space,'')
    html2 = html2.replace(space1,'')
    start = '<div class="mainContenr"   id="content"><script type="text/javascript">style5();</script>'
    end = '<script type="text/javascript">style6();</script></div>'
    start_addre = html2.find(start)+len(start)
    #print (start_addre)
    end_addre = html2.find(end)
    #print (end_addre)
    html2 = html2[start_addre:end_addre]
    #print(html2)
    return html2
def write_file(text):
    with open('盗墓笔记2.txt', 'a') as f:
        f.write(text)
        f.write('\n\n')        
if __name__ == '__main__':
    url = "http://www.quanshuwang.com/book_9055.html"
    urllist = []
    urllist = get_url_list(url)
    for i,j in urllist:
        print (j)
        text = data_mining(i)
        write_file(j)        
        write_file(text)
    #url1 = 'http://www.quanshuwang.com/book/9/9055/9674264.html'
    #data_mining(url1)
    
    #print (urllist)
    