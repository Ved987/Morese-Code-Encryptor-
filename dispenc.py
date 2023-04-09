import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()


def main():
    mycursor.execute("SELECT * FROM INPUTS")
    for x in mycursor:
        return x[1]

