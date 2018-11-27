from urllib import request
from bs4 import BeautifulSoup as bs

#获取网站文本标签
resp=request.urlopen("http://www.136book.com/")
html_data= resp.read().decode('utf-8')

#解析html标签
soup=bs(html_data,'html.parser')

book=soup.find('div',id='digg_list')
book_ul=book.find('ul')
book_list=book_ul.find_all('li')

book_hot_show=[]
print("热门小说推荐：")
for item in book_list:
    dict={}
    dict['链接'] = item.find('a')['href']
    dict['书名']=item.find('img')['title']
    print(dict)
    book_hot_show.append(dict)

book=soup.find('div',id='newly_list')
book_ul=book.find('ul')
book_list=book_ul.find_all('li')

book_new_show=[]
print("最新小说推荐：")
for item in book_list:
    dict={}
    dict['链接'] = item.find('a')['href']
    dict['书名']=item.find('img')['title']
    print(dict)
    book_new_show.append(dict)