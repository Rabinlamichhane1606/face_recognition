import database
from tkinter import *
import database
window=Tk()
window.title("SignUP")
window.geometry('700x500')
window.configure(bg='#273F6C')
title=Label(window,text="Face Recognition",padx=500,bd=1,relief='solid',pady=20)
title.pack()
label1=Label(window,text="Enter your Name:",font=("arial",40,"bold"),fg="steelblue").pack()
name=StringVar()
entry_box=Entry(window,textvariable=name,width=25,bg="lightgreen").pack()
label=Label(window,text="Enter your Password:",font=("arial",40,"bold"),fg="steelblue").pack()
password=StringVar()
entry_box1=Entry(window,textvariable=password,width=25,bg="lightgreen").pack()

b=Button(window,text="LogIn",padx=20,bd=2,pady=20)
b.pack()
name.set(entry_box)
password.set(entry_box1)
print(name.get())
b1=Button(window,text="SignUp",padx=20,bd=3,pady=20,command=database.insert(name.get(),password.get()))
b1.pack()
window.mainloop()

