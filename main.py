from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Employee Management System")
root.geometry("1240x615+20+100")
root.resizable(False,False)
root.configure(bg="#2c3e50")


logo = PhotoImage(file='logo2.png')
lbl_logo = Label(root,image=logo,bg='#2c3e50')
lbl_logo.place(x=80,y=510)

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


#====== [Define] =============
def hide():
    root.geometry("360x510")
def show():
    root.geometry("1240x615")

btnhide = Button(entries_frame,text="HIDE",bg="white",bd=1,relief=SOLID ,cursor='hand2',command=hide)
btnhide.place(x=270,y=10)
btnshow = Button(entries_frame,text="SHOW",bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnshow.place(x=310,y=10)
# =============Buttons Frame ================

btn_frame = Frame(entries_frame,bd=1,relief=SOLID,bg="#2c3e50")
btn_frame.place(x=10,y=400,width=335,height=100)

btnadd =Button(btn_frame,
               text="Add Details",
               width=14,
               height=1,
               font=("Calibri",16),
               fg="white",
               bg="#16a085",
               bd=0
               ).place(x=4,y=5)


btnedit =Button(btn_frame,
               text='Update Details',
               width=14,
               height=1,
               font=("Calibri",16),
               fg="white",
               bg="#2980b9",
               bd=0
               ).place(x=4,y=50)

btndelete =Button(btn_frame,
               text='Delete Details',
               width=14,
               height=1,
               font=("Calibri",16),
               fg="white",
               bg="#c0392b",
               bd=0
               ).place(x=170,y=5)


btnclear =Button(btn_frame,
               text="Clear Details",
               width=14,
               height=1,
               font=("Calibri",16),
               fg="white",
               bg="#f39c12",
               bd=0
               ).place(x=170,y=50)


#========== [table frame] =================
treeframe = Frame(root,bg="white")
treeframe.place(x=365,y=1,width=875,height=610)

# @
style = ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("calibri",13))
tv = ttk.Treeview(treeframe,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")

tv.heading("1",text="Id")
tv.column("1",width="40")

tv.heading("2",text="Name")
tv.column("2",width="140")

tv.heading("3",text="Age")
tv.column("3",width="50")


tv.heading("4",text="Job")
tv.column("4",width="120")



tv.heading("5",text="Email")
tv.column("5",width="150")

tv.heading("6",text="Gender")
tv.column("6",width="90")

tv.heading("7",text="Mobile")
tv.column("7",width="150")

tv.heading("8",text="Address")
tv.column("8",width="150")

tv['show'] = 'headings'

tv.place(x=1,y=1,height=610,width=875)


root.mainloop()
