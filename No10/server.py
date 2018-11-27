from socket import *

HOST='127.0.0.1'
PORT=14321
ADDERSS=(HOST,PORT)

sock=socket(AF_INET,SOCK_STREAM,0)
sock.bind(ADDERSS)  #绑定地址到Socket
sock.listen(10)
print("服务器开启")
print("服务器监听端口：",PORT)

connection, address = sock.accept()
print("ip地址：", address, "已连接")
while True: #循环轮询socket状态，等待访问
    #服务器接收客户端
    msg = connection.recv(1024).decode()
    if msg:
        # 服务器返回客户端
        if msg=='连接成功':
            str = msg
        else:
            str = '已收到' + msg
        connection.sendall(bytes(str, 'UTF-8'))
        print("客户端："+msg)
    else:
        break

print("客户端断开连接")
connection.close()
sock.close()

