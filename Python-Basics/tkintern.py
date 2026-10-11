from tkinter import *
root=Tk()
r1 = Radiobutton(root, text = "C", value = 1, height = 2, width = 10)
r2 = Radiobutton(root, text = "C++", value = 2, height = 2, width = 10)
r3 = Radiobutton(root, text = "JAVA",value = 3, height = 10, width = 100)
r1.pack()
r2.pack()
r3.pack()
root.mainloop()
