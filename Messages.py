import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()
Sql = "CREATE TABLE INPUTS ( no INT PRIMARY KEY, Message VARCHAR(5000))"
mycursor.execute(Sql)

#mycursor.execute("DROP TABLE INPUTS")

#mycursor.execute("SELECT * FROM INPUTS")

#for x in mycursor:
#    print(x)
