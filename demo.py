import os
import sqlite3
from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("ADMIN LOGIN")
root.geometry("1366x768")
root.resizable(0,0)
def cp():
    root.destroy()
    os.system("python cp.py")
def bk():
    root.destroy()
    os.system("python admin.py")
def slice(entry):
    v=entry[2:]
    f=v[:-3]
    return f
def login(v11,e):
    un=v11.get()
    ps=e.get()
    conn=sqlite3.connect("shop.db")
    c1=conn.execute("SELECT USERNAME FROM ADMIN" )
    for i in c1:
        unn=slice(str(i))
    c2=conn.execute("SELECT PASSWORD FROM ADMIN" )
    for i in c2:
        psw=slice(str(i))
    if((un==unn)&(ps==psw)):
         root.destroy()
         os.system("python admin.py")
    else:
        tkinter.messagebox.showinfo("Invalid LOG IN", "Incorrect combination of username and password!")
def back():
    if(c.get()):
        v2=e2.get()
        e2.delete(0,END)
        e2.insert(0,v2)
        e2.config(show="")
        b3.config(command=lambda:login(e1,e2))   
    else:
        v2=e2.get()
        e2.delete(0,END)
        e2.insert(0,v2)
        e2.config(show='*')
        b3.config(command=lambda:login(e1,e2))
photo1=PhotoImage(file='aaa.png')
bk_img=Label(root,image=photo1)
bk_img.place(x=0,y=0,relwidth=1,relheight=1)
photo2=PhotoImage(file='utsavfashion.png')
bk_img2=Label(root,image=photo2)
bk_img2.place(x=950,y=50)
photo3=PhotoImage(file='abc1.png')
bk_img3=Label(root,image=photo3)
bk_img3.place(x=850,y=150)
photo4=PhotoImage(file='admin2.png')
bk_img4=Label(root,image=photo4)
bk_img4.place(x=900,y=220)
photo5=PhotoImage(file='pass1.png')
bk_img5=Label(root,image=photo5)
bk_img5.place(x=900,y=305)
l1=Label(root,text="Username",font=('Franklin Gothic Medium',11,'bold'),relief=FLAT )
l1.place(x=900,y=180)
e1=Entry(root,width=30)
e1.place(x=920,y=220)
l2=Label(root,text='Password',font=('Franklin Gothic Medium',11,'bold'))
l2.place(x=900,y=265)
e2=Entry(root,show='*',width=30)
e2.place(x=922,y=305)
b3=Button(root,text="login",command=lambda:login(e1,e2))
b3.place(x=1070,y=330)
b4=Button(root,text="Back",font=('Franklin Gothic Medium',11,'bold'),command=bk)
b4.place(x=900,y=430)
b5=Button(root,text="Change password",font=('Franklin Gothic Medium',11,'bold'),command=cp)
b5.place(x=1000,y=430)
c=IntVar()
b1=Checkbutton(root,text='Show password',variable=c,command=back)
b1.place(x=900,y=330)
mainloop()
