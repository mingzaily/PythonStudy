from tkinter import *
from socket import *
from tkinter import scrolledtext

# 定义向服务器发起连接函数
def conn():
    HOST = '127.0.0.1'
    PORT = 14321
    ADDRESS = (HOST, PORT)
    cs.connect(ADDRESS)  # 向服务器发起连接请求
    str = "连接成功"
    cs.sendall(bytes(str, 'UTF-8'))
    data = cs.recv(1024).decode()
    msgcontent = '服务器信息: '
    txt_recv.insert('end', msgcontent + data + '\n')

# 关闭服务器连接
def closeconn():
    cs.close()
    txt_recv.insert('end', '断开服务器连接')

# 向服务器发送相关信息
def sendData():
    str = e.get()
    cs.sendall(bytes(str, 'UTF-8'))
    data = cs.recv(1024).decode()
    msgcontent = '服务器信息: '
    txt_recv.insert('end', msgcontent + data  + '\n')

win = Tk()
win.title("客户端程序")  # 添加标题
cs = socket(AF_INET, SOCK_STREAM, 0)

# 创建一个容器 接受客户信息
monty = LabelFrame(win, text=" 接收信息 ")  # 创建LabelFrame容器，其父容器为win
monty.grid(column=0, row=0, padx=15, pady=15)  # padx,pady为该容器外围需要留出的空余空间
# 滚动文本框
scrolW = 60  # 设置文本框的长度
scrolH = 5  # 设置文本框的高度
txt_recv = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH)
txt_recv.grid(column=0, columnspan=3)  # columnspan将3列合并成一列
# 按钮
action = Button(monty, text="连接服务器", command=conn)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
actions = Button(monty, text="断开服务器", command=closeconn)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=2, row=1)  # 设置其在界面中出现的位置
actions.grid(column=1, row=1)  # 设置其在界面中出现的位置


# 创建一个容器
montys = LabelFrame(win, text=" 发送信息 ")  # 创建LabelFrame容器，其父容器为win
montys.grid(column=0, row=1, padx=15, pady=15)  # padx,pady为该容器外围需要留出的空余空间
# 滚动文本框
scrolW = 60  # 设置文本框的长度
scrolH = 5  # 设置文本框的高度
e = StringVar()
txt_send = Entry(montys,textvariable=e,width=scrolW)
txt_send.grid(column=0, columnspan=3)  # columnspan将3列合并成一列
# 按钮
actionss = Button(montys, text="发送信息", command=sendData)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
actionss.grid(column=2, row=1)  # 设置其在界面中出现的位置


win.mainloop()
