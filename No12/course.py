from urllib import request
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import pymysql.cursors


def main():
    win = Tk()
    win.title("抓包程序")  # 添加标题
    
    # 创建一个容器 接受客户信息
    monty = LabelFrame(win, text=" 抓包信息 ")  # 创建LabelFrame容器，其父容器为win
    monty.grid(column=0, row=0, padx=15, pady=15)  # padx,pady为该容器外围需要留出的空余空间
    # 滚动文本框
    scrolW = 80  # 设置文本框的长度
    scrolH = 15  # 设置文本框的高度
    txt_recv = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, font='16')
    txt_recv.grid(column=0, columnspan=3)  # columnspan将3列合并成一列
    # 按钮
    action = Button(monty, text="抓包", command=get_book)
    actions = Button(monty, text="读取数据库", command=lambda: read_mysql(txt_recv))
    action.grid(column=2, row=1)  # 设置其在界面中出现的位置
    actions.grid(column=1, row=1)  # 设置其在界面中出现的位置
    
    win.mainloop()


def get_book():
    cursor = connect.cursor()
    # 获取网站文本标签
    resp = request.urlopen("http://www.yc.ifeng.com/store/")
    html_data = resp.read().decode('utf-8')

    # 解析html标签
    soup=bs(html_data, 'html.parser')

    book = soup.find('div', id='book_list')
    book_table = book.find('table')
    book_tbody = book_table.find('tbody')
    book_list = book_tbody.find_all('tr')

    del_sql="truncate TABLE book"
    cursor.execute(del_sql)

    for item in book_list:
        book_type = item.find('td',class_='col-type').find('a')['title']
        book_name = item.find('td',class_='col-name').find('a')['title']
        book_url = "http://www.yc.ifeng.com"+item.find('td',class_='col-name').find('a')['href']
        sql="INSERT INTO book VALUE(NULL,'%s','%s','%s')"
        data=(book_type, book_name, book_url)
        cursor.execute(sql % data)
        connect.commit()

    messagebox.showinfo("提示", "抓包成功")
    cursor.close()


def read_mysql(txt_recv):
    cursor = connect.cursor()
    txt_recv.delete(1.0, 'end')
    sql = "SELECT * from book"
    cursor.execute(sql)
    connect.commit()
    for row in cursor.fetchall():
        msg = "书名：%s\t\t链接：%s" % (row[2], row[3])
        txt_recv.insert('end', msg + '\n')

    messagebox.showinfo("提示", "共查找 %s 条数据" % cursor.rowcount)
    cursor.close()


if __name__ == '__main__':
    connect = pymysql.Connect(
        host='139.199.74.74',
        port=3306,
        user='python',
        passwd='123456',
        db='python',
        charset='utf8'
    )
    
    main()
    
    connect.close()
