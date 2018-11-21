from tkinter import Tk,Canvas,Button

def upRevt():
    can.move(rect,0,-3)
def downRevt():
    can.move(rect,0,3)
def leftRevt():
    can.move(rect,-3,0)
def rightRevt():
    can.move(rect,3,0)

win=Tk()
win.geometry('400x360')

btn1=Button(win,text='向上',command=upRevt)
btn1.pack(side='top')
btn3=Button(win,text='向左',command=leftRevt)
btn3.pack(side='left')
btn4=Button(win,text='向右',command=rightRevt)
btn4.pack(side='right')

can=Canvas(win,width=250,height=300)    #画布对象
can.pack()
x=100
y=100
rect=can.create_rectangle(x,y,x+30,y+30,fill='red')

btn2=Button(win,text='向下',command=downRevt)
btn2.pack()

win.mainloop()