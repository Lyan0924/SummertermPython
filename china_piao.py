# 引入需要使用到的库
# requests是一个提交http请求的常用的库。
import requests
# lxml是一个解析html和xml文件格式的库
from lxml import etree
# 设置requests的header，这样发送的和请求正常的浏览器一样，很多服务器会验证header
requests.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 
                         'Chrome/51.0.2704.63 Safari/537.36'}
# 这里向URL发送get请求，并获得返回的response
response = requests.get('http://www.chinapiao.com.cn/query.php')
# response有state（200、404等）、header、content等字段，其中content字段是返回的内容，通常是html格式的。
html = etree.HTML(response.content)
# 使用chrome的F12观察了返回的html的结构，复制了感兴趣的数据的xpath并根据特点自行修改
names = html.xpath('//tr/td[1]/a/text()') # 演出的名字
time = html.xpath('//tr/td[2]/text()')  # 演出时间
address = html.xpath('//tr/td[3]/text()')   # 演出地点
price_str = html.xpath('//tr/td[4]/text()') # 演出的价格
# 下面几行是按照价格最高和最低进行排序
price_high = []
price_low = []
for i in price_str:
    prices = i.split("、") # 一个演出通常会有多种票价，页面上用"、"分割，这里拆开
    prices = [int(i) for i in prices]
    # 然后取出每个演出的票价中的最高级和最低价
    price_high.append(max(prices))
    price_low.append(min(prices))
# 把数据组合成元组的列表
name_and_prices = zip(names, time, address, price_high, price_low)
name_and_prices = [i for i in name_and_prices if i[2] != '礼品卡' and i[1] != '全年' and i[1] != '常年']
# 按每个演出最高价排序
high_price = sorted(name_and_prices, key=lambda x : x[3])
# 按每个演出的最低价排序
low_price = sorted(name_and_prices, key=lambda x : x[4])
# 打印结果
print("中国演出票务网，在售最便宜前10：")
for x in low_price[:10]:
    print('价格:', x[4], '\t', x[2],'\t',x[1],'\t',x[0])
print("中国演出票务网，在售最贵前10：")
for x in high_price[-10:]:
    print('价格:', x[3], '\t', x[2],'\t',x[1],'\t', x[0])