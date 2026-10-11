from tkinter import *

me = Tk()

# Correct variable names and fixed Label spelling
label1 = Label(me, text="Label 1", bg="blue")
label2 = Label(me, text="Label 2", bg="red")

# Corrected pack() usage
label1.pack(fill=X, side=TOP,expand=TRUE)
label2.pack(fill=X, side=RIGHT) 

me.mainloop()
