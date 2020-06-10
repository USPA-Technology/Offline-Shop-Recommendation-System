import os
import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import  Tk, Menu, ttk
import time
import datetime
def slice1(entry):
    v=entry[1:]
    f=v[:-2]
    return f
def back():
    root.destroy()
    os.system("python admin.py")
def pro(v,p,v3,v4,e6,e7,e8,e9,ph,e10,e11):
    if((v3.get()=='select')|(v4.get()=='select')|(not e6.get().isnumeric())|(not e7.get().isnumeric())|(not e8.get().isnumeric())|(not e9.get().isnumeric())|
       (not e10.get().isnumeric())|
       (e6.get()=='')|(e7.get()=='')|(e8.get()=='')|(e9.get()=='')|(e10.get()=='')|(e11.get()=='')|(v=='select')|(p=='select')):
        tkinter.messagebox.showinfo("Invalid", "PLEASE SELECT APPROPRIATE VALUES.ALSO VALUES CANNOT BE NULL")
        pass
    else:
        list29=[]
        list30=[]
        list31=[]
        list32=[]
        list33=[]
        list34=[]
        list35=[]
        list36=[]
        list37=[]
        list38=[]
        list39=[]
        list40=[]
        vt=v3.get()
        vb=v4.get()
        e6=e6.get()
        e7=e7.get()
        e8=e8.get()
        e9=e9.get()
        e10=e10.get()
        e11=e11.get()
        conn=sqlite3.connect("shop.db")
        conn.execute("INSERT INTO stock_update VALUES(?,?,?,?,?,?,?,?,?,?,?)",[(v),(p),(vt),(vb),(e6),(e7),(e8),(e9),(ph),(e10),(e11)]);
        conn.commit()
        c10=conn.execute("SELECT vname1 FROM stock_update1 ")
        for i in c10:
            list29.append(slice(str(i)))
        c0=conn.execute("SELECT particular1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c0:
            list30.append(slice(str(i)))
        c1=conn.execute("SELECT type1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c1:
            list31.append(slice(str(i)))
        c2=conn.execute("SELECT brand1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c2:
            list32.append(slice(str(i)))
        c3=conn.execute("SELECT quantity1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c3:
            list33.append(slice1(str(i)))
        c4=conn.execute("SELECT purchase_rate1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c4:
            list34.append(slice1(str(i)))
        c5=conn.execute("SELECT sales_rate1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c5:
            list35.append(slice1(str(i)))
        c6=conn.execute("SELECT total1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c6:
            list36.append(slice1(str(i)))
        c7=conn.execute("SELECT phoneno1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c7:
            list37.append(slice1(str(i)))
        c8=conn.execute("SELECT id FROM stock_update1 WHERE vname1=?",[v])
        for i in c8:
            list38.append(slice1(str(i)))
        c9=conn.execute("SELECT payment1 FROM stock_update1 WHERE vname1=?",[v])
        for i in c9:
            list39.append(slice1(str(i)))
        m=len(list30)
        m1=len(list29)
        for i in range(m):
            if((list30[i]==p)&(list31[i]==vt)&(list32[i]==vb)):
                e71=int(e6)
                add=str(int(list33[i])+e71)
                conn=sqlite3.connect("shop.db")
                conn.execute("UPDATE stock_update1 SET quantity1="+add+" WHERE id=?",[(list38[i])])            
                conn.execute("UPDATE stock_update1 SET purchase_rate1="+e7+" WHERE id=?",[(list38[i])])             
                conn.execute("UPDATE stock_update1 SET sales_rate1="+e8+" WHERE id=?",[(list38[i])])
                add2=str(int(list36[i])+int(e9))
                conn.execute("UPDATE stock_update1 SET total1="+add2+" WHERE id=?",[(list38[i])])
                add1=str(int(list39[i])+int(e10))
                conn.execute("UPDATE stock_update1 SET payment1="+add1+" WHERE id=?",[(list38[i])])
                conn.commit()
                conn.close()
                list40.append(0)
                break;
        if(len(list40)==0):
            count=(m1+1)
            conn=sqlite3.connect("shop.db")
            conn.execute("INSERT INTO stock_update1 VALUES(?,?,?,?,?,?,?,?,?,?,?)",[(v),(p),(vt),(vb),(e6),(e7),(e8),(e9),(ph),(count),(e10)]);
            conn.commit()
            conn.close()
        root.destroy()
        os.system("python admin.py")
def proceed():
    if((v1.get()=='select')|(v2.get()=='select')):
        tkinter.messagebox.showinfo("Invalid", "PLEASE SELECT APPROPRIATE VALUES")
        pass
    else:
        v=v1.get()
        p=v2.get()
    ##    list44=[]
    ##    list45=[]
        conn=sqlite3.connect("shop.db")
    ##    str1='VNAME'
    ##    c11=conn.execute("SELECT "+str1+" FROM VENDOR_DETAILS ")
    ##    for i in c11:
    ##        list44.append(0)
    ##        g1=(slice(str(i)))
    ##        if(v==g1):
    ##            g2=(len(list44))
    ##            break;
    ##    c12=conn.execute("SELECT phone_no FROM VENDOR_DETAILS ")
    ##    for i in c12:
    ##        list45.append(slice(str(i)))
    ##    ph=(list45[-g2]) 
        c0=conn.execute("SELECT PHONE_NO FROM VENDOR_DETAILS WHERE VNAME=?",[v])
        for i in c0:
            ph=(slice(str(i)))
        C=[]
        conn=sqlite3.connect("shop.db")    
        c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",[p])
        ##c3=conn.execute( "SELECT TYPE FROM {}".format(p))
        for i in c3:
            C.append(slice(str(i)))
        OPTIONS3=C
        v3=StringVar()    
        w3=ttk.Combobox(root,textvariable=v3,values=OPTIONS3,width=10,state='readonly')
        w3.set('select')
        w3.place(x=470,y=120)
        l4=Label(text="TYPE",font=('Franklin Gothic Medium',12),fg='yellow2',bg='gray10')
        l4.place(x=380,y=120)
        D=[]
        list14=[]    
        c4=conn.execute("SELECT distinct(brand) FROM typebrand WHERE particular=?",[p])
        ##c4=conn.execute( "SELECT BRAND FROM {}".format(p))
        for i in c4:
            D.append(slice(str(i)))
        OPTIONS4=D
        v4=StringVar()    
        w4=ttk.Combobox(root,textvariable=v4,values=OPTIONS4,width=10,state='readonly')
        w4.set('select')
        w4.place(x=690,y=120)
        l5=Label(text="BRAND",font=('Franklin Gothic Medium',12),fg='yellow2',bg='gray10')
        l5.place(x=590,y=120)
        l6=Label(text="QUANTITY",font=('Franklin Gothic Medium',12),fg='cyan2',bg='gray10')
        l6.place(x=350,y=200)
        e6=Entry(root,bg='light gray',width=30)
        e6.place(x=490,y=200)
        l7=Label(text="PURCHASE_RATE",font=('Franklin Gothic Medium',12),fg='red2',bg='gray10')
        l7.place(x=350,y=270)
        e7=Entry(root,bg='light gray',width=30)
        e7.place(x=490,y=270)
        l8=Label(text="SALES_RATE",font=('Franklin Gothic Medium',12),fg='green2',bg='gray10')
        l8.place(x=350,y=340)
        e8=Entry(root,bg='light gray',width=30)
        e8.place(x=490,y=340)
        l9=Label(text="TOTAL AMOUNT",font=('Franklin Gothic Medium',12),fg='azure',bg='gray10')
        l9.place(x=350,y=410)
        e9=Entry(root,bg='light gray',width=30)
        e9.place(x=490,y=410)
        l10=Label(text="PAYMENT",font=('Franklin Gothic Medium',12),fg='turquoise1',bg='gray10')
        l10.place(x=350,y=480)
        e10=Entry(root,bg='light gray',width=30)
        e10.place(x=490,y=480)       
        l11=Label(root,text="DATE(dd/mm/yyyy)",font=('Franklin Gothic Medium',12,'bold'),bg="gray10",fg="orange")
        l11.place(x=350,y=550)   
        e11.place(x=520,y=550)
        e11.config(bg='light gray')
        localtime=time.asctime(time.localtime(time.time()))
        today=datetime.date.today()
        today=str(today)
        d2=today[8:10]
        m2=today[5:7]
        y2=today[0:4]
        xx=str(d2)+'/'+str(m2)+'/'+str(y2)
        v1111.set(xx)
        b2=Button(root,text="PROCEED",font=('Franklin Gothic Medium',13,'bold'),bg="light gray",fg="black",command=lambda:pro(v,p,v3,v4,e6,e7,e8,e9,ph,e10,e11))
        b2.place(x=750,y=620)
        b3=Button(root,text="BACK",font=('Franklin Gothic Medium',13,'bold'),bg="light gray",fg="black",command=back)
        b3.place(x=350,y=620)
def slice(entry):
    v=entry[2:]
    f=v[:-3]
    return f
######################################################################################################################################
root=Tk()
root.title("UPDATE STOCK")
root.geometry("1280x768")
root.resizable(0,0)
photo1=PhotoImage(file='u5.png')
bk_img=Label(root,image=photo1)
bk_img.place(x=0,y=0,relwidth=1,relheight=1)
a=[]
b=[]
conn=sqlite3.connect("shop.db")

c1=conn.execute("SELECT VNAME FROM VENDOR_DETAILS ")
for i in c1:
    a.append(slice(str(i)))
OPTIONS1=a
v1=StringVar(root)
w1=ttk.Combobox(root,textvariable=v1,values=OPTIONS1,width=10,state='readonly')
w1.set('select')
w1.place(x=470,y=50)

c2=conn.execute("SELECT PTYPE FROM PARTICULARS ")
for i in c2:
    b.append(slice(str(i)))
OPTIONS2=b
v2=StringVar()
w2=ttk.Combobox(root,textvariable=v2,values=OPTIONS2,width=10,state='readonly')
w2.place(x=690,y=50)
w2.set('select')
l2=Label(text="VENDOR NAME",font=('Franklin Gothic Medium',12),fg='white',bg='gray10')
l2.place(x=350,y=50)
l3=Label(text="PARTICULARS",font=('Franklin Gothic Medium',12),fg='white',bg='gray10')
l3.place(x=570,y=50)
b1=Button(root,text="PROCEED",font=('Franklin Gothic Medium',13,'bold'),fg='black',bg='light gray',command=proceed)
b1.place(x=780,y=50)
v1111=IntVar()
e11=Entry(root,textvariable=v1111,state=DISABLED,width=30)
mainloop()
