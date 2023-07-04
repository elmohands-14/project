from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Employee Management System")
root.geometry("1310x515+20+100")
root.resizable(False,False)
root.configure(bg="#2c3e50")

#============== Entries frame ==========

entries_frame = Frame(root,bg='#2c3e50')
entries_frame.place(x=1,y=1,width=360,height=510)
title = Label(entries_frame,text="Employee Company",font=("Calibri",18,"bold"),bg="#2c3e50",fg="white")
title.place(x=10,y=1)
lblName = Label(entries_frame,text="Name",font=("Calibri",16),bg="#2c3e50",fg="white")
lblName.place(x=10,y=50)
textName = Entry(entries_frame,width=20,font=("Calibri",16))
textName.place(x=120,y=50)


lbljob = Label(entries_frame,text="Job",font=("Calibri",16),bg="#2c3e50",fg="white")
lbljob.place(x=10,y=90)
textjob = Entry(entries_frame,width=20,font=("Calibri",16))
textjob.place(x=120,y=90)

lblgender = Label(entries_frame,text="Gender",font=("Calibri",16),bg="#2c3e50",fg="white")
lblgender.place(x=10,y=130)
combogender = ttk.Combobox(entries_frame,state="readonly",width=18,font=("Calibri",16))
combogender['values'] = ("Male","Female")
combogender.place(x=120,y=130)

lblage = Label(entries_frame,text="Age",font=("Calibri",16),bg="#2c3e50",fg="white")
lblage.place(x=10,y=170)
textage = Entry(entries_frame,width=20,font=("Calibri",16))
textage.place(x=120,y=170)

lblemail = Label(entries_frame,text="Email",font=("Calibri",16),bg="#2c3e50",fg="white")
lblemail.place(x=10,y=210)
textemail = Entry(entries_frame,width=20,font=("Calibri",16))
textemail.place(x=120,y=210)

lblcontact = Label(entries_frame,text="Mobile",font=("Calibri",16),bg="#2c3e50",fg="white")
lblcontact.place(x=10,y=250)
textcontact = Entry(entries_frame,width=20,font=("Calibri",16))
textcontact.place(x=120,y=250)


lbladdress = Label(entries_frame,text="Address :",font=("Calibri",16),bg="#2c3e50",fg="white")
lbladdress.place(x=10,y=290)
textaddress = Text(entries_frame,width=30,height=2,font=("Calibri",16))
textaddress.place(x=10,y=330)


root.mainloop()
