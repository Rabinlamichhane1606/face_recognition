from tkinter import *
import Recognition
import dataSet_creator
def main():
    window=Tk()
    window.title("Face Recognition")
    window.geometry('700x500')
    window.configure(bg='#273F6C')
    title=Label(window,text="Face Recognition",padx=500,bd=1,relief='solid',pady=20)
    title.pack()

    b=Button(window,text="Registration",padx=20,bd=2,pady=20,command=dataSet_creator.main)
    b.pack()

    b1=Button(window,text="Recognition",padx=20,bd=3,pady=20,command=Recognition.main)
    b1.pack()
    window.mainloop()


