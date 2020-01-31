import mysql.connector
def insert(name,password):
    try:
        mydb=mysql.connector.connect(host="localhost", user="root", password="",database="users")
    except:
        print("Failed to connect to database")
        exit()
    mycursor=mydb.cursor()
    sql="INSERT INTO login(name,password) VALUES(%s,%s)"
    values=(name,password)
    mycursor.execute(sql,values)
    mydb.commit()

    




