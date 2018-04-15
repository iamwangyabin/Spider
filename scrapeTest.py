from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import re

def scrape():
    # 需要爬取页面
    url = 'http://www.595ff.com/tttppp/'
    num = 864740

    # 浏览器头信息
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

    for i in range(10):
        urlForScrape = url + str(num) + '.html'
        request = urllib.request.Request(url = urlForScrape,headers = headers)
        response = urllib.request.urlopen(request)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        imgs=soup.find_all(re.compile("img"))
        root = '/home/wang/PycharmProjects/Spider/pic/'+str(num)+'/'


        for img in imgs:
            src = img['src']
            path = root + src.split('/')[-1]
            try:  # 创建或判断路径图片是否存在并下载
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(src)
                    with open(path, 'wb') as f:
                        f.write(r.content)
                        f.close()
                        print("文件保存成功")
                else:
                    print("文件已存在")
            except:
                print("爬取失败")

        num=num-1



#用来从网页里解析出图片地址
def parseImageUrl(html):
    soup = BeautifulSoup(html, 'html.parser')
    pass
#下载图片并且保存
def downloadImage(imgUrl):
    pass