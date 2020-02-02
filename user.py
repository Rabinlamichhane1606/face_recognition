from tkinter import *
import database
from tkinter import messagebox
import face_Recognition
import functools 
import operator 
class users:
    def __init__(self):
        self.names=''
        self.name=''
        self.password=''

    def insert(self):
        self.names=database.select()
        str = functools.reduce(operator.add, (self.names))
        #print(self.names)
        #print(str)
        tuple(self.names)
        dictionary={}
        for a, b in self.names: 
            dictionary.setdefault(a, []).append(b)
        #print(dictionary)
        di=dict(self.names)
        print(di)
        #''.join(self.names)
        #print(self.names)
        #print(self.name.get())
        for i in str:
            if(i==self.name.get()):
                messagebox.showinfo("Error", "Username already exist retry again using another names")
                break
        database.insert(self.name.get(),self.password.get())
                
    def program(self):
        flag=1
        self.names=database.select()
        tuple(self.names)
        di=dict(self.names)
        print(di)
        x=di.keys()
        #list(x)
        y=di.values()
        #list(y)
        #print(self.names)
        print(str)
        #tuple(self.names)
        
        #for i in x,y:
        for i,j in di.items():
            if self.name.get()==i and self.password.get()==j:
            #if(i==self.name.get() and j==self.password.get()):
                messagebox.showinfo("Welome", "Welcome to face Recognition System")
                face_Recognition.main()
                flag=0
        if(flag==1):
            messagebox.showinfo("Invalid", "Invalid username or password")
        
        
            
        
            

    def main(self):
        screen=Tk()
        screen.geometry("300x400")
        screen.configure(bg="#c203fc")
        screen.title("Face recognition")
        Label(text="Face Recognition 1.0",bg="cyan",width="300",height="2", font=("calibri",13)).pack()
        Label(text="").pack()
        Label(text="").pack()

        global name
        global password
        self.name=StringVar()
        self.password=StringVar()
       
        
        Label(text="UserName:",bg="#03f8fc",font=("calibri",13),width="13",height="1").pack()
        Label(text="").pack()
        user_entry=Entry(textvariable=self.name,bg="#fcdf03").pack()
        Label(text="").pack()
        Label(text="Password:",bg="#03f8fc",font=("calibri",13),width="13",height="1").pack()
        Label(text="").pack()
        password_entry=Entry(textvariable=self.password,bg="#fcdf03").pack()
        Label(text="").pack()
        Button(text="Login",width="30",height="2",bg="#d3fc03",command=self.program).pack()
        Label(text="").pack()
        
        Button(text="SignUp",width="30",height="2",bg="#d3fc03",command=self.insert).pack()
        screen.mainloop()


#inheritance
class user_child(users):
    def __init__(self):
        super().__init__()

#overidding
class user_child1(users):
    def __init__(self):
        self.name='Rabin'
u=users()
u.main()
