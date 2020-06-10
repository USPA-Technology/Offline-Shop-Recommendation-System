import sqlite3
import math
l2=[]
conn=sqlite3.connect("shop.db")
c3=conn.execute("select monetary from recency")
for i in c3:
    l2.append(i[0])

for i in range(0,len(l2)):
    if((l2[i]<=340)&(l2[i]>0)):
        conn.execute("UPDATE rank SET m=? WHERE rowid=?",[(1),(i+1)]);
    if((l2[i]<=470)&(l2[i]>340)):
        conn.execute("UPDATE rank SET m=? WHERE rowid=?",[(2),(i+1)]);
    if((l2[i]<=600)&(l2[i]>470)):
        conn.execute("UPDATE rank SET m=? WHERE rowid=?",[(3),(i+1)]);
    if((l2[i]<=730)&(l2[i]>600)):
        conn.execute("UPDATE rank SET m=? WHERE rowid=?",[(4),(i+1)]);
    if((l2[i]>730)):
        conn.execute("UPDATE rank SET m=? WHERE rowid=?",[(5),(i+1)]);
conn.commit()


l1=[]
conn=sqlite3.connect("shop.db")
c3=conn.execute("select recency1 from recency")
for i in c3:
    l1.append(i[0])
l1.sort()
r1=[]
for i in range(0,len(l1)):
    c3=conn.execute("select rowid from recency where recency1=?",[(l1[i])])
    for i in c3:
        r1.append(i[0])  
r1=list(dict.fromkeys(r1))
z=len(r1)/5

for i in range(0,len(r1)):
    if(i<z):
        conn.execute("UPDATE rank SET r=? WHERE rowid=?",[(5),(r1[i])]);
    if((i<z+150)&(i>=z)):
        conn.execute("UPDATE rank SET r=? WHERE rowid=?",[(4),(r1[i])]);
    if((i<z+250)&(i>=z+150)):
        conn.execute("UPDATE rank SET r=? WHERE rowid=?",[(3),(r1[i])]);
    if((i<z+350)&(i>=z+250)):
        conn.execute("UPDATE rank SET r=? WHERE rowid=?",[(2),(r1[i])]);
    if(i>=z+350):
        conn.execute("UPDATE rank SET r=? WHERE rowid=?",[(1),(r1[i])]);
conn.commit()

l4=[]
l3=[]
l5=[]
    
conn=sqlite3.connect("shop.db")
c3=conn.execute("select recency1 from recency")
for i in c3:
    l5.append(i[0])
c3=conn.execute("select frequency from recency")
for i in c3:
    l4.append(i[0])
#print(max(l4))
c3=conn.execute("select f from rank")
for i in c3:
    l3.append(i[0])
for i in range(0,len(l4)):
    if(l3[i]==3):
        if(l5[i]>120):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(2),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and ((l5[i]>30) and (l5[i]<=60))):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and (l5[i]<30)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(5),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);            
        elif(((l4[i]<=180)&(l4[i]>90)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(2),(i+1)]);
        elif(((l4[i]<=180)&(l4[i]>90)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(l4[i]>180):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);

    if(l3[i]==2):
        if(l5[i]>180):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]>120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]<120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]>120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]<120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);            
        elif(((l4[i]<=180)&(l4[i]>90)) and (l5[i]>120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(2),(i+1)]);
        elif(((l4[i]<=180)&(l4[i]>90)) and (l5[i]<120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=365)&(l4[i]>180)) and (l5[i]>120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);
        elif(((l4[i]<=365)&(l4[i]>180)) and (l5[i]<120)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(2),(i+1)]);
        elif(l4[i]>365):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);
  

    if(l3[i]==1):
        if(((l4[i]<=90)&(l4[i]>60)) and (l5[i]>180)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]<180)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);            
        elif(((l4[i]<=180)&(l4[i]>90)) and (l5[i]>180)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(2),(i+1)]);
        elif(((l4[i]<=180)&(l4[i]>90)) and (l5[i]<180)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=365)&(l4[i]>180)) and (l5[i]>180)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);
        elif(((l4[i]<=365)&(l4[i]>180)) and (l5[i]<180)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(2),(i+1)]);
        elif(l4[i]>365):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);


    if(l3[i]==4):
        if((l5[i]>90)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);   
        elif(((l4[i]<=30)&(l4[i]>0)) and ((l5[i]>30) and (l5[i]<=60))):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(5),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and (l5[i]<30)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(5),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);            
        elif(l4[i]>90):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);


    if(l3[i]==5):
        if((l5[i]>90)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and ((l5[i]>30) and (l5[i]<=60))):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(5),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and (l5[i]<30)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(5),(i+1)]);
        elif(((l4[i]<=30)&(l4[i]>0)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);
        elif(((l4[i]<=60)&(l4[i]>30)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(5),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]>60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(3),(i+1)]);
        elif(((l4[i]<=90)&(l4[i]>60)) and (l5[i]<60)):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(4),(i+1)]);            
        elif(l4[i]>90):
            conn.execute("UPDATE rank SET f=? WHERE rowid=?",[(1),(i+1)]);
        
        
conn.commit()
conn=sqlite3.connect("shop.db")
c1=conn.execute("select * from rank")
ids111=1

for i in c1:
    s111=(i[2]+i[1])/2
    conn.execute("UPDATE rank SET avg=? WHERE rowid=?",[(math.ceil(s111)),(ids111)]);
    ids111=ids111+1
conn.commit()







