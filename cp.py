import os
import sqlite3
from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("ADMIN LOGIN")
root.geometry("1366x768")
root.resizable(0,0)
def cn(e11,e21):
    id=1
    a1=e11.get()
    a2=e21.get()
    if((len(str(a2))>=8)&(('!' in a2)|('@' in a2)|('#' in a2)|('$' in a2)|('%' in a2)|('^' in a2)|('&' in a2)|('*' in a2))):         
        conn=sqlite3.connect("shop.db")
        conn.execute("DELETE FROM ADMIN WHERE ID=?",[(id)])
        conn.execute("INSERT INTO ADMIN VALUES(?,?,?)",[(a1),(a2),(id)]);
        conn.commit()
        root.destroy()
        os.system("python demo.py")
    elif(len(str(a2))<8):       
        tkinter.messagebox.showinfo(" Error", "Password should be of atleast 8 characters")
    elif((('!' not in a2)&('@' not in a2)&('#' not in a2)&('$' not in a2)&('%' not in a2)&('^' not in a2)&('&' not in a2)&('*' not in a2))):        
        tkinter.messagebox.showinfo(" Error", "Password should contain atleast one special character('!','@','#','$','%','^','&','*')")
def bk():
    root.destroy()
    os.system("python demo.py")

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
        l0.destroy()
        l5=Label(root,text="ENTER THE NEW USERNAME AND PASSWORD",font=('Franklin Gothic Medium',11,'bold'),relief=FLAT)
        l5.place(x=855,y=160)
        e1.destroy()
        e2.destroy()
        b1.destroy()
        b3.destroy()
        b4.destroy()
        e11=Entry(root,width=30)
        e11.place(x=920,y=230)      
        e21=Entry(root,show='*',width=30)
        e21.place(x=922,y=305)
        d=IntVar()
        b11=Checkbutton(root,text='Show password',variable=d,command=lambda:back1(e11,e21,b5,d))
        b11.place(x=900,y=330)
        b5=Button(root,text="confirm",command=lambda:cn(e11,e21))
        b5.place(x=1055,y=330)

    else:

        tkinter.messagebox.showinfo("Invalid LOG IN", "Incorrect combination of username and password!")
def back1(e11,e,b5,d):
    if(d.get()):
        v2=e.get()
        e.delete(0,END)
        e.insert(0,v2)
        e.config(show="")
        b5.config(command=lambda:cn(e11,e)) 
    else:
        v2=e.get()
        e.delete(0,END)
        e.insert(0,v2)
        e.config(show='*')
        b5.config(command=lambda:cn(e11,e))
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
bk_img4.place(x=900,y=230)
photo5=PhotoImage(file='pass1.png')
bk_img5=Label(root,image=photo5)
bk_img5.place(x=900,y=305)
l0=Label(root,text="ENTER THE OLD USERNAME AND PASSWORD",font=('Franklin Gothic Medium',11,'bold'),relief=FLAT )
l0.place(x=855,y=160)
l1=Label(root,text="Username",font=('Franklin Gothic Medium',11,'bold'),relief=FLAT )
l1.place(x=900,y=195)
e1=Entry(root,width=30)
e1.place(x=920,y=230)
l2=Label(root,text='Password',font=('Franklin Gothic Medium',11,'bold'))
l2.place(x=900,y=265)
e2=Entry(root,show='*',width=30)
e2.place(x=922,y=305)
b3=Button(root,text="login",command=lambda:login(e1,e2))
b3.place(x=1070,y=330)
b4=Button(root,text="Back",font=('Franklin Gothic Medium',11,'bold'),command=bk)
b4.place(x=900,y=430)
c=IntVar()
b1=Checkbutton(root,text='Show password',variable=c,command=back)
b1.place(x=900,y=330)
mainloop()
