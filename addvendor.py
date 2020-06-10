import os
import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import Tk, Menu, ttk
import time
import datetime
import os
import sqlite3
import pandas as pd
import numpy as np
import csv

conn = sqlite3.connect("shop.db")
root = Tk()
root.title("VENDOR DETAILS")
root.geometry("700x742")
root.resizable(0, 0)
conn=sqlite3.connect("shop.db")
c3=conn.execute("SELECT value from clusterlength")
list222222=[]
for j in c3:
    list222222.append(j[0])
photo1 = PhotoImage(file='u1.png')
bk_img = Label(root, image=photo1)
bk_img.place(x=0, y=0, relwidth=1, relheight=1)


def back():
    root.destroy()
    os.system("python admin.py")


def proceed():
    for i in range(1):
        phone_no = (e2.get())
        vname = e1.get()
        if not phone_no.isnumeric():
            tkinter.messagebox.showinfo("Number Error", "Number should be numeric only!")
            break;
        if (len(phone_no) != 10):
            tkinter.messagebox.showinfo("Invalid ", "Invalid Number.Mobile No. must be 10 digit!")
            break;
        if vname.isalnum() and not vname.isalpha():
            tkinter.messagebox.showinfo("Name Error", "Name can not be numerical!")
            break;
        if (vname == ''):
            tkinter.messagebox.showinfo("Name Error", "Name can not be NULL")
            break;
        if ((v11.get() == 'DAY') | (v21.get() == 'MONTH') | (v31.get() == 'YEAR')):
            tkinter.messagebox.showinfo("Date Error", "Date or Date format wrong!")
            break;
        else:
            e = v21.get()
            k = int(0)
            for i in OPTIONS21:
                k = k + 1
                if (e == i):
                    e = k
                    break;
            d = str(v11.get()) + '/' + str(e) + '/' + str(v31.get())
            conn = sqlite3.connect("shop.db")
            conn.execute("INSERT INTO vendor_details VALUES(?,?,?)", [(vname), (phone_no), (d)]);
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("ADDED", 'vendor is added succsesfully')
            root.destroy()
            os.system("python admin.py")


def slice(entry):
    v = entry[2:]
    f = v[:-3]
    return f


def proceed1(r12, r14, r16):
    if ((r12.get() == '') | (r14.get() == '') | (r16.get() == '')):
        tkinter.messagebox.showinfo("Invalid", "VALUE cannot be NULL")
        pass
    else:
        a = []
        conn = sqlite3.connect("shop.db")
        c1 = conn.execute("SELECT PTYPE FROM particulars")
        for i in c1:
            a.append(slice(str(i)))
        if r12.get() in a:
            pass
        else:
            conn.execute("INSERT INTO particulars VALUES(?)", [(r12.get())]);
        conn.execute("INSERT INTO typebrand VALUES(?,?,?)", [(r12.get()), (r14.get()), (r16.get())]);
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo("ADDED", 'new stock updated succsesfully')
        root.destroy()
        os.system("python admin.py")


import csv


def offer():
    b11122.destroy()
    b111.destroy()
    l1 = Label(root, text="Enter Name:", font=('Franklin Gothic Medium', 12, 'bold'), bg="WHITE", fg="WHITE")
    l1.place(x=10, y=80)
    e1 = Entry(root, width=30, bg='WHITE', fg='WHITE')
    e1.place(x=150, y=80)
    l2 = Label(root, text="Mobile NO:", font=('Franklin Gothic Medium', 12, 'bold'), bg="WHITE", fg="WHITE")
    l2.place(x=14, y=130)
    e2 = Entry(root, width=30, bg='WHITE', fg='WHITE')
    e2.place(x=150, y=130)
    l117 = Label(text="D-O-B:", font=('Franklin Gothic Medium', 12), bg='WHITE', fg='WHITE')
    l117.place(x=30, y=180)
    l1 = Label(root, text="                                             ", font=('Franklin Gothic Medium', 12, 'bold'),
               bg="white", fg="white")
    l1.place(x=150, y=80)
    l12 = Label(root, text="                                             ", font=('Franklin Gothic Medium', 12, 'bold'),
                bg="white", fg="white")
    l12.place(x=150, y=130)
    l13 = Label(root, text="                                                       ",
                font=('Franklin Gothic Medium', 12, 'bold'), bg="white", fg="white")
    l13.place(x=120, y=180)
    list3 = []
    with open('E:\BE project\Shop\sbh.csv', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            list3.append(row)
    v111 = StringVar()
    w111 = ttk.Combobox(root, textvariable=v11, values=list3[0][1:31], width=8, state='readonly')
    w111.place(x=135, y=30)
    w111.set('ITEMS')
    l117 = Label(text="SELECT ITEM", font=('Franklin Gothic Medium', 12), bg='black', fg='yellow')
    l117.place(x=30, y=30)
    b5551 = Button(root, text="PROCEED", font=('Franklin Gothic Medium', 13, 'bold'), bg="light gray", fg="black",
                   command=lambda: proceed2(w111))
    b5551.place(x=270, y=250)


def proceed2(v111):
    a11 = []
    l = str(v111.get())

    dataset = pd.read_csv("sbh1.csv")
    f1 = dataset['110001'].values
    f2 = dataset['110003'].values
    f3 = dataset['131111'].values
    f4 = dataset['131113'].values
    f5 = dataset['131131'].values
    f6 = dataset['131133'].values
    f7 = dataset['131373'].values
    f8 = dataset['131371'].values
    f9 = dataset['131391'].values
    f10 = dataset['131393'].values
    f11 = dataset['133701'].values
    f12 = dataset['133703'].values
    f13 = dataset['133901'].values
    f14 = dataset['133903'].values
    f15 = dataset['317001'].values
    f16 = dataset['317003'].values
    f17 = dataset['319001'].values
    f18 = dataset['319003'].values
    f19 = dataset['331111'].values
    f20 = dataset['331113'].values
    f21 = dataset['331131'].values
    f22 = dataset['331133'].values
    f23 = dataset['331373'].values
    f24 = dataset['331371'].values
    f25 = dataset['331391'].values
    f26 = dataset['331393'].values
    f27 = dataset['333701'].values
    f28 = dataset['333703'].values
    f29 = dataset['333901'].values
    f30 = dataset['333903'].values
    X = np.array(list(
        zip(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23,
            f24, f25, f26, f27, f28, f29, f30)))
    from sklearn.cluster import KMeans
    q = list222222[0]
    print(q)
    kmeans = KMeans(n_clusters=q)
    kmeans.fit(X)
    # print(kmeans.cluster_centers_)
    # print(kmeans.labels_)

    conn = sqlite3.connect("shop.db")
    c1=conn.execute("select count(*) from customer_details")
    for i in c1:
        uniquser=i[0]
    c2=conn.execute("select * from clusterlength")
    for i in c2:
        clusterl=i[0]

    for j in range(0,clusterl):
        s2 = 0
        da=[]
        f22=list(kmeans.labels_).count(j)
        for i in range(0, uniquser):
            if (j == kmeans.labels_[i]):
                c3 = conn.execute("SELECT a" + l + " FROM kmeans WHERE u=?", [i])
                for k in c3:
                    s2=s2+int(k[0])
                da.append(i)
        s2=s2/f22
        if(s2>0.2):
            print(da)


l1 = Label(root, text="Enter Name:", font=('Franklin Gothic Medium', 12, 'bold'), bg="lawn green", fg="black")
l1.place(x=10, y=80)
e1 = Entry(root, width=30, bg='light gray', fg='black')
e1.place(x=150, y=80)
l2 = Label(root, text="Mobile NO:", font=('Franklin Gothic Medium', 12, 'bold'), bg="cyan", fg="black")
l2.place(x=14, y=130)
e2 = Entry(root, width=30, bg='light gray', fg='black')
e2.place(x=150, y=130)
l117 = Label(text="D-O-B:", font=('Franklin Gothic Medium', 12), bg='red', fg='black')
l117.place(x=30, y=180)
OPTIONS11 = []
for i in range(31):
    OPTIONS11.append(i + 1)
v11 = StringVar()
w11 = ttk.Combobox(root, textvariable=v11, values=OPTIONS11, width=8, state='readonly')
w11.place(x=125, y=180)
w11.set('DAY')
OPTIONS21 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
             'november', 'december']
v21 = StringVar()
w21 = ttk.Combobox(root, textvariable=v21, values=OPTIONS21, width=10, state='readonly')
w21.place(x=195, y=180)
w21.set('MONTH')
OPTIONS31 = []
for i in range(101):
    OPTIONS31.append(2018 - i)
v31 = StringVar(root)
w31 = ttk.Combobox(root, textvariable=v31, values=OPTIONS31, width=10, state='readonly')
w31.place(x=275, y=180)
w31.set('YEAR')
b1 = Button(root, text="PROCEED", font=('Franklin Gothic Medium', 13, 'bold'), bg="light gray", fg="black",
            command=proceed)
b1.place(x=270, y=250)
b2 = Button(root, text="BACK", font=('Franklin Gothic Medium', 13, 'bold'), bg="light gray", fg="black", command=back)
b2.place(x=10, y=250)


def refresh():
    root.destroy()
    os.system("python addvendor.py")


b557 = Button(root, text="REFRESH", font=('Franklin Gothic Medium', 12, 'bold'), bg="light gray", fg="black",
              command=refresh)
b557.place(x=130, y=250)


def newstock():
    r11 = Label(root, text="  Particular  ", font=('Franklin Gothic Medium', 12, 'bold'), bg="lawn green", fg="black")
    r11.place(x=10, y=80)
    r12 = Entry(root, width=30, bg='light gray', fg='black')
    r12.place(x=150, y=80)
    r13 = Label(root, text="     Type     ", font=('Franklin Gothic Medium', 12, 'bold'), bg="cyan", fg="black")
    r13.place(x=10, y=130)
    r14 = Entry(root, width=30, bg='light gray', fg='black')
    r14.place(x=150, y=130)
    r15 = Label(root, text="    Brand    ", font=('Franklin Gothic Medium', 12, 'bold'), bg="red", fg="black")
    r15.place(x=12, y=180)
    r16 = Entry(root, width=40, bg='light gray', fg='black')
    r16.place(x=125, y=180)
    b555 = Button(root, text="PROCEED", font=('Franklin Gothic Medium', 13, 'bold'), bg="light gray", fg="black",
                  command=lambda: proceed1(r12, r14, r16))
    b555.place(x=270, y=250)
    b556 = Button(root, text="BACK", font=('Franklin Gothic Medium', 13, 'bold'), bg="light gray", fg="black",
                  command=back)
    b556.place(x=10, y=250)
    b111.destroy()
    b11122.destroy()


b111 = Button(root, text="ADD NEW STOCK", font=('Franklin Gothic Medium', 10, 'bold'), bg="light gray", fg="black",
              command=newstock)
b111.place(x=10, y=25)
##b11122 = Button(root, text=" OFFER  ", font=('Franklin Gothic Medium', 12, 'bold'), bg="light gray", fg="black",
##                command=offer)
##b11122.place(x=250, y=20)
root.mainloop()
