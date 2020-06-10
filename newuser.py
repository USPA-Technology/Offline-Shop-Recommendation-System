import os
import sqlite3
import time
import datetime
import pandas as pd
import numpy as np
from random import seed
from random import randint
from apyori import apriori
import csv


def slice(entry):
    v = entry[2:]
    f = v[:-3]
    return f


def slice1(entry):
    v = entry[1:]
    f = v[:-2]
    return f


def slice2(entry):
    v = entry[5:]
    f = v[:-3]
    return f


def slice3(entry):
    f = entry[:-6]
    return f


def slice4(entry):
    f = entry[8:]
    return f


def refres(c):
    conn = sqlite3.connect("shop.db")
    x11.clear()
    # x11=[]
    x = []
    if (c == "110001"):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["ethical"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("fabindia")
        d2.append("biba")

        r2 = randint(0, len(d2) - 1)
        x.append("ethical")
        x.append(d1[r1])
        x.append(d2[r2])
    if (c == "110003"):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["ethical"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("melange")
        d2.append("shree")
        r2 = randint(0, len(d2) - 1)
        x.append("ethical")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131111") | (c == "331111")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["tshirt"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("nike")
        d2.append("adidas")
        r2 = randint(0, len(d2) - 1)
        x.append("tshirt")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131113") | (c == "331113")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["tshirt"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("tommy")
        d2.append("lacoste")
        d2.append("gucci")
        r2 = randint(0, len(d2) - 1)
        x.append("tshirt")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131131") | (c == "331131")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["shirt"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("nike")
        d2.append("adidas")
        r2 = randint(0, len(d2) - 1)
        x.append("shirt")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131133") | (c == "331133")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["shirt"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("tommy")
        d2.append("lacoste")
        d2.append("gucci")
        r2 = randint(0, len(d2) - 1)
        x.append("shirt")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131371") | (c == "331371")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["sum"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("jockey")

        r2 = randint(0, len(d2) - 1)
        x.append("sum")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131373") | (c == "331373")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["sum"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("domyos")
        r2 = randint(0, len(d2) - 1)
        x.append("sum")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131391") | (c == "331391")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["winter"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("raymonds")
        d2.append("peter_eng")
        r2 = randint(0, len(d2) - 1)
        x.append("winter")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "131393") | (c == "331393")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["winter"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("montecarlo")

        r2 = randint(0, len(d2) - 1)
        x.append("winter")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "133701") | (c == "333701")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["jeans"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("pepe")
        d2.append("levis")
        d2.append("wrangler")
        r2 = randint(0, len(d2) - 1)
        x.append("jeans")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "133703") | (c == "333703")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["jeans"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("lee")
        d2.append("diesel")

        r2 = randint(0, len(d2) - 1)
        x.append("jeans")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "133901") | (c == "333901")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["trousers"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("jcrew")
        d2.append("lestrange")

        r2 = randint(0, len(d2) - 1)
        x.append("trousers")
        x.append(d1[r1])
        x.append(d2[r2])
    if ((c == "133903") | (c == "333903")):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["trousers"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("rhone")

        r2 = randint(0, len(d2) - 1)
        x.append("trousers")
        x.append(d1[r1])
        x.append(d2[r2])
    if (c == "317001"):
        d1 = []

        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["kurtas"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("fabindia")
        d2.append("aurelia")

        r2 = randint(0, len(d2) - 1)
        x.append("kurtas")
        x.append(d1[r1])
        x.append(d2[r2])
    if (c == "317003"):
        d1 = []
        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["kurtas"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("biba")
        d2.append("libas")
        r2 = randint(0, len(d2) - 1)
        x.append("kurtas")
        x.append(d1[r1])
        x.append(d2[r2])
    if (c == "319001"):
        d1 = []
        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["sarees"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("satyapaul")
        d2.append("sabyasachi")

        r2 = randint(0, len(d2) - 1)
        x.append("sarees")
        x.append(d1[r1])
        x.append(d2[r2])
    if (c == "319003"):
        d1 = []
        c3 = conn.execute("SELECT distinct(type) FROM typebrand WHERE particular=?", ["sarees"])
        for k in c3:
            d1.append(slice(str(k)))
        r1 = randint(0, len(d1) - 1)
        d2 = []
        d2.append("ritu")
        d2.append("tarun")
        r2 = randint(0, len(d2) - 1)
        x.append("sarees")
        x.append(d1[r1])
        x.append(d2[r2])
    for i in range(0, len(x)):
        x11.append(x[i])
    # print("hii")
    print(x11)


def g():
    import csv
    conn = sqlite3.connect("shop.db")
    c1=conn.execute("select count(*) from customer_details")
    for i in c1:
        uniquser=i[0]
    data = []
    for j in range(0, len(s)):
        for i in range(0,uniquser):
            if (i == s[j]):
                c3 = conn.execute("SELECT * FROM kmeans WHERE u=?", [i])
                for k in c3:
                    data.append(k)
    # print(data)
    list1 = []
    list3 = []
    with open('sbh.csv') as c:
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
    # print(len(association_results))
    print(association_results)
    ##    data2=[]
    ##    for k in range(0,len(s)):
    ##        data2.append(s[k])

    p1 = []
    p2 = []
    for item in association_results:
        for i in range(0, len(item[2])):
            b1 = str(item[2][i][0])[11:-2]
            b2 = str(item[2][i][1])[11:-2]
            print("Rule: " + b1 + " -> " + b2)
            if ((len(b1) == 8) & (len(b2) == 8)):
                p1.append(b2)
            ##                x=0
            ##                y=0
            ##                for i2 in range(1, 31):
            ##                    if(b1[1:-1]==list3[0][i2]):
            ##                        if(data2[0][i2]>0):
            ##                            x=x+1
            ##                            break
            ##                for i2 in range(1, 31):
            ##                    if(b2[1:-1]==list3[0][i2]):
            ##                        if(data2[0][i2]>0):
            ##                            y=y+1
            ##                            break
            ##                if((x>0)&(y==0)):
            ##                    p1.append(b2)
            ##                    #print(b2)
            if ((len(b1) == 18) & (len(b2) == 8)):
                p1.append(b2)
            ##                x = 0
            ##                y = 0
            ##                for i2 in range(1, 31):
            ##                    if ((b1[1:8] == list3[0][i2])|(b1[11:-1] == list3[0][i2])):
            ##                        if (data2[0][i2] > 0):
            ##                            x = x + 1
            ##                for i2 in range(1, 31):
            ##                    if (b2[1:-1] == list3[0][i2]):
            ##                        if (data2[0][i2] > 0):
            ##                            y = y + 1
            ##                            break
            ##                if ((x==2) & (y == 0)):
            ##                    p1.append(b2)
            ##                    #print(b2)
            if ((len(b1) == 8) & (len(b2) == 18)):
                p1.append(b2[0:8])
                p1.append(b2[10:])
            ##                x = 0
            ##                y = 0
            ##                for i2 in range(1, 31):
            ##                    if ((b2[1:8] == list3[0][i2])|(b2[11:-1] == list3[0][i2])):
            ##                        if (data2[0][i2] > 0):
            ##                            x = x + 1
            ##                for i2 in range(1, 31):
            ##                    if (b1[1:-1] == list3[0][i2]):
            ##                        if (data2[0][i2] > 0):
            ##                            y = y + 1
            ##                            break
            ##                if ((x==0) & (y == 1)):
            ##                    p1.append(b2[0:8])
            ##                    p1.append(b2[10:])
            ##                    #print(b2[10:])
            if ((len(b1) == 18) & (len(b2) == 18)):
                p1.append(b2[0:8])
                p1.append(b2[10:])
            ##                x = 0
            ##                y = 0
            ##                for i2 in range(1, 31):
            ##                    if ((b1[1:8] == list3[0][i2])|(b1[11:-1] == list3[0][i2])):
            ##                        if (data2[0][i2] > 0):
            ##                            x = x + 1
            ##                    if ((b2[1:8] == list3[0][i2])|(b2[11:-1] == list3[0][i2])):
            ##                        if (data2[0][i2] > 0):
            ##                            y = y + 1
            ##                if ((x==2) & (y == 0)):
            ##                    p1.append(b2[0:8])
            ##                    p1.append(b2[10:])
            ##                    #print(b2)
            if ((len(b1) == 0) & (len(b2) == 8)):
                p2.append(b2)
    ##                for i2 in range(1, 31):
    ##                    if(b2[1:-1]==list3[0][i2]):
    ##                        p2.append(b2)
    ##                        #print(b2)
    ##
    ##
    ##
    ##    p1=list(dict.fromkeys(p1))
    ##    p2=list(dict.fromkeys(p2))

    o = ''
    o1 = ''
    if (len(p1) == 1):
        refres(p1[0][1:-1])
        o = o + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
        refres(p2[-1][1:-1])
        o1 = o1 + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
    elif (len(p1) > 1):
        refres(p1[-2][1:-1])
        o = o + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
        refres(p1[-1][1:-1])
        o1 = o1 + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
    if (len(p1) == 0):
        if (len(p2) == 1):
            refres(p2[0][1:-1])
            o = o + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
        elif (len(p2) > 1):
            refres(p2[-2][1:-1])
            o = o + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
            refres(p2[-1][1:-1])
            o1 = o1 + str(x11[0]) + ' ' + str(x11[1]) + " " + str(x11[2])
    if (o == '' and o1 == ''):
        mains = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        exid = []
        conn = sqlite3.connect("shop.db")
        c1=conn.execute("select count(*) from customer_details")
        for i in c1:
            uniquser=i[0]
        for i in range(0, len(s)):
            for j in range(0,uniquser):
                if (j == s[i]):
                    c1 = conn.execute("select * from kmeans where u=?", [j]);
                    for n in c1:
                        exid.append(n)
                    break
        for i in range(0, len(s)):
            for j in range(0, 30):
                mains[j] = mains[j] + exid[i][j + 1]
        idinfo = []
        with open('sbh.csv') as c:
            reader = csv.reader(c)
            for row in reader:
                idinfo.append(row)
                break
        print(idinfo)
        indexes=[]
        max1 = max(mains)
        if (mains.count(max1) > 1):
            for i in range(0, 30):
                if (mains[i] == max1):
                    indexes.append(i)
            ind1 = indexes(0)
            ind2 = indexes(1)
        else:
            ind1 = mains.index(max1)
            mains.pop(ind1)
            mains.insert(ind1,0)
            max2 = max(mains)
            ind2 = mains.index(max2)
        print(str(ind1) + " " + str(mains[ind1]))
        print(str(ind2) + " " + str(mains[ind2]))
        o = (idinfo[0][ind1 + 1])
        o1 = (idinfo[0][ind2 + 1])
        print(o)
        print(o1)
        refres(o)
        refres(o1)

    #ff=max(set(zz2),key=zz2.count)
    conn.commit()

#take input date here


ynew="2000"
conn=sqlite3.connect("shop.db")
d=[]
c1=conn.execute("select dob from customer_details");
for i in c1:
    d.append(i[0])
print(d[0])

y=[]
for i in range(0,len(d)):
    year=d[i][6:10]
    y.append(year)
print(y[0])
s=[]
k=[]
for i in range(0,len(y)):
    if((y[i]>=str(int(ynew)-2)) and (y[i]<=str(int(ynew)+2))):
        s.append(i)
        k.append(y[i])

print(s)



x11=[]
g()

conn.commit()
