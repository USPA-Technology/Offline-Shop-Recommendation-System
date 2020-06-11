import os
import sqlite3
import time
import datetime
import pandas as pd
import numpy as np
from random import seed
from random import randint
from apyori import apriori


# import urllib.request
# import urllib.parse


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
    conn = sqlite3.connect("E:\BE project\Shop\shop.db")
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


def g(v1):
    ##  kmeans = KMeans(n_clusters=q)
    ##  kmeans.fit(X)
    # print(kmeans.cluster_centers_)
    # print(kmeans.labels_)
    d2222 = []
    conn = sqlite3.connect("E:\BE project\Shop\shop.db")
    c3 = conn.execute("SELECT clusterno FROM clusterinfo")
    for i in c3:
        d2222.append(str(i))
    km = []
    for j in range(0, len(d2222)):
        km.append(int(d2222[j][1:-2]))
    ##    print(km)
    conn.commit()

    import csv
    v1 = int(v1)
    v2 = km[v1]
    conn = sqlite3.connect("E:\BE project\Shop\shop.db")
    data = []
    for j in range(v2, v2 + 1):
        for i in range(0, 999):
            if (j == km[i]):
                c3 = conn.execute("SELECT * FROM kmeans WHERE u=?", [i])
                for k in c3:
                    data.append(k)
    list1 = []
    list3 = []
    with open('E:\BE project\Shop\sbh1.csv', newline='') as c:
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
    with open('E:\BE project\Shop\d22.csv', 'w', newline='') as my:
        writer = csv.writer(my)
        writer.writerows(m)

    list5 = []
    with open('E:\BE project\Shop\d22.csv', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            list5.append(row)

    association_rules = apriori(list5, min_support=0.5, min_confidence=0.7)
    association_results = list(association_rules)
    #print(len(association_results))
    #print(association_results)

    data2 = []
    c5 = conn.execute("SELECT * FROM kmeans WHERE u=?", [v1])
    for k in c5:
        data2.append(k)
    p1 = []
    p2 = []
    for item in association_results:
        for i in range(0, len(item[2])):
            b1 = str(item[2][i][0])[11:-2]
            b2 = str(item[2][i][1])[11:-2]
            print("Rule: " + b1 + " -> " + b2)
            if ((len(b1) == 8) & (len(b2) == 8)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if (b1[1:-1] == list3[0][i2]):
                        if (data2[0][i2] > 0):
                            x = x + 1
                            break
                for i2 in range(1, 31):
                    if (b2[1:-1] == list3[0][i2]):
                        if (data2[0][i2] > 0):
                            y = y + 1
                            break
                if ((x > 0) & (y == 0)):
                    p1.append(b2)
                    print(b2)
            if ((len(b1) == 18) & (len(b2) == 8)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if ((b1[1:8] == list3[0][i2]) | (b1[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            x = x + 1
                for i2 in range(1, 31):
                    if (b2[1:-1] == list3[0][i2]):
                        if (data2[0][i2] > 0):
                            y = y + 1
                            break
                if ((x == 2) & (y == 0)):
                    p1.append(b2)
                    print(b2)
            if ((len(b1) == 8) & (len(b2) == 18)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if ((b2[1:8] == list3[0][i2]) | (b2[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            x = x + 1
                for i2 in range(1, 31):
                    if (b1[1:-1] == list3[0][i2]):
                        if (data2[0][i2] > 0):
                            y = y + 1
                            break
                if ((x == 0) & (y == 1)):
                    p1.append(b2[0:8])
                    p1.append(b2[10:])
                    print(b2[10:])
            if ((len(b1) == 18) & (len(b2) == 18)):
                x = 0
                y = 0
                for i2 in range(1, 31):
                    if ((b1[1:8] == list3[0][i2]) | (b1[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            x = x + 1
                    if ((b2[1:8] == list3[0][i2]) | (b2[11:-1] == list3[0][i2])):
                        if (data2[0][i2] > 0):
                            y = y + 1
                if ((x == 2) & (y == 0)):
                    p1.append(b2[0:8])
                    p1.append(b2[10:])
                    print(b2)
            if ((len(b1) == 0) & (len(b2) == 8)):
                for i2 in range(1, 31):
                    if (b2[1:-1] == list3[0][i2]):
                        p2.append(b2)
                        print(b2)

    p1 = list(dict.fromkeys(p1))
    p2 = list(dict.fromkeys(p2))



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
    print(o)
    print(o1)
    conn = sqlite3.connect("E:\BE project\Shop\shop.db")
    if (o == ''):
        o = "Null"
    if (o1 == ''):
        o1 = "Null"
    c3 = conn.execute("select phone_no1 from customer_details where cname=?", [v1])
    for k in c3:
        t2 = str(k[0])
    localtime = time.asctime(time.localtime(time.time()))
    today = datetime.date.today()

    today = str(today)
    d2 = today[8:10]
    m2 = today[5:7]
    y2 = today[0:4]
    today = d2 + "/" + m2 + "/" + y2

    conn.execute("INSERT INTO messinfo VALUES(?,?,?,?)", [(t2), (o), (o1), (today)]);
    conn.commit()
    #c3=conn.execute("select phone_no1 from customer_details where cname=?", [v1])
    #for k in c3:
    #    t2=str(k[0])  
    #    sendSMS(o,o1,t2)

x11 = []

localtime = time.asctime(time.localtime(time.time()))
today = datetime.date.today()

today = str(today)
d2 = today[8:10]
m2 = today[5:7]
y2 = today[0:4]

l = []
ids2 = 0
conn = sqlite3.connect("E:\BE project\Shop\shop.db")
c3 = conn.execute("select date from sales_report")
for i in c3:
    t3 = str(i[0])
    d31 = t3[0:2]
    d3 = int(d31)
    m3 = t3[3:5]
    y31 = t3[6:10]
    y3 = int(y31)
    if (str(d2) == "01"):
        if ((m3 == m2) & (d3 > 0) & (d3 < 8) & ((int(y2) - y3) > 0) & ((int(y2) - y3) < 2)):
            print(t3)
            l.append(ids2)
    if (str(d2) == "08"):
        if ((m3 == m2) & (d3 > 7) & (d3 < 15) & ((int(y2) - y3) > 0) & ((int(y2) - y3) < 2)):
            print(t3)
            l.append(ids2)
    if (str(d2) == "15"):
        if ((m3 == m2) & (d3 > 14) & (d3 < 22) & ((int(y2) - y3) > 0) & ((int(y2) - y3) < 2)):
            print(t3)
            l.append(ids2)
    if (str(d2) == "22"):
        if ((m3 == m2) & (d3 > 21) & (d3 < 32) & ((int(y2) - y3) > 0) & ((int(y2) - y3) < 2)):
            print(t3)
            l.append(ids2)
    ids2 = ids2 + 1

ids1 = 0
conn = sqlite3.connect("E:\BE project\Shop\shop.db")
c2 = conn.execute("select dob from customer_details")
for i in c2:
    t1 = str(i[0])
    d1 = t1[0:2]
    m1 = t1[3:5]
    if ((m1 == m2) & (d1 == d2)):
        l.append(ids1)
        #c3=conn.execute("select phone_no1 from customer_details where cname=?",[ids1])
        #for k in c3:
        #    t2=str(k[0])  
        #    sendSMSDOB(t2)
    ids1 = ids1 + 1

rec = []
avgr = []

c1 = conn.execute("select recency1 from recency")
c2 = conn.execute("select avg from rank")

for i in c1:
    rec.append(i[0])
for j in c2:
    avgr.append(j[0])

for i in range(0, len(rec)):
    if (rec[i] == 15 and avgr[i] == 5):
        l.append(i)
    if (rec[i] == 30 and avgr[i] == 4):
        l.append(i)
    if (rec[i] == 45 and avgr[i] == 5):
        l.append(i)
    if (rec[i] == 60 and avgr[i] == 3):
        l.append(i)
    if (rec[i] == 60 and avgr[i] == 4):
        l.append(i)
    if (rec[i] == 90 and avgr[i] == 2):
        l.append(i)
    if (rec[i] == 120 and avgr[i] == 1):
        l.append(i)

l = list(dict.fromkeys(l))
print(l)
for i in range(0, len(l)):
    g(l[i])

conn.commit()

#def sendSMS(product1,product2,numbers):
#    message="You may also like"+product1+" and "+product2
#    apikey='apikey'
#    sender='senderkey'

#    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
#        'message' : message, 'sender': sender})
#    data = data.encode('utf-8')
#    request = urllib.request.Request("https://api.textlocal.in/send/?")
#    f = urllib.request.urlopen(request, data)
#    fr = f.read()
#    print(fr)

#def sendSMSDOB(numbers):
#    message="Wish you a very beautiful and prosperous Happy Birthday." 
#    apikey='apikey'
#    sender='senderkey'

#    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
#        'message' : message, 'sender': sender})
#    data = data.encode('utf-8')
#    request = urllib.request.Request("https://api.textlocal.in/send/?")
#    f = urllib.request.urlopen(request, data)
#    fr = f.read()
#    print(fr)
