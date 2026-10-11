import tkinter as tk
from tkinter import messagebox

def login():
   username=username_Entry.get()
   password=password_Entry.get()

   if username=="bharath" and password=="1234":
       messagebox.showinfo("login successful",f"welcome,{username}!")
   else:
       messagebox.showwarning("login failed")

window = tk.Tk()
window.title("login form")
window.geometry("300x200")

tk.Label(window,text="username:").pack(pady=5)
username_entry = tk.Entry(window)
username_entry.pack(pady=5)

tk.Label(window,text="password:").pack(pady=5)
username_entry = tk.Entry(window,show="*")
username_entry.pack(pady=5)

login_button = tk.Button(window,text='login',command=login)
login_button.pack(pady=10)

window.mainloop()

