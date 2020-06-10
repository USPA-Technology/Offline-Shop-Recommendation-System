import os
from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("ADMIN")
root.geometry("1360x765")
root.resizable(0,0)
photo1=PhotoImage(file='u3.png')
bk_img=Label(root,image=photo1)
bk_img.place(x=0,y=0,relwidth=1,relheight=1)
photo2=PhotoImage(file='utsav2.png')
bk_img=Label(root,image=photo2)
bk_img.place(x=542,y=50)
def av():
     root.destroy()
     os.system("python addvendor.py")

def us():
    root.destroy()
    os.system("python updatestock.py")

def vr():
    root.destroy()
    os.system("python vendor_report.py")

def sr():
    root.destroy()
    os.system("python sales_report.py")

def str2():
    root.destroy()
    os.system("python cosine.py")

def home():
    root.destroy()
    os.system("python home.py")
b1=Button(root,text="ADD VENDOR",font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="red",command=av)
b1.place(x=322,y=240)

b2=Button(root,text='UPDATE STOCK',font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="orange",command=lambda:us())
b2.place(x=780,y=240)

b3=Button(root,text="VENDOR REPORT",font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="turquoise1",command=vr)
b3.place(x=300,y=370)

b4=Button(root,text="SALES REPORT",font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="magenta3",command=sr)
b4.place(x=780,y=370)

b5=Button(root,text="RECLUSTERING",font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="GREEN4",command=str2)
b5.place(x=550,y=500)

b6=Button(root,text="HOME",font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="gray4",command=home)
b6.place(x=600,y=310)

##b7=Button(root,text="OFFER",font=('Franklin Gothic Medium',20,'bold'),bg="snow",fg="gray4",command=home)
##b7.place(x=600,y=600)
root.mainloop()
