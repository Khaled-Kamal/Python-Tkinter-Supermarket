from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

pro = Tk()
pro.geometry('800x450+280+50')
pro.resizable(False,False)
pro.title('SuperMarket')
pro.iconbitmap('c:\\super.ico')

title=Label(pro,text='Super Market System',fg='orange',bg='white',font=('tajawal',17,'bold'))
title.pack(fill=X)

u1='https://www.facebook.com/username'
u2='url-telegram'
u3='url-youtube'

def superrr():
 pro.destroy()
 import Super

def open1():
    webbrowser.open_new(u1)
def open2():
    webbrowser.open_new(u2)
def open3():
    webbrowser.open_new(u3) 
def about1():
    messagebox.showinfo('Develope','Team psg')    
def about2 ():
    messagebox.showinfo('about project','SuperMarket project by python')          
def log():
   user=en1.get()
   passw=en2.get()
    
   if user =='username'and passw=='123456':
       messagebox.showinfo('Welecome','Welecome in SuberMarket')
   else :
        messagebox.showerror('Error','There is error')


f1=Frame(pro,width=230,height=420,bg='orange')
f1.place(x=570,y=37)
title1 = Label(f1,text=' Super Market Broject',bg='orange',fg='white',font=('tajawal',12,'bold'))
title1.place(x=30,y=10)
title2=Label(f1,text='Developed by Team psg',bg='orange',fg='white',font=('tajawal',12,'bold'))
title2.place(x=28,y=50)
title3=Label(f1,text='To Call Us',bg='orange',fg='white',font=('tajawal',12,'bold'))
title3.place(x=65,y=90)
b1=Button(f1,text='Facebook',width=13,fg='orange',bg='white',font=('tajawal',11,'bold'),command=open1)
b1.place(x=45,y=130)
b2=Button(f1,text='Telegram',width=13,fg='orange',bg='white',font=('tajawal',11,'bold'),command=open2)
b2.place(x=45,y=170)
b3=Button(f1,text='Youtube',width=13,fg='orange',bg='white',font=('tajawal',11,'bold'),command=open3)
b3.place(x=45,y=210)
b4=Button(f1,text='Develober',width=13,fg='orange',bg='white',font=('tajawal',11,'bold'),command=about1)
b4.place(x=45,y=250)
b5=Button(f1,text='summar of Project',width=14,fg='orange',bg='white',font=('tajawal',11,'bold'),command=about2)
b5.place(x=40,y=290)
b6=Button(f1,text='Close program',width=13,fg='orange',bg='white',font=('tajawal',11,'bold'),command=quit)
b6.place(x=45,y=330)

photo=PhotoImage(file="c:\\shop.png")
imo = Label(pro,image=photo)
imo.place(x=160,y=80)

f2=Frame(pro ,width=570,height=120,bg='orange')
f2.place(x=0,y=330)

photo1=PhotoImage(file="c:\\man.png")
imo1=Label(pro,image=photo1)
imo1.place(x=450,y=335,width=110,height=110)

l1=Label(f2,text='user name',fg='white',bg='orange',font=('tajawal',12,'bold'))
l1.place(x=330,y=25)
l2=Label(f2,text='password',fg='white',bg='orange',font=('tajawal',12,'bold'))
l2.place(x=330,y=70)

en1=Entry(f2,font=('tajawal',12),justify='center')
en1.place(x=130,y=26)
en2=Entry(f2,font=('tajawal',12),justify='center')
en2.place(x=130,y=71)

b=Button(f2,text='sign in',fg='orange',bg='white',font=('tajawal',15),width=8,height=1,command=superrr)
b.place(x=15,y=56)



pro.mainloop()