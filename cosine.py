import os
import sqlite3
from random import seed
from random import randint
import pandas as pd
import numpy as np
import csv
import math
from tkinter import *
import time
import datetime
root=Tk()


def slice(entry):
    v=entry[2:]
    f=v[:-3]
def kmea():
    list3 = []
    with open('sbh.csv', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            list3.append(row)   
    data=[]
    data.append(list3[0])
    conn=sqlite3.connect("shop.db")
    c3=conn.execute("SELECT * FROM kmeans ")
    for k in c3:
        data.append(k)
    m = data
    with open('sbh1.csv', 'w', newline='') as my:
        writer = csv.writer(my)
        writer.writerows(m)



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
        zip(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24,
            f25, f26, f27, f28, f29, f30)))
    from sklearn.cluster import KMeans

    q = list22[0]
    conn = sqlite3.connect("shop.db")
    c3 = conn.execute("update clusterlength set value=? WHERE rowid=?", [(q),(1)])
    conn.commit()
    print(q)
    kmeans = KMeans(n_clusters=q)
    kmeans.fit(X)
    #print(kmeans.cluster_centers_)
    #print(kmeans.labels_)
    conn = sqlite3.connect("shop.db")
    for j in range(0,len(kmeans.labels_)):
        inte=int(kmeans.labels_[j])
        c3 = conn.execute("update clusterinfo set clusterno=? WHERE rowid=?", [(inte),(j+1)])
    conn.commit()
    
    conn = sqlite3.connect("shop.db")
    c1=conn.execute("select count(*) from customer_details")
    for i in c1:
        uniquser=i[0]
    c2=conn.execute("select * from clusterlength")
    for i in c2:
        clusterl=i[0]

        
    l2=[]
    for j in range(0,clusterl):
        data = []
        l=[]
        for i in range(0,uniquser):
            if (j == kmeans.labels_[i]):
                c3 = conn.execute("SELECT * FROM kmeans WHERE u=?", [i])
                for k in c3:
                    data.append(k)
        for y in range(1,31):
            m=0
            for x in range(0,len(data)):
                m=m+data[x][y]
            l.append(m)
        l2.append(l)
    n=l2
    with open('cosine.csv', 'w', newline='') as my2:
        writer = csv.writer(my2)
        writer.writerows(n)
###################################################################

conn=sqlite3.connect("shop.db")
c3=conn.execute("SELECT value from clusterlength")
list22=[]
for j in c3:
    list22.append(j[0])
z111=[]
##localtime=time.asctime(time.localtime(time.time()))
##today=datetime.date.today()
##today=str(today)
##d2=today[8:10]
##m2=today[5:7]
##y2=today[0:4]
##xx=str(d2)+'/'+str(m2)+'/'+str(y2)
conn=sqlite3.connect("shop.db")
c3=conn.execute("SELECT particular3,brand3,id,quantity3 FROM sales_report  WHERE date=?",["04/11/2017"])
for j in c3:
    z111.append(j)
for i1111 in range(0,len(z111)):
    
        
    z=[]
    conn=sqlite3.connect("shop.db")
    c3=conn.execute("SELECT code FROM typebrand  WHERE (particular=? and brand=?)",[(str(z111[i1111][0])),(str(z111[i1111][1]))])
    for j in c3:
        z.append(j)
    l1=[]
    if((z[0][0]==110001)|(z[0][0]==110003)|(z[0][0]==317001)|(z[0][0]==317003)|(z[0][0]==319001)|(z[0][0]==319003)):
        l1.append(z[0][0])
        r1=0
    else:
        l1.append(z[0][0])
        m1=z[0][0]+200000
        l1.append(m1)
        r1=randint(0,1)
    data=[]
    c3=conn.execute("SELECT a"+str(l1[r1])+" FROM kmeans WHERE u=?",[z111[i1111][2]])
    for k in c3:
        data.append(k)

    conn.execute("UPDATE kmeans SET a"+str(l1[r1])+"="+str(z111[i1111][3]+data[0][0])+" WHERE u=?",[z111[i1111][2]])
    conn.commit()
    conn=sqlite3.connect("shop.db")
    conn.execute("UPDATE recency SET recency1=0 WHERE rowid=?",[z111[i1111][2]+1])
    conn.commit()
    da=[]
    conn=sqlite3.connect("shop.db")
    c3=conn.execute("SELECT * FROM kmeans WHERE u=?",[z111[i1111][2]])
    for k in c3:
        da.append(k)

        
    l=[]
    va=[]
    k=[]
    with open('cosine.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        l.append(row)

    ll=da[0][0:31]

    asq=0
    bsq=0
    for j in range(0,30):
      v=int(ll[j])
      asq=asq+(v*v)
      va.append(v)
    a=sum(va)
    diva=math.sqrt(asq/(a*a))
    mm=0
    for i in range(0,len(l)):
        vb=[]
        bsq=0
        c=l[i]
        val=0
        for j in range(0,30):
          v=int(c[j])
          bsq=bsq+(v*v)
          vb.append(v)
        b=sum(vb)
        for j in range(0,30):
          val=val+((va[j]/a)*(vb[j]/b))
        divb=math.sqrt(bsq/(b*b))
        div=diva * divb
        si=val/div
        k.append(si)
        if(si>0.2):
            mm=mm+1
            
    print(max(k))
    if(mm==0):
        mm1=list22[0]
        list22.clear()
        list22.append(mm1+1)
    kmea()

mainloop()
