import mysql.connector
try:
        mydb=mysql.connector.connect(host="localhost", user="root", password="",database="users")
except:
        print("Failed to connect to database")
        exit()
def insert(name,password):
    mycursor=mydb.cursor()
    sql="INSERT INTO login(name,password) VALUES(%s,%s)"
    values=(name,password)
    mycursor.execute(sql,values)
    mydb.commit()
def insert_name(id,name):
    mycursor=mydb.cursor()
    sql="INSERT INTO username(id,name) VALUES(%s,%s)"
    values=(id,name)
    mycursor.execute(sql,values)
    mydb.commit()
def select():
    mycursor=mydb.cursor()
    sql="SELECT name,password FROM login"
    mycursor.execute(sql)
    names=mycursor.fetchall()
    return names
def select_name():
    mycursor=mydb.cursor()
    sql="SELECT id,name FROM username"
    mycursor.execute(sql)
    names=mycursor.fetchall()
    return names
    

    




