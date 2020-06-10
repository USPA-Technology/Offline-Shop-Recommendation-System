import os
import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import  Tk, Menu, ttk
import time
import datetime
import pandas as pd
import numpy as np
from random import seed
from random import randint
from apyori import apriori

def cross1(y1,n):
    m=(len(list22))
    for i in range(m):
        if(n==(i+1)):
            del list90[i*2:2+2*i]
    del list22[:]
    for i in range(m):
        list22.append(0)
##        y1=280+30*(len(list22))
##        l9=Label(text='     ',font=('Franklin Gothic Medium',12),bg='yellow')
##        l9.place(x=80,y=y1)
##        l10=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##        l10.place(x=100,y=y1)
##        l11=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##        l11.place(x=250,y=y1)
##        l12=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##        l12.place(x=400,y=y1)
##        l13=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##        l13.place(x=550,y=y1)
##        l14=Label(text='                    ',font=('Franklin Gothic Medium',12),bg='yellow')
##        l14.place(x=650,y=y1)
    listbox.delete(0,END)
    for i in range(n):
        if(i==n-1):
            del list222[i*5:5+i*5]
    list223=list222.copy()
    m=(len(list22))
    del list22[:]
    for i in range(m-1):
        if(len(list223)==0):
            break;
        list22.append(0)
##        y1=280+30*(len(list22))
##        l9=Label(text=str(i+1),font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l9.place(x=80,y=y1)
##        l10=Label(text='PARTICULAR:  '+list223[0],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l10.place(x=100,y=y1)
##        l11=Label(text='TYPE:  '+list223[1],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l11.place(x=250,y=y1)
##        l12=Label(text='BRAND:  '+list223[2],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l12.place(x=400,y=y1)
##        l13=Label(text='QUANTITY:  '+list223[3],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l13.place(x=550,y=y1)
##        l14=Label(text='PRICE:  '+list223[4],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l14.place(x=650,y=y1)        
        listbox.insert(END,str(i+1)+')'+'PARTICULAR: '+list223[0]+'     TYPE: '+list223[1]+'     BRAND: '+list223[2]+'     QUANTITY: '+list223[3]+'     PRICE: '+list223[4])
        listbox.insert(END,'                                                                                                         ')
        del list223[0:5]
    y1=150+32*(len(list22)+1)
    l9=Label(text='     ',font=('Franklin Gothic Medium',19),bg='white')
    l9.place(x=752,y=y1)
##    l10=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##    l10.place(x=100,y=y1)
##    l11=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##    l11.place(x=250,y=y1)
##    l12=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##    l12.place(x=400,y=y1)
##    l13=Label(text='                                                       ',font=('Franklin Gothic Medium',12),bg='yellow')
##    l13.place(x=550,y=y1)
##    l14=Label(text='                                                    ',font=('Franklin Gothic Medium',17),bg='yellow')
##    l14.place(x=650,y=y1+2)
def confirm(e111):
    e111=e111.get()
    z111=[]
    conn=sqlite3.connect("shop.db")
    c3=conn.execute("SELECT CNAME FROM CUSTOMER_DETAILS  WHERE phone_no1=?",[e111])
    for j in c3:
            z111.append(slice(str(j)))

    list28=[]
    l1=int((len(list222))/5)
    st=int(0)
    for i in range(l1):
        st=st+int(list222[(4*(i+1))+i])
    st=str(st)
    l15=Label(text='AMOUNT TO BE PAID  '+st,font=('Franklin Gothic Medium',30),fg='green4',bg='white')
    l15.place(x=820,y=300)
    l=int((len(list222))/5)
    for i in range(l):
        localtime=time.asctime(time.localtime(time.time()))
        today=str(datetime.date.today())
        day=(slice4(today))
        month=(slice2(today))
        year=(slice3(today))
        today1=(day+'/'+month+'/'+year)
        conn=sqlite3.connect("shop.db")
        conn.execute("INSERT INTO sales_report VALUES(?,?,?,?,?,?,?,?,?)",[(list222[0]),(list222[1]),(list222[2]),(list222[3]),(list222[4]),(today1),(month),(year),(z111[0])]);
        conn.commit()
        del list222[0:5]
    for i in range(l):
        conn=sqlite3.connect("shop.db")
        c3=conn.execute("SELECT quantity1 FROM stock_update1 WHERE id=?",[list90[2*i]])
        for j in c3:
            list28.append(slice1(str(j)))
        q=str(int(list28[0])-int(list90[2*i+1]))
        conn=sqlite3.connect("shop.db")
        conn.execute("UPDATE STOCK_UPDATE1 SET QUANTITY1="+q+" WHERE id=?",[list90[2*i]])
        conn.commit()
        del list28[:]
def pro1(p,v3,v4,e6,w3,l4,w4,l5,l6):
    if((v3.get()=='select')|(v4.get()=='select')|(e6.get()=='')|(not e6.get().isnumeric())):
        tkinter.messagebox.showinfo("Invalid", "PLEASE SELECT APPROPRIATE VALUES")
        pass
    else:
        list23=[]
        list24=[]
        list25=[]
        list26=[]
        list27=[]
        list22.append(0)
        e7=str(e6.get())
        vt=v3.get()
        vb=v4.get()
        conn=sqlite3.connect("shop.db")
        c0=conn.execute("SELECT type1 FROM stock_update1 WHERE particular1=?",[p])
        for i in c0:
            list23.append(slice(str(i)))
        c1=conn.execute("SELECT brand1 FROM stock_update1 WHERE particular1=?",[p])
        for i in c1:
            list24.append(slice(str(i)))
        c2=conn.execute("SELECT sales_rate1 FROM stock_update1 WHERE particular1=?",[p])
        for i in c2:
            list25.append(slice1(str(i)))
        c3=conn.execute("SELECT quantity1 FROM stock_update1 WHERE particular1=?",[p])
        for i in c3:
            list26.append(slice1(str(i)))
        c4=conn.execute("SELECT id FROM stock_update1 WHERE particular1=?",[p])
        for i in c4:
            list27.append(slice1(str(i)))
        m=(len(list23))
        for i in range(m):
            if((list23[i]==vt)&(list24[i]==vb)):
                price=int((list25[i]))
        for i in range(m):
            if((list23[i]==vt)&(list24[i]==vb)):
                e70=(list27[i])
                e71=int(e7)
                list90.append(e70)
                list90.append(e71)
        y1=150+32*(len(list22))
    ##    l9=Label(text=len(list22),font=('Franklin Gothic Medium',12),fg='red',bg='black')
    ##    l9.place(x=80,y=y1)
    ##    l10=Label(text='PARTICULAR:  '+p,font=('Franklin Gothic Medium',12),fg='red',bg='black')
    ##    l10.place(x=100,y=y1)
    ##    l11=Label(text='TYPE:  '+vt,font=('Franklin Gothic Medium',12),fg='red',bg='black')
    ##    l11.place(x=250,y=y1)
    ##    l12=Label(text='BRAND:  '+vb,font=('Franklin Gothic Medium',12),fg='red',bg='black')
    ##    l12.place(x=400,y=y1)
    ##    l13=Label(text='QUANTITY:  '+e7,font=('Franklin Gothic Medium',12),fg='red',bg='black')
    ##    l13.place(x=550,y=y1)
        e71=int(e7)
        price1=(e71*price)
        price1=str(e71*price)
    ##    l14=Label(text='PRICE:  '+price1,font=('Franklin Gothic Medium',12),fg='red',bg='black')
    ##    l14.place(x=650,y=y1)
        list222.append(p)
        list222.append(vt)
        list222.append(vb)
        list222.append(e7)
        list222.append(price1)
        l1=int((len(list222))/5)
        listbox.insert(END,str(l1)+')'+'PARTICULAR: '+p+'     TYPE: '+vt+'     BRAND: '+vb+'     QUANTITY: '+e7+'     PRICE: '+price1)
        listbox.insert(END,'                                                                        ')
        b4=Button(text="X",font=('Franklin Gothic Medium',12),fg='black',bg='white',command=lambda:cross1(y1,l1))
        b4.place(x=752,y=y1)
        w3.destroy()
        l4.destroy()
        w4.destroy()
        l5.destroy()
        l6.destroy()
        e6.destroy()
        start()
def proceed(v2,e111):
    if((v2.get()=='select')):
        tkinter.messagebox.showinfo("Invalid", "PLEASE SELECT APPROPRIATE VALUES")
        pass
    else:
        p=v2.get()
        C=[]
        conn=sqlite3.connect("shop.db")    
        c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",[p])
        #c3=conn.execute( "SELECT TYPE FROM {}".format(p))
        for i in c3:
            C.append(slice(str(i)))
        OPTIONS3=C
        v3=StringVar()
        w3=ttk.Combobox(root,textvariable=v3,values=OPTIONS3,width=10,state='readonly')
        w3.place(x=85,y=100)
        w3.set('select')
        l4=Label(text="TYPE",font=('Franklin Gothic Medium',12),fg='BLACK',bg='CYAN')
        l4.place(x=30,y=100)
        D=[]
        list14=[]    
        c4=conn.execute("SELECT distinct(brand) FROM typebrand WHERE particular=?",[p])
        #c4=conn.execute( "SELECT BRAND FROM {}".format(p))
        for i in c4:
            D.append(slice(str(i)))
        OPTIONS4=D
        v4=StringVar()
        w4=ttk.Combobox(root,textvariable=v4,values=OPTIONS4,width=10,state='readonly')
        w4.place(x=255,y=100)
        w4.set('select')
        l5=Label(text="BRAND",font=('Franklin Gothic Medium',12),fg='snow',bg='GREEN4')
        l5.place(x=185,y=100)
        l6=Label(text="QUANTITY",font=('Franklin Gothic Medium',12),fg='red',bg='black')
        l6.place(x=355,y=100)
        e6=Entry(root,width=12,bg='LIGHT GRAY')
        e6.place(x=450,y=105)
        b2=Button(text="ADD",font=('Franklin Gothic Medium',12),fg='black',bg='light gray',command=lambda:pro1(p,v3,v4,e6,w3,l4,w4,l5,l6))
        b2.place(x=30,y=610)
        b3=Button(text="CONFIRM",font=('Franklin Gothic Medium',12),fg='black',bg='light gray',command=lambda:confirm(e111))
        b3.place(x=672,y=610)
        b321=Button(text="REFRESH",font=('Franklin Gothic Medium',12),fg='black',bg='light gray',command=lambda:refresh1())
        b321.place(x=352,y=610)
def refresh1():
    root.destroy()
    os.system("python home.py")
def slice(entry):
    v=entry[2:]
    f=v[:-3]
    return f
def slice1(entry):
    v=entry[1:]
    f=v[:-2]
    return f
def slice2(entry):
    v=entry[5:]
    f=v[:-3]
    return f
def slice3(entry):
    f=entry[:-6]
    return f
def slice4(entry):
    f=entry[8:]
    return f
def cus(e111):
    
    for i in range(1):
        num=e111.get()
        if not num.isnumeric():
            tkinter.messagebox.showinfo("Number Error", "Number can be numeric only!")
            break;
        if (len(num) != 10):
            tkinter.messagebox.showinfo("Number", "Invalid Number.Mobile No. must be 10 digit!")
            break;
        list231=[]
        list241=[]
        e111=e111.get()
        conn=sqlite3.connect("shop.db")
        c0=conn.execute("SELECT cname FROM customer_details WHERE phone_no1=?",[e111])
        for i in c0:
            list231.append(slice(str(i)))
        c1=conn.execute("SELECT dob FROM customer_details WHERE phone_no1=?",[e111])
        for i in c1:
            list241.append(slice(str(i)))
        if((len(list231))!=0):
            l112=Label(text="NAME:",font=('Franklin Gothic Medium',12),fg='SNOW',bg='GREEN4')
            l112.place(x=1060,y=130)
            v1111=IntVar()
            l114=Entry(root,textvariable=v1111,state=DISABLED,width=25,bg='gray')
            l114.place(x=1150,y=130)
            v1111.set(str(list231[0]))
            l113=Label(text="D-O-B:",font=('Franklin Gothic Medium',12),fg='black',bg='cyan')
            l113.place(x=1062,y=160)
            v1112=IntVar()
            l115=Entry(root,textvariable=v1112,state=DISABLED,width=10,bg='gray')
            l115.place(x=1150,y=160)
            v1112.set(str(list241[0]))


            e1112=e111.get()
            z111=[]
            conn=sqlite3.connect("shop.db")
            c3=conn.execute("SELECT CNAME FROM CUSTOMER_DETAILS  WHERE phone_no1=?",[e1112])
            for j in c3:
                    z111.append(slice(str(j)))
            print(z111[0])
            g(z111[0])




            
        elif((len(list231))==0):
            l116=Label(text="NAME:",font=('Franklin Gothic Medium',12),fg='snow',bg='green4')
            l116.place(x=1060,y=130)
            e112=Entry(root,width=30,bg='light gray')
            e112.place(x=1148,y=130)
            l117=Label(text="D-O-B:",font=('Franklin Gothic Medium',12),fg='snow',bg='black')
            l117.place(x=1062,y=160)
            OPTIONS11=[]
            for i in range(31):
                OPTIONS11.append(i+1)
            v11=StringVar()
            w11=ttk.Combobox(root,textvariable=v11,values=OPTIONS11,width=8,state='readonly')
            w11.place(x=1130,y=160)
            w11.set('DAY')
            OPTIONS21=['january','february','march','april','may','june','july','august','september','october','november','december']
            v21=StringVar()
            w21=ttk.Combobox(root,textvariable=v21,values=OPTIONS21,width=10,state='readonly')
            w21.place(x=1200,y=160)
            w21.set('MONTH')
            OPTIONS31=[]
            for i in range(101):
                OPTIONS31.append(2018-i)
            v31=StringVar(root)
            w31=ttk.Combobox(root,textvariable=v31,values=OPTIONS31,width=8,state='readonly')
            w31.place(x=1280,y=160)
            w31.set('YEAR')
            b1=Button(text="proceed",font=('Franklin Gothic Medium',12),fg='black',bg='light gray',command=lambda:cus1(e112,e111,v11,v21,v31,OPTIONS21))
            b1.place(x=1180,y=200)
def cus1(e112,e111,v11,v21,v31,OPTIONS21):
    z11122 = []
    conn = sqlite3.connect("shop.db")
    c3 = conn.execute("SELECT CNAME FROM CUSTOMER_DETAILS")
    for j in c3:
        z11122.append(slice(str(j)))
    wwww = len(z11122)

    conn.execute("INSERT INTO kmeans VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 [wwww,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,e111]);
    conn.commit()
    
    conn = sqlite3.connect("shop.db")
    conn.execute("INSERT INTO recency VALUES(?,?,?)",
                 [0,2000,0]);
    conn.commit()

    conn = sqlite3.connect("shop.db")
    conn.execute("INSERT INTO rank VALUES(?,?,?,?)",
                 [3,3,3,3]);
    conn.commit()
    
    for i in range(1):
        name=e112.get()
        if  name.isalnum() and not name.isalpha():
            tkinter.messagebox.showinfo("Name Error", "Name can not be numerical!")
            break;
        if(name==''):
            tkinter.messagebox.showinfo("Name Error", "Name can not be NULL")
            break;
        if((v11.get()=='DAY')|(v21.get()=='MONTH')|(v31.get()=='YEAR')):
            tkinter.messagebox.showinfo("Date Error","Date or Date format wrong!")
            break;
        e=v21.get()
        k=int(0)
        for i in OPTIONS21:
                k=k+1
                if(e==i):
                    e=k
                    break;
        e112=e112.get()
        d=str(v11.get())+'/'+str(e)+'/'+str(v31.get())
        conn=sqlite3.connect("shop.db")
        conn.execute("INSERT INTO customer_details VALUES(?,?,?)",[(wwww),(e111),(d)]);
        conn.commit()
        conn.close()
######################################################################################################################################
root=Tk()
root.title("ADMIN ")
root.geometry("1366x768")
root.config(bg="white")
root1=Frame(root,bg='white')
root1.place(x=30,y=180)
listbox = Listbox(root1,width=70,height=18,font=('Franklin Gothic Medium',13),bg='light gray',fg='black')
scrollbar1 = Scrollbar(root1, orient="horizontal")
scrollbar1.config(command=listbox.xview)
scrollbar1.pack(side="bottom",fill="x")
listbox.pack(side='left')
scrollbar = Scrollbar(root1, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="left", fill="y")
listbox.config(xscrollcommand=scrollbar1.set)
listbox.config(yscrollcommand=scrollbar.set)
list22=[]
list222=[]
list90=[]
x11=[]
l111=Label(text="PHONE_NO:",font=('Franklin Gothic Medium',12),fg='snow',bg='black')
l111.place(x=1050,y=30)
e111=Entry(root,width=20,bg='LIGHT gray')
e111.place(x=1150,y=30)
b1=Button(text="PROCEED",font=('Franklin Gothic Medium',11),fg='BLACK',bg='light GRAY',command=lambda:cus(e111))
b1.place(x=1120,y=70)
l111=Label(text="RECOMMENDATION:",font=('Franklin Gothic Medium',12),fg='snow',bg='black')
l111.place(x=1030,y=270)
e22222=IntVar()
e2222=Entry(root,textvariable=e22222,state=DISABLED,width=25,bg='LIGHT gray')
e2222.place(x=1180,y=270)
e222221=IntVar()
e2222=Entry(root,textvariable=e222221,state=DISABLED,width=25,bg='LIGHT gray')
e2222.place(x=1180,y=290)


conn=sqlite3.connect("shop.db")
c3=conn.execute("SELECT value from clusterlength")
list222222=[]
for j in c3:
    list222222.append(j[0])

def balance4(l4,l2,l3,b100,w111,w211,w1111,w2111,l21,l31,b1000,b22222):
    l4.destroy()
    l2.destroy()
    l3.destroy()
    l21.destroy()
    l31.destroy()
    b100.destroy()
    b1000.destroy()
    w211.destroy()
    w111.destroy()
    w2111.destroy()
    w1111.destroy()
    b22222.destroy()
def balance3(v111,v211,v1111,v2111,l2,l3,b100,w111,w211,w1111,w2111,l21,l31,b1000):
    conn=sqlite3.connect("shop.db")
    data=[]
    data1=[]
    q="SELECT total1 From stock_update1 WHERE (vname1=? and particular1=? and type1=? and brand1=?)"
    b=conn.execute(q,[v111.get(),v211.get(),v1111.get(),v2111.get()])
    for i in b:
        data.extend(i)
    q1="SELECT payment1 From stock_update1 WHERE (vname1=? and particular1=? and type1=? and brand1=?)"
    b1=conn.execute(q1,[v111.get(),v211.get(),v1111.get(),v2111.get()])
    for j in b1:
        data1.extend(j)
    l4=Label(text='BALANCE AMOUNT:'+str(data[0]-data1[0]),font=('Franklin Gothic Medium',15),fg='red',bg='snow')
    l4.place(x=1050,y=565)
    b22222=Button(text="REFRESH",font=('Franklin Gothic Medium',11),fg='BLACK',bg='light GRAY',command=lambda:balance4(l4,l2,l3,b100,w111,w211,w1111,w2111,l21,l31,b1000,b22222))
    b22222.place(x=1120,y=610)
def balance2(v111,v211,l2,l3,b100,w111,w211):
    a=[]
    b=[]
    conn=sqlite3.connect("shop.db")

    c1=conn.execute("SELECT type FROM typebrand where particular=?",[v211.get()])
    for i in c1:
        a.append(slice(str(i)))
    OPTIONS1=a
    v1111=StringVar(root)    
    w1111=ttk.Combobox(root,textvariable=v1111,values=OPTIONS1,width=10,state='readonly')
    w1111.set('select')
    w1111.place(x=1020,y=520)

    c2=conn.execute("SELECT brand FROM typebrand where particular=?",[v211.get()])
    for i in c2:
        b.append(slice(str(i)))
    OPTIONS2=b
    v2111=StringVar()    
    w2111=ttk.Combobox(root,textvariable=v2111,values=OPTIONS2,width=10,state='readonly')
    w2111.set('select')
    w2111.place(x=1195,y=520)
    l21=Label(text="TYPE",font=('Franklin Gothic Medium',10),fg='white',bg='gray10')
    l21.place(x=958,y=520)
    l31=Label(text="BRAND",font=('Franklin Gothic Medium',10),fg='white',bg='gray10')
    l31.place(x=1128,y=520)        
    b1000=Button(text="PROCEED",font=('Franklin Gothic Medium',9),fg='BLACK',bg='light GRAY',command=lambda:balance3(v111,v211,v1111,v2111,l2,l3,b100,w111,w211,w1111,w2111,l21,l31,b1000))
    b1000.place(x=1280,y=517)
def balance1():
    a=[]
    b=[]
    conn=sqlite3.connect("shop.db")

    c1=conn.execute("SELECT VNAME FROM VENDOR_DETAILS ")
    for i in c1:
        a.append(slice(str(i)))
    OPTIONS1=a
    v111=StringVar(root)    
    w111=ttk.Combobox(root,textvariable=v111,values=OPTIONS1,width=10,state='readonly')
    w111.set('select')
    w111.place(x=1020,y=470)

    c2=conn.execute("SELECT PTYPE FROM PARTICULARS ")
    for i in c2:
        b.append(slice(str(i)))
    OPTIONS2=b
    v211=StringVar()    
    w211=ttk.Combobox(root,textvariable=v211,values=OPTIONS2,width=10,state='readonly')
    w211.set('select')
    w211.place(x=1195,y=470)
    l2=Label(text="VENDOR NAME",font=('Franklin Gothic Medium',10),fg='white',bg='gray10')
    l2.place(x=930,y=470)
    l3=Label(text="PARTICULARS",font=('Franklin Gothic Medium',10),fg='white',bg='gray10')
    l3.place(x=1110,y=470)        
    b100=Button(text="PROCEED",font=('Franklin Gothic Medium',9),fg='BLACK',bg='light GRAY',command=lambda:balance2(v111,v211,l2,l3,b100,w111,w211))
    b100.place(x=1280,y=467)
def start():
    b=[]
    conn=sqlite3.connect("shop.db")
    c2=conn.execute("SELECT PTYPE FROM PARTICULARS ")
    for i in c2:
        b.append(slice(str(i)))
    OPTIONS2=b
    v2=StringVar()
    w2=ttk.Combobox(root,textvariable=v2,values=OPTIONS2,width=10,state='readonly')
    w2.place(x=140,y=30)
    w2.set('select')
    l3=Label(text="PARTICULARS:",font=('Franklin Gothic Medium',11),fg='WHITE',bg='BLACK')
    l3.place(x=30,y=30)
    b1=Button(text="PROCEED",font=('Franklin Gothic Medium',11),fg='BLACK',bg='LIGHT GRAY',command=lambda:proceed(v2,e111))
    b1.place(x=250,y=30)
    b322=Button(text="ADMIN LOGIN",font=('Franklin Gothic Medium',18),fg='GREEN4',bg='SNOW',command=lambda:refresh2())
    b322.place(x=640,y=30)
def refresh2():
    root.destroy()
    os.system("python demo.py")
b22222=Button(text="BALANCE",font=('Franklin Gothic Medium',11),fg='BLACK',bg='light GRAY',command=lambda:balance1())
b22222.place(x=1120,y=610)

    
def refres(c):
            x11.clear()
            x=[]
            if(c=="110001"):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["ethical"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("fabindia")
                d2.append("biba")
                
                r2=randint(0,len(d2)-1)
                x.append("ethical")
                x.append(d1[r1])
                x.append(d2[r2])
            if(c=="110003"):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["ethical"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("melange")
                d2.append("shree")
                r2=randint(0,len(d2)-1)
                x.append("ethical")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131111")|(c=="331111")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["tshirt"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("nike")
                d2.append("adidas")
                r2=randint(0,len(d2)-1)
                x.append("tshirt")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131113")|(c=="331113")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["tshirt"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("tommy")
                d2.append("lacoste")
                d2.append("gucci")
                r2=randint(0,len(d2)-1)
                x.append("tshirt")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131131")|(c=="331131")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["shirt"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("nike")
                d2.append("adidas")
                r2=randint(0,len(d2)-1)
                x.append("shirt")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131133")|(c=="331133")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["shirt"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("tommy")
                d2.append("lacoste")
                d2.append("gucci")        
                r2=randint(0,len(d2)-1)
                x.append("shirt")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131371")|(c=="331371")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["sum"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("jockey")
                
                r2=randint(0,len(d2)-1)
                x.append("sum")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131373")|(c=="331373")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["sum"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("domyos")    
                r2=randint(0,len(d2)-1)
                x.append("sum")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131391")|(c=="331391")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["winter"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("raymonds")
                d2.append("peter_eng")
                r2=randint(0,len(d2)-1)
                x.append("winter")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="131393")|(c=="331393")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["winter"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("montecarlo")
                        
                r2=randint(0,len(d2)-1)
                x.append("winter")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="133701")|(c=="333701")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["jeans"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("pepe")
                d2.append("levis")
                d2.append("wrangler")
                r2=randint(0,len(d2)-1)
                x.append("jeans")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="133703")|(c=="333703")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["jeans"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("lee")
                d2.append("diesel")
                        
                r2=randint(0,len(d2)-1)
                x.append("jeans")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="133901")|(c=="333901")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["trousers"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("jcrew")
                d2.append("lestrange")
                
                r2=randint(0,len(d2)-1)
                x.append("trousers")
                x.append(d1[r1])
                x.append(d2[r2])
            if((c=="133903")|(c=="333903")):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["trousers"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("rhone")
            
                r2=randint(0,len(d2)-1)
                x.append("trousers")
                x.append(d1[r1])
                x.append(d2[r2])
            if(c=="317001"):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["kurtas"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("fabindia")
                d2.append("aurelia")
                
                r2=randint(0,len(d2)-1)
                x.append("kurtas")
                x.append(d1[r1])
                x.append(d2[r2])
            if(c=="317003"):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["kurtas"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("biba")
                d2.append("libas")
                r2=randint(0,len(d2)-1)
                x.append("kurtas")
                x.append(d1[r1])
                x.append(d2[r2])
            if(c=="319001"):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["sarees"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("satyapaul")
                d2.append("sabyasachi")
                
                r2=randint(0,len(d2)-1)
                x.append("sarees")
                x.append(d1[r1])
                x.append(d2[r2])
            if(c=="319003"):
                d1=[]
                conn=sqlite3.connect("shop.db")
                c3=conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?",["sarees"])
                for k in c3:
                    d1.append(slice(str(k)))
                r1=randint(0,len(d1)-1)
                d2=[]
                d2.append("ritu")
                d2.append("tarun")
                r2=randint(0,len(d2)-1)
                x.append("sarees")
                x.append(d1[r1])
                x.append(d2[r2])
            for i in range(0,len(x)):
                x11.append(x[i])
                





def g(v1):
##    dataset = pd.read_csv("sbh1.csv")
##    f1 = dataset['110001'].values
##    f2 = dataset['110003'].values
##    f3 = dataset['131111'].values
##    f4 = dataset['131113'].values
##    f5 = dataset['131131'].values
##    f6 = dataset['131133'].values
##    f7 = dataset['131373'].values
##    f8 = dataset['131371'].values
##    f9 = dataset['131391'].values
##    f10 = dataset['131393'].values
##    f11 = dataset['133701'].values
##    f12 = dataset['133703'].values
##    f13 = dataset['133901'].values
##    f14 = dataset['133903'].values
##    f15 = dataset['317001'].values
##    f16 = dataset['317003'].values
##    f17 = dataset['319001'].values
##    f18 = dataset['319003'].values
##    f19 = dataset['331111'].values
##    f20 = dataset['331113'].values
##    f21 = dataset['331131'].values
##    f22 = dataset['331133'].values
##    f23 = dataset['331373'].values
##    f24 = dataset['331371'].values
##    f25 = dataset['331391'].values
##    f26 = dataset['331393'].values
##    f27 = dataset['333701'].values
##    f28 = dataset['333703'].values
##    f29 = dataset['333901'].values
##    f30 = dataset['333903'].values
##    X = np.array(list(
##        zip(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24,
##            f25, f26, f27, f28, f29, f30)))
##    from sklearn.cluster import KMeans

    q = list222222[0]
    print(q)
##  kmeans = KMeans(n_clusters=q)
##  kmeans.fit(X)
    #print(kmeans.cluster_centers_)
    #print(kmeans.labels_)
    d2222=[]
    conn = sqlite3.connect("shop.db")
    c3=conn.execute("SELECT clusterno FROM clusterinfo")
    for i in c3:
	d2222.append(str(i))
    km=[]
    for j in range(0,len(d2222)):
            km.append(int(d2222[j][1:-2]))
##    print(km)
    conn.commit()
    
    import csv
    v1=int(v1)
    v2=km[v1]
    conn = sqlite3.connect("shop.db")
    data = []

    c1=conn.execute("select count(*) from customer_details")
    for i in c1:
        uniquser=i[0]

    
    for j in range(v2,v2+1):
        for i in range(0, uniquser):
            if (j == km[i]):
                c3 = conn.execute("SELECT * FROM kmeans WHERE u=?", [i])
                for k in c3:
                    data.append(k)
    list1 = []
    list3 = []
    with open('sbh1.csv', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            list3.append(row)
    for i2 in range(0, len(data)):
        p = []
        for j2 in range(1, 31):
            if (data[i2][j2] >= 1):
                p.append(list3[0][j2])

        list1.append(p)

    m = list1
    with open('d22.csv', 'w', newline='') as my:
        writer = csv.writer(my)
        writer.writerows(m)


    list5 = []
    with open('d22.csv', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            list5.append(row)


    association_rules = apriori(list5, min_support=0.5, min_confidence=0.7)
    association_results = list(association_rules)
    print(len(association_results))
    print(association_results)

    data2=[]
    c5 = conn.execute("SELECT * FROM kmeans WHERE u=?", [v1])
    for k in c5:
        data2.append(k)
    p1=[]
    p2=[]
    for item in association_results:
        for i in range(0,len(item[2])):
            b1=str(item[2][i][0])[11:-2]
            b2 = str(item[2][i][1])[11:-2]
            print("Rule: " + b1 + " -> " + b2)
            if((len(b1)==8)&(len(b2)==8)):
                x=0
                y=0
                for i2 in range(1, 31):
                    if(b1[1:-1]==list3[0][i2]):
                        if(data2[0][i2]>0):
                            x=x+1
                            break
                for i2 in range(1, 31):
                    if(b2[1:-1]==list3[0][i2]):
                        if(data2[0][i2]>0):
                            y=y+1
                            break
                if((x>0)&(y==0)):
                    p1.append(b2)
                    print(b2)
            if ((len(b1) == 18) & (len(b2) == 8)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if ((b1[1:8] == list3[0][i2])|(b1[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            x = x + 1
                for i2 in range(1, 31):
                    if (b2[1:-1] == list3[0][i2]):
                        if (data2[0][i2] > 0):
                            y = y + 1
                            break
                if ((x==2) & (y == 0)):
                    p1.append(b2)
                    print(b2)
            if ((len(b1) == 8) & (len(b2) == 18)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if ((b2[1:8] == list3[0][i2])|(b2[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            x = x + 1
                for i2 in range(1, 31):
                    if (b1[1:-1] == list3[0][i2]):
                        if (data2[0][i2] > 0):
                            y = y + 1
                            break
                if ((x==0) & (y == 1)):
                    p1.append(b2[0:8])
                    p1.append(b2[10:])
                    print(b2[10:])
            if ((len(b1) == 18) & (len(b2) == 18)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if ((b1[1:8] == list3[0][i2])|(b1[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            x = x + 1
                    if ((b2[1:8] == list3[0][i2])|(b2[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            y = y + 1
                if ((x==2) & (y == 0)):
                    p1.append(b2[0:8])
                    p1.append(b2[10:])
                    print(b2)
            if((len(b1)==0)&(len(b2)==8)):
                for i2 in range(1, 31):
                    if(b2[1:-1]==list3[0][i2]):
                        p2.append(b2)
                        print(b2)


                        
    p1=list(dict.fromkeys(p1))
    p2=list(dict.fromkeys(p2))
    
    o=''
    o1=''
    if(len(p1)==1):
        refres(p1[0][1:-1])
        o=o+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
        refres(p2[-1][1:-1])
        o1=o1+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
    elif(len(p1)>1):
        refres(p1[-2][1:-1])
        o=o+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
        refres(p1[-1][1:-1])
        o1=o1+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
    if(len(p1)==0):
        if(len(p2)==1):
            refres(p2[0][1:-1])
            o=o+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
        elif(len(p2)>1):
            refres(p2[-2][1:-1])
            o=o+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
            refres(p2[-1][1:-1])
            o1=o1+str(x11[0])+' '+str(x11[1])+" "+str(x11[2])
    e22222.set(o)
    e222221.set(o1)
start()
mainloop()






















        
