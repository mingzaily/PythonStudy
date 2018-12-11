from urllib import request
from bs4 import BeautifulSoup as bs

# 获取网站文本标签
resp=request.urlopen("http://www.yc.ifeng.com/?cid=91002/")
html_data= resp.read().decode('utf-8')

# 解析html标签
soup = bs(html_data, 'html.parser')

book = soup.find('div', id='book_list')
book_table = book.find('table')
book_tbody = book_table.find('tbody')
book_list = book_tbody.find_all('tr')

book_hot_show=[]
print("书库：")
for item in book_list:
    dict={}
    dict['类型'] = item.find('td',class_='col-type').find('a')['title']
    dict['书名'] = item.find('td',class_='col-name').find('a')['title']
    print(dict)
    book_hot_show.append(dict)
