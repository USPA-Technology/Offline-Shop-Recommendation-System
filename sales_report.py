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
def back():
    root.destroy()
    os.system("python admin.py")
def proceed1(l9,l10,l11,l12,l13,l14,m):
    listbox.delete(0,END)
def pro1(l9,l10,l11,l12,l13,l14,v11,date,v21,v31,OPTIONS21):
    k=int(0)
    proceed1(l9,l10,l11,l12,l13,l14,list22[0])
    list50=[]
    list51=[]
    list52=[]
    list53=[]
    list54=[]
    stt1=date
    if(stt1=='year'):
        e=v11.get()
    if(stt1=='date'):
        e1=v21.get()
        for i in OPTIONS21:
            k=k+1
            if(e1==i):
                e1=k
                break;
        a=int(v11.get())
        if((e1>=10)&(a>=10)):
            e=str(v11.get())+'/'+str(e1)+'/'+str(v31.get())
        if((e1<10)&(a<10)):
            e=str('0'+v11.get())+'/0'+str(e1)+'/'+str(v31.get())
        if((e1>=10)&(a<10)):
            e=str('0'+v11.get())+'/'+str(e1)+'/'+str(v31.get())
        if((e1<10)&(a>=10)):
            e=str(v11.get())+'/0'+str(e1)+'/'+str(v31.get())
    conn=sqlite3.connect("shop.db")
    conn.commit()
    c0=conn.execute("SELECT particular3 FROM sales_report WHERE "+stt1+"=?",[e])
    for i in c0:
        list50.append(slice(str(i)))
    c1=conn.execute("SELECT type3 FROM sales_report WHERE "+stt1+"=?",[e])
    for i in c1:
        list51.append(slice(str(i)))
    c2=conn.execute("SELECT brand3 FROM sales_report WHERE "+stt1+"=?",[e])
    for i in c2:
        list52.append(slice(str(i)))
    c3=conn.execute("SELECT quantity3 FROM sales_report WHERE "+stt1+"=?",[e])
    for i in c3:
        list53.append(slice1(str(i)))
    c4=conn.execute("SELECT price3 FROM sales_report WHERE "+stt1+"=?",[e])
    for i in c4:
        list54.append(slice1(str(i)))
    list22.pop()
    list22.append(len(list50))
    m=len(list50)
    for i in range(m):
        listbox.insert(END,str(i+1)+')'+'          '+list50[i]+'               '+list51[i]+'               '+list52[i]+'                         '+list53[i]+'                    '+list54[i])
        listbox.insert(END,'                                                                                                         ')
##        l9=Label(text=str(i+1),font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l9.place(x=80,y=300+30*i)
##        l10=Label(text='PARTICULAR:  '+list50[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l10.place(x=100,y=300+30*i)
##        l11=Label(text='TYPE:  '+list51[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l11.place(x=250,y=300+30*i)
##        l12=Label(text='BRAND:  '+list52[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l12.place(x=400,y=300+30*i)
##        l13=Label(text='QUANTITY:  '+list53[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l13.place(x=550,y=300+30*i)
##        l14=Label(text='PRICE  '+list54[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##        l14.place(x=700,y=300+30*i)
def pro2(l9,l10,l11,l12,l13,l14,e1,date,v3,OPTIONS2):
    k=int(0)
    proceed1(l9,l10,l11,l12,l13,l14,list22[0])
    list50=[]
    list51=[]
    list52=[]
    list53=[]
    list54=[]
    list55=[]
    stt1=date
    e=e1.get()
    v3=v3.get()
    if(stt1=='month'):
        for i in OPTIONS2:
            k=k+1
            if(e==i):
                e=k
                break;
    e=str(e)
    conn=sqlite3.connect("shop.db")
    c0=conn.execute("SELECT particular3 FROM sales_report WHERE year=?",[v3])
    for i in c0:
        list50.append(slice(str(i)))
    c1=conn.execute("SELECT type3 FROM sales_report WHERE year=?",[v3])
    for i in c1:
        list51.append(slice(str(i)))
    c2=conn.execute("SELECT brand3 FROM sales_report WHERE year=?",[v3])
    for i in c2:
        list52.append(slice(str(i)))
    c3=conn.execute("SELECT quantity3 FROM sales_report WHERE year=?",[v3])
    for i in c3:
        list53.append(slice1(str(i)))
    c4=conn.execute("SELECT price3 FROM sales_report WHERE year=?",[v3])
    for i in c4:
        list54.append(slice1(str(i)))
    c5=conn.execute("SELECT month FROM sales_report WHERE year=?",[v3])
    for i in c5:
        list55.append(slice1(str(i)))
    list22.pop()
    list22.append(len(list50))
    m=len(list50)
    k=int(0)
    for i in range(m):
        if(list55[i]==e):
            listbox.insert(END,str(k+1)+')'+'          '+list50[i]+'               '+list51[i]+'               '+list52[i]+'                         '+list53[i]+'                    '+list54[i])
            listbox.insert(END,'                                                                                                         ')
##            l9=Label(text=str(i+1),font=('Franklin Gothic Medium',12),fg='red',bg='black')
##            l9.place(x=80,y=300+30*k)
##            l10=Label(text='PARTICULAR:  '+list50[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##            l10.place(x=100,y=300+30*k)
##            l11=Label(text='TYPE:  '+list51[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##            l11.place(x=250,y=300+30*k)
##            l12=Label(text='BRAND:  '+list52[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##            l12.place(x=400,y=300+30*k)
##            l13=Label(text='QUANTITY:  '+list53[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##            l13.place(x=550,y=300+30*k)
##            l14=Label(text='PRICE  '+list54[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##            l14.place(x=700,y=300+30*k)
            k=k+1
root=Tk()
root.title("SALES_REPORT")
root.geometry("1000x562")
root.resizable(0,0)
photo1=PhotoImage(file='u6.png')
bk_img=Label(root,image=photo1)
bk_img.place(x=0,y=0)
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
list22=[' ']
l9=Label(text='         ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
l10=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
l11=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
l12=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
l13=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
l14=Label(text='                                                             ',font=('Franklin Gothic Medium',12),fg='yellow',bg='yellow')
list30=[]
list31=[]
list32=[]
list33=[]
list34=[]
list35=[]
list36=[]
list37=[]
localtime=time.asctime(time.localtime(time.time()))
today=str(datetime.date.today())
day=(slice4(today))
month=(slice2(today))
year=(slice3(today))
today1=(day+'/'+month+'/'+year)
conn=sqlite3.connect("shop.db")
conn.commit()
c0=conn.execute("SELECT particular3 FROM sales_report WHERE date=?",[today1])
for i in c0:
    list30.append(slice(str(i)))
c1=conn.execute("SELECT type3 FROM sales_report WHERE date=?",[today1])
for i in c1:
    list31.append(slice(str(i)))
c2=conn.execute("SELECT brand3 FROM sales_report WHERE date=?",[today1])
for i in c2:
    list32.append(slice(str(i)))
c3=conn.execute("SELECT quantity3 FROM sales_report WHERE date=?",[today1])
for i in c3:
    list33.append(slice1(str(i)))
c4=conn.execute("SELECT price3 FROM sales_report WHERE date=?",[today1])
for i in c4:
    list34.append(slice1(str(i)))
##c5=conn.execute("SELECT date FROM sales_report ")
##for i in c5:
##    list35.append(slice1(str(i)))
##c6=conn.execute("SELECT month FROM sales_report ")
##for i in c6:
##    list36.append(slice1(str(i)))
##c7=conn.execute("SELECT year FROM sales_report ")
##for i in c7:
##    list37.append(slice1(str(i)))
m=len(list30)
list22.pop()
list22.append(len(list30))
for i in range(m):        
    listbox.insert(END,str(i+1)+')'+'          '+list30[i]+'               '+list31[i]+'               '+list32[i]+'                         '+list33[i]+'                    '+list34[i])
    listbox.insert(END,'                                                                                                         ')
##    l9=Label(text=str(i+1),font=('Franklin Gothic Medium',12),fg='red',bg='black')
##    l9.place(x=80,y=300+30*i)
##    l10=Label(text='PARTICULAR:  '+list30[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##    l10.place(x=100,y=300+30*i)
##    l11=Label(text='TYPE:  '+list31[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##    l11.place(x=250,y=300+30*i)
##    l12=Label(text='BRAND:  '+list32[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##    l12.place(x=400,y=300+30*i)
##    l13=Label(text='QUANTITY:  '+list33[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##    l13.place(x=550,y=300+30*i)
##    l14=Label(text='PRICE:  '+list34[i],font=('Franklin Gothic Medium',12),fg='red',bg='black')
##    l14.place(x=700,y=300+30*i)
b01=Button(text="DAY",font=('Franklin Gothic Medium',15),fg='red',bg='WHITE',command=lambda:day())
b01.place(x=50,y=50)
b02=Button(text="MONTH",font=('Franklin Gothic Medium',15),fg='dark green',bg='WHITE',command=lambda:month())
b02.place(x=110,y=50)
b03=Button(text="YEAR",font=('Franklin Gothic Medium',15),fg='cyan4',bg='WHITE',command=lambda:year())
b03.place(x=196,y=50)
w11=ttk.Combobox(root)
w21=ttk.Combobox(root)
w31=ttk.Combobox(root)
w2=ttk.Combobox(root)
w3=ttk.Combobox(root)
w4=ttk.Combobox(root)
b1=Button(root)
b2=Button(root)
b3=Button(root)
lb1=Label(text='PARTICULAR',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
lb1.place(x=210,y=120)
lb2=Label(text='TYPE',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
lb2.place(x=348,y=120)
lb3=Label(text='BRAND',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
lb3.place(x=428,y=120)
lb4=Label(text='QUANTITY',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
lb4.place(x=530,y=120)
lb5=Label(text='PRICE',font=('Franklin Gothic Medium',14),fg='YELLOW',bg='black')
lb5.place(x=642,y=120)
b2222=Button(root,text="BACK",font=('Franklin Gothic Medium',13,'bold'),bg="light gray",fg="black",command=back)
b2222.place(x=460,y=500)
def day():
    b2.place_forget()
    b3.place_forget()
    w2.place_forget()
    w3.place_forget()
    w4.place_forget()
    OPTIONS11=[]
    for i in range(31):
        OPTIONS11.append(i+1)
    v11=StringVar()
    w11.config(textvariable=v11,values=OPTIONS11,width=10,state='readonly')
    w11.place(x=650,y=60)
    w11.set('DAY')
    OPTIONS21=['january','february','march','april','may','june','july','august','september','october','november','december']
    v21=StringVar()
    w21.config(textvariable=v21,values=OPTIONS21,width=10,state='readonly')
    w21.place(x=730,y=60)
    w21.set('MONTH')
    OPTIONS31=[]
    for i in range(101):
        OPTIONS31.append(2018+i)
    v31=StringVar()
    w31.config(textvariable=v31,values=OPTIONS31,width=10,state='readonly')
    w31.place(x=810,y=60)
    w31.set('YEAR')
    b1.config(text="PROCEED",font=('Franklin Gothic Medium',13),fg='black',bg='light gray',command=lambda:pro1(l9,l10,l11,l12,l13,l14,v11,'date',v21,v31,OPTIONS21))
    b1.place(x=910,y=53)
def month():
    b1.place_forget()
    b3.place_forget()
    w11.place_forget()
    w21.place_forget()
    w31.place_forget()
    w4.place_forget()
    OPTIONS2=['january','february','march','april','may','june','july','august','september','october','november','december']
    v2=StringVar()
    w2.config(textvariable=v2,values=OPTIONS2,width=10,state='readonly')
    w2.place(x=690,y=60)
    w2.set('MONTH')
    OPTIONS3=[]
    for i in range(101):
        OPTIONS3.append(2018+i)
    v3=StringVar()
    w3.config(textvariable=v3,values=OPTIONS3,width=10,state='readonly')
    w3.place(x=790,y=60)
    w3.set('YEAR')
    b2.config(text="PROCEED",font=('Franklin Gothic Medium',13),fg='BLACK',bg='light gray',command=lambda:pro2(l9,l10,l11,l12,l13,l14,v2,'month',v3,OPTIONS2))
    b2.place(x=900,y=53)
def year():
    b1.place_forget()
    b2.place_forget()
    w11.place_forget()
    w21.place_forget()
    w31.place_forget()
    w2.place_forget()
    w3.place_forget()
    OPTIONS4=[]
    for i in range(101):
        OPTIONS4.append(2018+i)
    v4=StringVar()
    w4.config(textvariable=v4,values=OPTIONS4,width=10,state='readonly')
    w4.set('YEAR')
    w4.place(x=750,y=60)
    b3.config(text="PROCEED",font=('Franklin Gothic Medium',13),fg='black',bg='light gray',command=lambda:pro1(l9,l10,l11,l12,l13,l14,v4,'year','0',0,OPTIONS4))
    b3.place(x=870,y=53)
mainloop()
