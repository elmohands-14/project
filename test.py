from tkinter import *
from tkinter import ttk
<<<<<<< HEAD
#hacker me
=======
# salah ali
>>>>>>> 50c5d52f03f63d3dc16d6356efea999e946cc6cc

root = Tk()
root.title("tester")
root.geometry("400x400")

style = ttk.Style()
style.configure("test.Treeview",font=("cairo",16),rowheight=30)
tv = ttk.Treeview(root,columns=(1,2,3),style="test.Treeview")

tv.heading("1",text="Id")
tv.column("1",width=100)

tv.heading("2",text="Name")
tv.column("2",width=120)

tv.heading("3",text="Phone")
tv.column("3",width=150)

tv['show'] = 'headings'

tv.pack(pady=10)



root.mainloop()