from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


driver=webdriver.Chrome(chrome_options=chrome_options) 
driver.implicitly_wait(2)             
driver.get("http://piyao.sina.cn/")
time.sleep(2)


for i in range(200):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

date=driver.find_elements_by_xpath('//div[@class="zy_day"]')#日期

times=[]
titles=[]
likes=[]
comments=[]

for k in range(90):
        time=date[k].find_element_by_xpath('div[@class="day_date"]')
        title=date[k].find_elements_by_xpath('div[@class="day_date"]/following-sibling::ul//div[@class="left_title"]')
        like=date[k].find_elements_by_xpath('div[@class="day_date"]/following-sibling::ul//div[@class="like_text"]')
        comment=date[k].find_elements_by_xpath('div[@class="day_date"]/following-sibling::ul//div[@class="comment_text"]')
        for j in range(len(title)):
                times.append(time.text)
                titles.append(title[j].text)
                likes.append(like[j].text)
                comments.append(comment[j].text)

likes=[int(i) for i in likes]
comments=[int(i) for i in comments]


high_likes_news=sorted(zip(times,titles,likes,comments), key=lambda x : x[2],reverse=True)
high_comments_news=sorted(zip(times,titles,likes,comments), key=lambda x : x[3],reverse=True)

print("新浪辟谣网三个月内点赞数前十谣言： ")
for x in high_likes_news[:10]:
        print(x[0],'\t','点赞数: ',x[2],'\t',x[1])

print("新浪辟谣网三个月内评论数前十谣言： ")
for x in high_comments_news[:10]:
        print(x[0],'\t','评论数: ',x[3],'\t',x[1])


