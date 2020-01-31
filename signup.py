import database
from tkinter import *
window=Tk()
window.title("Validate")
window.geometry('700x500')
window.configure(bg='cyan')
title=Label(window,text="Face Recognition",padx=500,bd=1,relief='solid',pady=20)
title.pack()
label1=Label(window,text="Enter your Name:",font=("arial",15,"bold"),fg="steelblue").pack()
name=StringVar()
e1=Entry(window,textvariable=name,width=25,bg="lightgreen").pack()
label1=Label(window,text="Enter your Password:",font=("arial",15,"bold"),fg="steelblue").pack()
password=StringVar()
e2=Entry(window,textvariable=password,width=25,bg="lightgreen").pack()

b=Button(window,text="LogIn",padx=20,bd=2,pady=20)
b.pack()
b1=Button(window,text="SignUp",padx=20,bd=3,pady=20,command=database.insert)
b1.pack()
