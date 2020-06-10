import os
import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import  Tk, Menu, ttk
import tkinter as tk
import time
import datetime
def slice(entry):
    v=entry[2:]
    f=v[:-3]
    return f
def slice1(entry):
    v=entry[1:]
    f=v[:-2]
    return f
def back():
    root.destroy()
    os.system("python admin.py")
def proceed1(listbox):
##    for i in range(m):
##        l9=Label(text='         ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##        l9.place(x=80,y=300+30*i)
##        l10=Label(text='                                                             ' ,font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##        l10.place(x=100,y=300+30*i)
##        l11=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##        l11.place(x=250,y=300+30*i)
##        l12=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##        l12.place(x=400,y=300+30*i)
##        l13=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##        l13.place(x=550,y=300+30*i)
##        l14=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##        l14.place(x=700,y=300+30*i)
    listbox.delete(0,END)
def proceed():
    root1=Frame(root)
    root1.place(x=190,y=170)
    listbox = Listbox(root1,width=65,height=14,font=('Franklin Gothic Medium',11),bg='gray85',fg='black')
    scrollbar1 = Scrollbar(root1, orient="horizontal")
    scrollbar1.config(command=listbox.xview)
    scrollbar1.pack(side="bottom",fill="x")
    listbox.pack(side='left')
    scrollbar = Scrollbar(root1, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="left", fill="y")
    listbox.config(xscrollcommand=scrollbar1.set)
    listbox.config(yscrollcommand=scrollbar.set)
    lb1=Label(text='PARTICULAR',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
    lb1.place(x=210,y=120)
    lb2=Label(text='TYPE',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
    lb2.place(x=348,y=120)
    lb3=Label(text='BRAND',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
    lb3.place(x=428,y=120)
    lb4=Label(text='QUANTITY',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
    lb4.place(x=530,y=120)
    lb5=Label(text='BALANCE AMOUNT',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
    lb5.place(x=635,y=120)
    proceed1(listbox)
    list30=[]
    list31=[]
    list32=[]
    list33=[]
    list34=[]
    list35=[]
    list36=[]
    list37=[]
    list38=[]
    v=v1.get()    
    conn=sqlite3.connect("shop.db")
    c0=conn.execute("SELECT particular FROM stock_update WHERE vname=?",[v])
    for i in c0:
        list30.append(slice(str(i)))
    c1=conn.execute("SELECT type FROM stock_update WHERE vname=?",[v])
    for i in c1:
        list31.append(slice(str(i)))
    c2=conn.execute("SELECT brand FROM stock_update WHERE vname=?",[v])
    for i in c2:
        list32.append(slice(str(i)))
    c3=conn.execute("SELECT quantity FROM stock_update WHERE vname=?",[v])
    for i in c3:
        list33.append(slice1(str(i)))
    c4=conn.execute("SELECT purchase_rate FROM stock_update WHERE vname=?",[v])
    for i in c4:
        list34.append(slice1(str(i)))
    c5=conn.execute("SELECT sales_rate FROM stock_update WHERE vname=?",[v])
    for i in c5:
        list35.append(slice1(str(i)))
    c6=conn.execute("SELECT total FROM stock_update WHERE vname=?",[v])
    for i in c6:
        list36.append(slice1(str(i)))
    c7=conn.execute("SELECT phoneno FROM stock_update WHERE vname=?",[v])
    for i in c7:
        list37.append(slice1(str(i)))
    c8=conn.execute("SELECT payment FROM stock_update WHERE vname=?",[v])
    for i in c8:
        list38.append(slice1(str(i)))
    list22.pop()
    list22.append(len(list30))
    for i in range(list22[0]):
##        l9=Label(text=str(i+1),font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l9.place(x=80,y=300+30*i)
##        l10=Label(text='PARTICULAR:  '+list30[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l10.place(x=100,y=300+30*i)
##        l11=Label(text='TYPE:  '+list31[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l11.place(x=250,y=300+30*i)
##        l12=Label(text='BRAND:  '+list32[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l12.place(x=400,y=300+30*i)
##        l13=Label(text='QUANTITY:  '+list33[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l13.place(x=550,y=300+30*i)
        str5=str((int(list36[i]))-(int(list38[i])))
##        l14=Label(text='BALANCE AMOUNT:  '+str5,font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l14.place(x=700,y=300+30*i)       
        listbox.insert(END,str(i+1)+')'+'          '+list30[i]+'               '+list31[i]+'               '+list32[i]+'                         '+list33[i]+'                    '+str5)
        listbox.insert(END,'                                                                                                         ')
    b2=Button(root,text="BACK",font=('Franklin Gothic Medium',13,'bold'),bg="light gray",fg="black",command=back)
    b2.place(x=460,y=500)
root=Tk()
root.title("VENDOR REPORT")
root.geometry("1000x562")
root.resizable(0,0)
photo1=PhotoImage(file='u8.png')
bk_img=Label(root,image=photo1)
bk_img.place(x=0,y=0)
##l9=Label(text='         ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##l10=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##l11=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##l12=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##l13=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
##l14=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
list22=[5]
a=[]
conn=sqlite3.connect("shop.db")
c1=conn.execute("SELECT VNAME FROM VENDOR_DETAILS ")
for i in c1:
    a.append(slice(str(i)))
OPTIONS1=a
w1=ttk.Combobox(root)
v1=StringVar()
w1.config(textvariable=v1,values=OPTIONS1,width=10,state='readonly')
w1.set('NAME')
w1.place(x=450,y=55)
l1=Label(text="VENDOR NAME",font=('Franklin Gothic Medium',12),fg='RED',bg='white')
l1.place(x=330,y=50)
b1=Button(text="PROCEED",font=('Franklin Gothic Medium',13),fg='BLACK',bg='LIGHT GRAY',command=lambda:proceed())
b1.place(x=570,y=45)
mainloop()
