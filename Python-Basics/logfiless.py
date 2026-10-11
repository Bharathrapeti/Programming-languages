import tkinter as tk
from time import strftime
def update_time():
 current_time = strftime('%H:%M:%S %p')
 lbl_time.config(text=current_time)
 lbl_time.after(1000, update_time)
# GUI Setup
window = tk.Tk()
window.title("Digital Clock")
lbl_time = tk.Label(window, font=('Helvetica', 48), fg='blue')
lbl_time.pack()
update_time()
window.mainloop()
