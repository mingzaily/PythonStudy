from tkinter import Tk,Canvas

win=Tk()
win.geometry('250x300')

can=Canvas(win,width=250,height=300)    #画布对象
can.pack()

data1=(50,50,150,150)
data2=(45,45,145,145)
rect1=can.create_rectangle(data1,fill='black')  #黑色阴影
rect2=can.create_rectangle(data2,fill='red') #红色矩形

win.mainloop()