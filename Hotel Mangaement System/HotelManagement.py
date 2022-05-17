import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import time
from tkinter import font
def show_frame(frame):
    frame.tkraise()
root=tk.Tk()
conn = sqlite3.connect('AlBurjHotel.db')
c = conn.cursor()
frame1=tk.Frame(root,bg='#FFD43B')
frame2=tk.Frame(root,bg='#FFD43B')
frame3=tk.Frame(root,bg='#FFD43B')
frame4=tk.Frame(root,bg='#FFD43B')
frame5=tk.Frame(root,bg='#FFD43B')
frame6=tk.Frame(root,bg='#FFD43B')
show_frame(frame1) 
root.geometry(f"{890}x{700}")
root.maxsize(890,640)
root.title("Alburj Hotel LTD")
root.iconbitmap('c:/48.ico')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
for frame in (frame1,frame2,frame3,frame4,frame5,frame6):
    frame.grid(row=0,column=0,sticky='nsew')
def booking():
    show_frame(frame4)
def rooms():
    show_frame(frame5)    
#frame1 login page

can3 =tk.Canvas(frame6, height=2000, width=2000, background='#FFE4C4')
can3.pack()
can4 =tk.Canvas(frame3, height=2000, width=2000, background='#FFE4C4')
can4.pack()
can3.create_text(260,100,text='YOUR TOTAL AMOUNT IS  :',font='comicsansms 26 bold')
def payment():
    show_frame(frame6)
    yoyo =tk.Frame(frame6, bd=10)
    yoyo.place(x=150,y=140,width=350,height=400)
    for item in lbx.curselection():
        payget = lbx.get(item)
        can3.create_text(670,100,text=payget,font = 'comicsansms 30 bold')
        label1 = tk.Label(yoyo, text='*' * 80, font='comicsansms 8 bold')
        label1.pack()
        label2 = tk.Label(yoyo, text='*' * 80, font='comicsansms 8 bold')
        label2.pack()
        label3 = tk.Label(yoyo, text='Atif,Nishan ALBurjHotel Inc.\nALBURJ, DUBAI')
        label3.pack()
        label4 = tk.Label(yoyo, text='=' * 80)
        label4.pack()
        label5 = tk.Label(yoyo, text='YOUR-ROOM')
        label5.place(x=10,y=120)
        label8 = tk.Label(yoyo, text='AMOUNT')
        label8.place(x=230, y=120)
        payget = str(payget)
        label6 = tk.Label(yoyo, text=payget[:7])
        label6.place(x=10,y=150)
        label7 = tk.Label(yoyo, text=payget[8:])
        label7.place(x=200,y=150)
        print(payget)
    paybyt =tk.Button(frame6,text='PAY',fg='green',font='comicsansms 19 bold',borderwidth=6,command=paid)
    paybyt.place(x=400,y=460)
def back2():
    show_frame(frame1)
def back():
    show_frame(frame3) 
def sign():
    c.execute("SELECT * FROM ALBURJROOMS")
    l=c.fetchall()
    i=0
    a=[]
    for i in range(len(l)):
        for j in range(2):
           a.append(l[i][j])
    for i in range(len(a)):
     if i%2==0:   
        x=a[i]     
     else:
        y=a[i]
        if var7.get()==x:
          if var8.get()==y:
            show_frame(frame3)
          else:
           messagebox.showerror("Error","Check username or password")       
    def room1():
            r1info = tk.Label(frame5,text='ROOM-1',font='comicsansms 15 bold',bg='blue',fg='white')
            r1info.place(x=570,y=55)

            r1bed = tk.Label(frame5,text='Total Bed(s)',font='comicsansms 12 bold',bg='blue',fg='white')
            r1bed.place(x=100,y=100)
            l1 = tk.Label(frame5,text='5',font='comicsansms 20 bold',fg='#00008B')
            l1.place(x=130,y=140)

            r1ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r1ac.place(x=300, y=100)
            l2 = tk.Label(frame5,text='YES',font='comicsansms 20 bold',fg='#00008B')
            l2.place(x=330,y=140)

            r1tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r1tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r1wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r1wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r1price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r1price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$100000', font='comicsansms 20 bold', fg='#00008B')
            l5.place(x=960, y=140)

            r1re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r1re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room2():
            r2info = tk.Label(frame5, text='ROOM-2', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r2info.place(x=570, y=55)

            r2bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r2bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='4', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r2ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r2ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r2tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r2tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r2wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r2wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r2price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r2price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$90000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r2re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r2re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room3():
            r3info = tk.Label(frame5, text='ROOM-3', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r3info.place(x=570, y=55)

            r3bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r3bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='5', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r3ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r3ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r3tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r3tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r3wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r3wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r3price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r3price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$80000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r3re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r3re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold',fg='#00008B')
            l6.place(x=1130, y=140)
    def room4():
            r4info = tk.Label(frame5, text='ROOM-4', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r4info.place(x=570, y=55)

            r4bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r4bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='4', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r4ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r4ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r4tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r4tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r4wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r4wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r4price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r4price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$70000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r4re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r4re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room5():
            r5info = tk.Label(frame5, text='ROOM-5', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r5info.place(x=570, y=55)

            r5bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r5bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='4', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r5ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r5ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r5tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r5tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r5wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r5wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r5price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r5price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$60000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r5re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r5re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room6():
            r6info = tk.Label(frame5, text='ROOM-6', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r6info.place(x=570, y=55)

            r6bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r6bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='3', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r6ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r6ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r6tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r6tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r6wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r6wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r6price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r6price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$50000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r6re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r6re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room7():
            r7info = tk.Label(frame5, text='ROOM-7', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r7info.place(x=570, y=55)

            r7bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r7bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='2', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r7ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r7ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r7tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r7tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r7wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r7wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r7price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r7price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$40000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r7re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r7re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room8():
            r8info = tk.Label(frame5, text='ROOM-8', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r8info.place(x=570, y=55)

            r8bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r8bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='2', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r8ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r8ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r8tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r8tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r8wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r8wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r8price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
            r8price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$30000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=962, y=140)

            r8re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r8re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room9():
            r9info = tk.Label(frame5, text='ROOM-9', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r9info.place(x=570, y=55)

            r9bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r9bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='1', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r9ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r9ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)

            r9tv = tk.Label(frame5, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r9tv.place(x=500, y=100)
            l3 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l3.place(x=530, y=140)

            r9wifi = tk.Label(frame5, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
            r9wifi.place(x=750, y=100)
            l4 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l4.place(x=750, y=140)

            r9price = tk.Label(frame5, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white',padx=10)
            r9price.place(x=960, y=100)
            l5 = tk.Label(frame5, text='$7000', font='comicsansms 20 bold', fg='#00008B',padx=10)
            l5.place(x=970, y=140)

            r9re = tk.Label(frame5, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
            r9re.place(x=1100, y=100)
            l6 = tk.Label(frame5, text='NO', font='comicsansms 20 bold', fg='#00008B')
            l6.place(x=1130, y=140)
    def room10():
            r10info = tk.Label(frame5, text='ROOM-10', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
            r10info.place(x=565, y=55)

            r10bed = tk.Label(frame5, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
            r10bed.place(x=100, y=100)
            l1 = tk.Label(frame5, text='1', font='comicsansms 20 bold', fg='#00008B')
            l1.place(x=130, y=140)

            r10ac = tk.Label(frame5, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
            r10ac.place(x=300, y=100)
            l2 = tk.Label(frame5, text='YES', font='comicsansms 20 bold', fg='#00008B')
            l2.place(x=330, y=140)
            
    R1 = tk.Button(frame5, text='ROOM-1', font='comicsansms 10 bold', borderwidth=4,command=room1)
    R1.place(x=10, y=70)
    R2 = tk.Button(frame5, text='ROOM-2', font='comicsansms 10 bold', borderwidth=4,command=room2)
    R2.place(x=10, y=110)
    R3 = tk.Button(frame5, text='ROOM-3', font='comicsansms 10 bold', borderwidth=4,command=room3)
    R3.place(x=10, y=150)
    R4 = tk.Button(frame5, text='ROOM-4', font='comicsansms 10 bold', borderwidth=4,command=room4)
    R4.place(x=10, y=190)
    R5 = tk.Button(frame5, text='ROOM-5', font='comicsansms 10 bold', borderwidth=4,command=room5)
    R5.place(x=10, y=230)
    R6 = tk.Button(frame5, text='ROOM-6', font='comicsansms 10 bold', borderwidth=4,command=room6)
    R6.place(x=10, y=270)
    R7 = tk.Button(frame5, text='ROOM-7', font='comicsansms 10 bold', borderwidth=4,command=room7)
    R7.place(x=10, y=310)
    R8 = tk.Button(frame5, text='ROOM-8', font='comicsansms 10 bold', borderwidth=4,command=room8)
    R8.place(x=10, y=350)
    R9 = tk.Button(frame5, text='ROOM-9', font='comicsansms 10 bold', borderwidth=4,command=room9)
    R9.place(x=10, y=390)
    R10 = tk.Button(frame5, text='ROOM-10', font='comicsansms 10 bold', borderwidth=4,command=room10)
    R10.place(x=10, y=430)
    R11 = tk.Button(frame5, text='Back', font='comicsansms 10 bold', borderwidth=4,command=back)
    R11.place(x=800, y=20)
    R14 = tk.Button(frame6, text='Back', font='comicsansms 10 bold', borderwidth=4,command=back)
    R14.place(x=800, y=20)
    
    unreserve =tk.Button(frame3,text='UNRESERVE',font='comicsansms 12 bold',fg='red',bg='black',borderwidth=8,command=unreserveH)
    unreserve.place(x=50,y=510)
    variety_beds = ['Twin','Twin XL','Full','Queen','King','DayBed','WaterBed','AirBed','Four-Poster Bed','Round Bed','Ottoman Bed','Divan','Hanging Bed','Triple Bed','Simple Bed']
    setter = tk.StringVar()
    setter.set('Select')
    optionbed =tk.OptionMenu(frame3,setter,*variety_beds)
    optionbed.config(font='comicsansms 10 bold')
    optionbed.place(x=140,y=225)

    AC = ['Samsung','Panasonic','Sony','Bosch','LG','Haier']
    setterAC =tk.StringVar()
    setterAC.set('Select')
    optionac =tk.OptionMenu(frame3,setterAC,*AC)
    optionac.config(font='comicsansms 10 bold')
    frame2_can.create_text(900,320,text='AC  :  ',font='comicsansms 15 bold')
    optionac.place(x=140,y=285)

    TV = ['One plus','Sony Bravia Curved','Sony Bravia','MI','Samsung','TCL']
    setterTV = tk.StringVar()
    setterTV.set('Select')
    optiontv = tk.OptionMenu(frame3,setterTV,*TV)
    optiontv.config(font='comicsansms 10 bold')
    frame2_can.create_text(900,380,text='TV  :  ',font='comicsansms 15 bold')
    optiontv.place(x=140,y=345)

    wifi = ['Airtel','Jio','Hathway','Private Wifi(COST EXTRA)']
    setterwifi =tk.StringVar()
    setterwifi.set('Select')
    optionwifi =tk.OptionMenu(frame3,setterwifi,*wifi)
    optionwifi.config(font='comicsansms 10 bold')
    frame2_can.create_text(900,440,text='WIFI  :  ',font='comicsansms 15 bold')
    optionwifi.place(x=140,y=405)

can4.create_text(100,200,text='FILTER',font='comicsansms 15 bold')
can4.create_text(100,240,text='BED(S)  :  ',font='comicsansms 15 bold')
can4.create_text(100,300,text='AC  :  ',font='comicsansms 15 bold')
can4.create_text(100,360,text='TV  :  ',font='comicsansms 15 bold')
can4.create_text(100,420,text='WIFI  :  ',font='comicsansms 15 bold')    
# adding payement
#button

frame1_button=tk.Button(frame1,text="new customer click here",fg='blue',command=lambda:show_frame(frame2))
frame1_button.place(x=660,y=550)
frame2_button=tk.Button(frame1,text="sign-in",command=sign,font='comicsansms 9 bold',bg='#FFD43B',bd=4)
frame2_button.place(x=705,y=340)

#labels
frame1_label1=tk.Label(frame1,text="Alburj Group of Hotels",font = 'comicsansms 20 bold',bg='#FFD43B')
frame1_label1.place(x=300,y=20)
frame1_label2=tk.Label(frame1,text="Alburj DUBAI",font = 'comicsansms 12 bold',bg='#FFD43B',fg='white')
frame1_label2.place(x=210,y=510)
frame1_label3=tk.Label(frame1,text="Username  :",font = 'comicsansms 14 bold',bg='#FFD43B')
frame1_label3.place(x=550,y=250)
frame1_label4=tk.Label(frame1,text="Password  :",font = 'comicsansms 14 bold',bg='#FFD43B')
frame1_label4.place(x=550,y=300)
def paid():
            global asking
            asking = messagebox.askquestion('PAY','ARE YOU SURE')
            if asking == 'yes':
                    flag=True
                    time.sleep(1)
                    messagebox.showinfo('IMPORTANT','YOU HAVE SUCCESSFULLY PAID YOUR AMOUNT NOW YOU CAN ACCEPT THE ROOM')
            elif asking == 'no':
                flag=False
                pass
                messagebox.showerror('ERROR','YOU CANCELLED YOUR TRANSACTION\n  TRY AGAIN')
            else:
                messagebox.showerror('ERROR','YOU HAVE NOT REGISTERED YOUR INFO')
                res=var6.get()
                data2=[res]
                c.execute("INSERT INTO ALBURJROOMS('reservations') VALUES(?)",(data2,))
#entry
var=tk.StringVar()
var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
var4=tk.StringVar()
var5=tk.StringVar()
var6=tk.StringVar()
var7=tk.StringVar()
var8=tk.StringVar()
var9=tk.StringVar()
var10=tk.StringVar()
var69=tk.StringVar()
frame1_entry1=tk.Entry(frame1,textvariable=var7,font='calibri 14')
frame1_entry1.place(x=670,y=252,height=24)
frame1_entry2=tk.Entry(frame1,textvariable=var8,font='calibri 14')
frame1_entry2.place(x=670,y=300,height=24)
canvas=tk.Canvas(frame1,width=420,height=400)
canvas.place(x=50,y=100)
img =ImageTk.PhotoImage(Image.open("alburj.png"))
canvas.create_image(270,200,image=img)

frame2_can =tk.Canvas(frame2,width=1500,height=1800,bg='#FFE4C4')
frame2_can.pack()
lbx =tk.Listbox(frame3,bd=8,highlightthickness=20,width=70,height=5)
bolded = font.Font(weight='bold')
lbx.config(font=bolded)
lbx.place(x=300,y=240)
frame2_can.create_text(440,40,text='PERSONAL INFORMATION',font='comicsansms 15 bold')
var.set('First Name*')
frame2_entry =tk.Entry(frame2,textvariable=var,font='calibri 14')
frame2_can.create_window(110,270,window=frame2_entry)
var1.set('Middle Name*')
frame2_entry1 =tk.Entry(frame2,textvariable=var1,font='calibri 14')
frame2_can.create_window(320,270,window=frame2_entry1)
var2.set('Last Name*')
frame2_entry2 =tk.Entry(frame2,textvariable=var2,font='calibri 14')
frame2_can.create_window(530,270,window=frame2_entry2)
frame2_can.create_text(450,330,text='CONTACT INFORMATION',font='comicsansms 15 bold')
var3.set('Contact Number*')
frame2_entry3 =tk.Entry(frame2,textvariable=var3,font='calibri 14')
frame2_can.create_window(110,370,window=frame2_entry3)
var4.set('Email*')
frame2_entry4 =tk.Entry(frame2,textvariable=var4,font='calibri 14')
frame2_can.create_window(320,370,window=frame2_entry4)
var5.set('Guest Address*')
frame2_entry5 =tk.Entry(frame2,textvariable=var5,font='calibri 14')
frame2_can.create_window(530,370,window=frame2_entry5)  
var9.set('Username*')
frame2_entry6 =tk.Entry(frame2,textvariable=var9,font='calibri 14')
frame2_can.create_window(110,170,window=frame2_entry6)
var10.set('Password*')
frame2_entry7 =tk.Entry(frame2,textvariable=var10,font='calibri 14')
frame2_can.create_window(320,170,window=frame2_entry7)
name_get = var.get()
mid_get = var1.get()
last_get = var2.get()
num_get = var3.get()
em_get = var4.get()
ga_get = var5.get()
username=var9.get()
passwor=var10.get()

def signup():
    if len(name_get) and len(username) and len(passwor) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(ga_get) !=0 and num_get.isnumeric() and len(num_get) != 10:
        messagebox.showerror('contact details',"Please check contact details ")
    else:    
        quest = messagebox.askquestion('QUESTION???','Are You Sure???')
        if quest == 'yes':
            data = [username,passwor,name_get,mid_get,last_get,num_get,em_get,ga_get]
            c.executemany("INSERT INTO ALBURJROOMS ('USERNAME','PASSWORD','FIRST_NAME','MIDDLE_NAME','LAST_NAME','CONTACT_NUMBER','EMAIL','GUEST_ADDRESS') VALUES(?,?,?,?,?,?,?,?)",(data,))

            messagebox.showinfo('REGISTERED','Your Information Has Been Sucessfullly Registered With Us...Kindly Proceed Further')
            messagebox.showinfo('INFO','You can now sign-in and book your room')        
def unreserveH():
    quest = messagebox.askquestion('QUESTION','Are You Sure...Coz The Information Entered By You Will Be Lost')
    if quest == 'yes':
        c.execute("DELETE FROM ALBURJROOMS WHERE rowid =1")
    else:
        pass
R13 = tk.Button(frame2, text='sign-up', font='comicsansms 14 bold',fg='green',borderwidth=8,command=signup)
R13.place(x=30,y=430)    
R14 = tk.Button(frame2, text='back', font='comicsansms 10 bold',borderwidth=8,command=back2)
R14.place(x=800,y=20)    
          
   # can2.create_text(frame3,680,30,text='BURJ MANAGEMENT SYSTEM DEVELOPED BY "ATIF" AND CO-DEVELOPED BY "NISHAN"',font='comicsansms 20 bold',fill='black')
butHotelStatus = tk.Button(frame3,text='HOTEL STATUS',font='comicsansms 13 bold',borderwidth=5,command=booking)
butHotelStatus.place(x=20,y=40)
can2 =tk.Canvas(frame4, height=1500, width=1800, background='#FFE4C4')
can2.pack()
back3= tk.Button(frame4,text='back',font='comicsansms 13 bold',borderwidth=5,command=back)
back3.place(x=840,y=20)
can2.create_text(450,40,text='HOTEL-STATUS',font='comicsansms 30 bold',fill='#4D4D4D')
can2.create_text(80,100,text='TOTAL ROOMS',font='comicsansms 15 bold',fill='#4D4D4D')
can2.create_text(70,140,text='10',font='helivitica 40 bold',fill='blue')
can2.create_text(270, 100, text='AVAILABLE ROOMS', font='comicsansms 15 bold', fill='#4D4D4D')
can2.create_text(260, 140, text='10', font='helevitica 40 bold', fill='blue')
can2.create_text(460, 100, text='RESERVATIONS', font='comicsansms 15 bold', fill='#4D4D4D')
can2.create_text(450, 140, text='0', font='helevitica 40 bold', fill='blue')
can2.create_text(650, 100, text='CUSTOMERS', font='comicsansms 15 bold', fill='#4D4D4D')
can2.create_text(640, 140, text='0', font='helivitica 40 bold', fill='blue')
can2.create_text(840, 100, text='STAFF', font='comicsansms 15 bold', fill='#4D4D4D')
can2.create_text(850, 140, text='50', font='helivitica 40 bold', fill='blue')
can2.create_text(1030, 100, text='UNDER RENOVATION', font='comicsansms 15 bold', fill='#4D4D4D')
can2.create_text(1040, 140, text='5', font='helivitica 40 bold', fill='blue')
butDoor = tk.Button(frame3,text='ROOMS',font='comicsansms 13 bold',borderwidth=5,command=rooms)
butDoor.place(x=220,y=40)
loginpage = tk.Button(frame3,text='sign-out',font='comicsansms 13 ',borderwidth=5,command=back2)
loginpage.place(x=780,y=20)
    #can.create_text(720,160,text='PAYMENTS INFO',fill='black',font='comicsansms 13 bold')
butPayments = tk.Button(frame3,text='PAYMENTS INFO',font='comicsansms 13 bold',borderwidth=5,command=payment)
butPayments.place(x=340,y=40)
def room():
    ruum = {'Room-1': '$100000', 'Room-2': '$90000', 'Room-3': '$80000', 'Room-4': '$70000',
            'Room-5': '$60000',
            'Room-6': '$50000', 'Room-7': '$40000', 'Room-8': '$30000','Room-9': '$7000',
            'Room-10': '$5000'}
    lbx.insert(0, 'Room    :   Price')
    for key in ruum:
        tobeins = key, ':', ruum[key]
        END=10
        lbx.insert(END, tobeins)

    messagebox.showinfo('INFO', 'For More Info About Rooms You Can Press Rooms Button To Check')

    def lbxselect():
        for item in lbx.curselection():
                got = lbx.get(item)
                var9.set(got)
                lastvar = var9.get()
                try:
                        if asking:
                                c.execute('''INSERT INTO ALBURJROOMS ('FIRST_NAME','reservations') VALUES (?,?)''',(name_get,str(lastvar),))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo('REGISTERED','THANK YOU FOR BOOKING A ROOM WITH ALBURJHOTELS YOU CAN CHECK IN FROM THE SAME DAY \n  ENJOY YOUR DAY')

                except Exception as e:
                    messagebox.showwarning('WARNING','DEAR USER YOU FIRST NEED TO PAY AMOUNT FROM PAYMENT SECTION...')

    accbut =tk.Button(frame3,text='Accept Selected Room',borderwidth=4,command=lbxselect)
    accbut.place(x=670,y=590)

finalRoom=tk.Button(frame3, text='FIND ROOMS', font='comicsansms 17 bold', borderwidth=7, bg='grey',command=room)
finalRoom.place(x=600, y=440)

root.mainloop()