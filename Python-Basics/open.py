from tkinter import *
top=Tk()
l1=Label(top,text="Label1",bg="blue")
l2=Label(top,text="Label2",bg="red" )
l3=Label(top,text="Label2",bg="green")
l1.grid(row=0,column=0,)
l2.grid(row=0,column=1,)
l3.grid(row=1,column=1,)
top.mainloop()