import sqlite3
import time
import datetime
import math
conn=sqlite3.connect("shop.db")

a=[]
f=[]
for i in range(0,500):
	my_dates=[]
	c4=conn.execute("SELECT date FROM sales_report WHERE id=?",[(i)]);
	for j in c4:
		my_dates.append(str(j))

	l=[]
	for i in range(0,len(my_dates)):
		l.append(str(my_dates[i][2:12]))
	dates = [datetime.datetime.strptime(ts, "%d/%m/%Y") for ts in l]
	dates.sort()
	sorteddates = [datetime.datetime.strftime(ts, "%d/%m/%Y") for ts in dates]
	if(len(sorteddates)>1):
		str1=sorteddates[0]
		dates1 = datetime.datetime.strptime(str1, "%d/%m/%Y").date()

		str2=sorteddates[len(sorteddates)-1]
		dates2 = datetime.datetime.strptime(str2, "%d/%m/%Y").date()
		delta = dates2-dates1
		d=str(delta)
		a=d.split()
		fr=math.ceil(int(a[0])/(len(sorteddates)-1))
		f.append(fr)
	else:
		if(len(sorteddates)==1):
			f.append(2000)
		
print(f)

for j in range(0,len(f)):
   	conn.execute("UPDATE recency SET frequency=? WHERE rowid=?",[(f[j]),(j+1)]);
conn.commit()



conn=sqlite3.connect("shop.db")
str1="01/01/2020"
dates1 = datetime.datetime.strptime(str1, '%d/%m/%Y').date()

date=[]
a=[]
for i in range(0,500):
	my_dates=[]
	c4=conn.execute("SELECT date FROM sales_report WHERE id=?",[(i)]);
	for j in c4:
		my_dates.append(str(j))

	l=[]
	for i in range(0,len(my_dates)):
		l.append(str(my_dates[i][2:12]))
	dates = [datetime.datetime.strptime(ts, "%d/%m/%Y") for ts in l]
	dates.sort()
	sorteddates = [datetime.datetime.strftime(ts, "%d/%m/%Y") for ts in dates]
	str2=sorteddates[len(sorteddates)-1]
	dates2 = datetime.datetime.strptime(str2, "%d/%m/%Y").date()
	delta = dates1-dates2
	d=str(delta)
	a=d.split()
	date.append(a[0])
	
print(date)

for j in range(0,len(date)):
   	conn.execute("UPDATE recency SET recency1=? WHERE rowid=?",[(date[j]),(j+1)]);
conn.commit()	



##for j in range(0,len(date)):
##        conn.execute("INSERT INTO recency VALUES (?,?)",[(date[j]),(0)]);
##conn.commit()

m=[]
for i in range(0,500):
        z=[]
        a=0
        conn=sqlite3.connect("shop.db")
        c4=conn.execute("SELECT date FROM sales_report WHERE id=?",[(i)]);
        for j in c4:
                z.append(j[0])
        z=list(dict.fromkeys(z))
        conn=sqlite3.connect("shop.db")
        c4=conn.execute("SELECT quantity3,price3 FROM sales_report WHERE id=?",[(i)]);
        for j in c4:
                a=a+j[0]*j[1]
        m.append(math.floor(a/len(z)))

print(m)
for j in range(1,len(m)+1):
   	conn.execute("UPDATE recency SET monetary=? WHERE rowid=?",[(m[j-1]),(j)]);
conn.commit()
		










