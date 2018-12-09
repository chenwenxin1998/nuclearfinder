from bs4 import BeautifulSoup
from urllib.request import urlopen
import re,time

#水处理公司元素周期表爬虫


class DATA:             #通过原子序列更新数据,   DATA.data为更新过后的数据

    def __init__(self,number):
        self.number = number
        self.data = None     #用来存放此条目信息
        self.getdata()

    # 得到url
    def GetUrls(self):
        urls = []  # 用于存储元素表超链接
        html = urlopen("https://www.lenntech.com/periodic/periodic-chart.htm")  # 获取HTML
        bsObj = BeautifulSoup(html, "lxml")                                          # 获取HTML的BeautifulSoup
        for link in bsObj.findAll("a",
                                  href=re.compile("https://www.lenntech.com/periodic/elements/.*\.htm")):  # 获取元素表的超链接
            if 'href' in link.attrs:
                urls.append(link.attrs['href'])
        self.urls=urls

    # 得到元素数据
    def getproperties(self):
        # 元素性质类别

        # 遍历每个元素
        for url in self.urls:
            d = {'Atomic name': None, 'Atomic number': None, 'Atomic mass': None,
                 'Electronegativity according to Pauling': None,
                 'Density': None, 'Melting point': None, 'Boiling point': None, 'Vanderwaals radius ': None,
                 'Ionic radius': None,
                 'Isotopes': None, 'Electronic shell ': None, 'Energy of first ionisation': None, 'Discovered by': None,
                 }
            time.sleep(1)  # 道德要求。。
            html = urlopen(url)
            bsObj = BeautifulSoup(html, "lxml")  # 页面解析

            for i in bsObj.findAll("div", {"class": "col-md-9"}):  # 找到元素名称
                if i.h1:
                    d['Atomic name'] = i.h1.contents[0].string
            try:
                a = bsObj.findAll("table")[0].findAll("tr")[0]
            except IndexError:
                continue
            except AttributeError:
                continue

            for i in a.findAll('tr'):  # 找到各个性质
                try:
                    b0 = i.findAll("td")[0].p.contents[0].string
                    s=''
                    for m in i.findAll("td")[1].p.contents:
                        s=s+m.string
                    b1=s
                except IndexError:
                    continue
                except AttributeError:
                    continue
                else:
                    if b0 in d:  # 放入字典
                        d[b0] = b1
            if str(self.number)==d['Atomic number']:
                self.data=d
                return 0

    def getdata(self):
        print(self.number)
        self.GetUrls()
        self.getproperties()

# def main():
#     s = DATA(5)
#     print(s.data)
#     # s = DATA(5)
#     # s.getdata()
# main()
#
