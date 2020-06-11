import os
import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import Tk, Menu, ttk
from datetime import date
import random
import pandas as pd
import numpy as np
import time
import datetime
from random import seed
from random import randint

root = Tk()
root.title("offer")
root.geometry("1280x768")
root.resizable(0, 0)
photo1=PhotoImage(file='u5.png')
bk_img=Label(root,image=photo1)
bk_img.place(x=0,y=0,relwidth=1,relheight=1)
a = []
b = []
C = []
D = []

conn = sqlite3.connect("shop.db")

c2 = conn.execute("SELECT PTYPE FROM PARTICULARS ")
for i in c2:
    b.append(i)
OPTIONS2 = b
v2 = StringVar()
w2 = ttk.Combobox(root, textvariable=v2, values=OPTIONS2, width=10, state='readonly')
w2.place(x=495, y=50)
w2.set('select')

l3 = Label(text="PARTICULARS", font=('Franklin Gothic Medium', 12), fg='white', bg='gray10')
l3.place(x=380, y=50)
b1 = Button(root, text="PROCEED", font=('Franklin Gothic Medium', 13, 'bold'), fg='black', bg='light gray',
            command=lambda: proceed())
b1.place(x=600, y=50)


# v1111=IntVar()
# e11=Entry(root,textvariable=v1111,state=DISABLED,width=30)

def mess(particular,brand,typ,offerenddate,offerpercentage,numbers):
    message="Flat "+offerpercentage+"% off on "+particular+" of type "+typ" on brand "+brand+".So hurry up offer is only valid till"+offerenddate+"."
#    apikey='apikey'
#    sender='senderkey'

#    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
#        'message' : message, 'sender': sender})
#    data = data.encode('utf-8')
#    request = urllib.request.Request("https://api.textlocal.in/send/?")
#    f = urllib.request.urlopen(request, data)
#    fr = f.read()
#    print(fr)
    print(message)

def proceed():
    if ((v2.get() == 'select')):
        tkinter.messagebox.showinfo("Invalid", "PLEASE SELECT APPROPRIATE VALUES")
        pass
    else:

        p = v2.get()
        conn = sqlite3.connect("shop.db")
        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", [p])

        for i in c3:
            C.append(i)
        OPTIONS3 = C
        v3 = StringVar()
        w3 = ttk.Combobox(root, textvariable=v3, values=OPTIONS3, width=10, state='readonly')
        w3.set('select')
        w3.place(x=434, y=120)
        l4 = Label(text="TYPE", font=('Franklin Gothic Medium', 12), fg='cyan', bg='gray10')
        l4.place(x=380, y=120)

        list14 = []

        c4 = conn.execute("SELECT distinct(brand) FROM typebrand WHERE particular=?", [p])

        for i in c4:
            D.append(i)
        OPTIONS4 = D
        v4 = StringVar()
        w4 = ttk.Combobox(root, textvariable=v4, values=OPTIONS4, width=10, state='readonly')
        w4.set('select')
        w4.place(x=604, y=120)
        l5 = Label(text="BRAND", font=('Franklin Gothic Medium', 12), fg='cyan', bg='gray10')
        l5.place(x=535, y=120)
        l117 = Label(text="DATE:", font=('Franklin Gothic Medium', 12), bg='gray10', fg='yellow2')
        l117.place(x=380, y=180)
        OPTIONS11 = []
        for i in range(31):
            OPTIONS11.append(i + 1)
        v11 = StringVar()

        w11 = ttk.Combobox(root, textvariable=v11, values=OPTIONS11, width=5, state='readonly')
        w11.place(x=440, y=180)
        w11.set('DAY')
        OPTIONS21 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                     'november', 'december']
        v21 = StringVar()
        w21 = ttk.Combobox(root, textvariable=v21, values=OPTIONS21, width=10, state='readonly')
        w21.place(x=490, y=180)
        w21.set('MONTH')
        OPTIONS31 = []
        for i in range(10):
            OPTIONS31.append(2019 + i)
        v31 = StringVar(root)
        w31 = ttk.Combobox(root, textvariable=v31, values=OPTIONS31, width=6, state='readonly')
        w31.place(x=570, y=180)
        w31.set('YEAR')

        l1172 = Label(text="OFFER PERCENTAGE:", font=('Franklin Gothic Medium', 12), bg='gray10', fg='cyan')
        l1172.place(x=380, y=240)
        OPTIONS3122 = []
        for i in range(11):
            OPTIONS3122.append(10*(i+1))
        v3122 = StringVar(root)
        w3122 = ttk.Combobox(root, textvariable=v3122, values=OPTIONS3122, width=12, state='readonly')
        w3122.place(x=540, y=240)
        w3122.set('PERCENTAGE')

        b1 = Button(root, text="PROCEED", font=('Franklin Gothic Medium', 13, 'bold'), fg='black', bg='light gray',
                    command=lambda: proceed1(p, v3, v4, v11, v21, v31,v3122))
        b1.place(x=650, y=240)


def proceed1(p, v3, v4, v11, v21, v31,v3122):
    aaa = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                 'november', 'december']
    t = v3.get()
    b = v4.get()
    day = v11.get()
    month = v21.get()
    year = v31.get()
    cen = v3122.get()
    for i in range(0,12):
        if(month==aaa[i]):
            month=str(i+1)
    ww=day+"/"+month+"/"+year
    localtime = time.asctime(time.localtime(time.time()))
    today = datetime.date.today()
    today = str(today)
    d2222 = today[8:10]
    m2222 = today[5:7]
    y2222 = today[0:4]
    xx = str(d2222) + '/' + str(m2222) + '/' + str(y2222)
    z = []
    conn = sqlite3.connect("shop.db")
    c3 = conn.execute("SELECT code FROM typebrand  WHERE particular=? and brand=? and type=?", [(p), (b), (t)])
    for j in c3:
        z.append(j)
    l1 = []
    if ((z[0][0] == 110001) | (z[0][0] == 110003) | (z[0][0] == 317001) | (z[0][0] == 317003) | (z[0][0] == 319001) | (
            z[0][0] == 319003)):
        l1.append(z[0][0])
        r1 = 0
    else:
        l1.append(z[0][0])
        m1 = z[0][0] + 200000
        l1.append(m1)
        r1 = randint(0, 1)
    d = []
    c3 = conn.execute("SELECT clusterno FROM clusterinfo")
    for i in c3:
        d.append(str(i))
    d1 = []
    for j in range(0, len(d)):
        d1.append(int(d[j][1:-2]))

    conn = sqlite3.connect("shop.db")
    c1=conn.execute("select count(*) from customer_details")
    for i in c1:
        uniquser=i[0]
    c2=conn.execute("select * from clusterlength")
    for i in c2:
        clusterl=i[0]
    bbbb = 0
    for j in range(0, clusterl):
        s2 = 0
        da = []
        da2= []
        f22 = d1.count(j)

        for i in range(0,uniquser):
            if (j == d1[i]):
                c3 = conn.execute("SELECT a" + str(l1[r1]) + " FROM kmeans WHERE u=?", [i])
                for k in c3:
                    s2 = s2 + int(k[0])
                da.append(i)
        s2 = s2 / f22
        if (s2 > 0.2):
            for rec in range(0,len(da)):
                c1 = conn.execute("SELECT phone_no1 from customer_details WHERE cname=?", [rec])
                for oph in c1:
                    phoneno=oph[0]
                    mess(p,b,t,ww,cen,phoneno) 
            print(da)
            bbbb = bbbb + len(da)
    if (bbbb < 1):
        c4 = conn.execute("select count(*) from kmeans where a" + str(l1[r1]) + ">=1")
        for k222 in c4:
            bbbb = k222[0]
        c44 = conn.execute("select u from kmeans where a" + str(l1[r1]) + ">=1")
        for k2222 in c44:
            bbbb2 = k2222[0]
            da2.append(bbbb2)
            c1 = conn.execute("SELECT phone_no1 from customer_details WHERE cname=?", [bbbb2])
            for oph in c1:
                phoneno=oph[0]
                mess(p,b,t,ww,cen,phoneno)
    print(bbbb)
    print(da2)
    conn = sqlite3.connect("shop.db")
    offerstartdate=date.today()
    conn.execute("INSERT INTO offerinfo VALUES(?,?,?,?,?,?)", [(p), (t), (b),(ww),(xx),(cen)]);
    conn.commit()
    root.destroy()
    os.system("python admin.py")


root.mainloop()
