from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global a,b,c
def lahenda():
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))*(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Нет корней"
            graf=False
        otv.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return graf,D,t
def graafik():
    flag,D,t=lahenda()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,"b:o", x0, y0,"g-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"вершина параболы({x0},{y0})"
    else:
        text=f"график нет возможности построить"
    otv.configure(text=f"D={D}\n{t}\n{text}")
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        uvokno.config(text="Уменьшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        uvokno.config(text="Увеличить окно")
        t=0
def kit():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.3,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-9.5,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('square equation')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def o4ki():
    x1=np.arange(-9,-1,0.5)
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9,0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-1,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-6,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1,0.5)
    y7=(-0.5)*x7*x7+1.5
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Очки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def zont():
    x1=np.arange(-12,12,0.5)
    y1=(-1/18)*x1*x1+12
    x2=np.arange(-4,4,0.5)
    y2=(-1/8)*x2*x2+6
    x3=np.arange(-12,-4,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,12,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,-0.3,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.2,0.5)
    y6=1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('Зонтик')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("800x300")
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)
lk=Label(f1,text="Решение квадратного уравнения",font="Arial 20", fg="green",bg="lightblue")
lk.pack()
otv=Label(f1,text="Решение", height=4,width=60,bg="yellow")
otv.pack(side=BOTTOM)
a=Entry(f1,font="Arial 20", fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)
x2=Label(f1,text="x**2+",font="Alial 20", fg="green", padx=10)
x2.pack(side=LEFT)
b=Entry(f1,font="Arial 20", fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(f1,text="x+",font="Arial 20", fg="green")
x.pack(side=LEFT)
c=Entry(f1,font="Arial 20", fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
ghj=Label(f1,text="=0",font="Arial 20", fg="green")
ghj.pack(side=LEFT)
bnt=Button(f1,text="Решить",font="Arial 20",bg="green",command=lahenda)
bnt.pack(side=LEFT)
bui_g=Button(f1,text="График", font="Arial 20",bg="green",command=graafik)
bui_g.pack(side=LEFT)
uvokno=Button(f2,text="Увеличить окно", font="Arial 20",bg="green",command=veel)
uvokno.pack()
kit=Radiobutton(f2,text="Кит",font="Arial 20",bg="blue",command=kit)
kit.pack()
o4ki=Radiobutton(f2,text="очки",font="Arial 20",bg="blue",command=o4ki)
o4ki.pack()
zont=Radiobutton(f2,text="зонт",font="Arial 20",bg="blue",command=zont)
zont.pack()
aken.mainloop()