import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()
global morse_str
# noinspection PyRedeclaration
morse_str = ""


def check_non_symbol(n):
    global morse_str
    if 'a' <= n <= 'z':
        n = n.upper()
    Sql = "SELECT code FROM morse WHERE letter ="
    Sql = Sql + '\'' + n + '\''
    mycursor.execute(Sql)
    S1 = mycursor.fetchall()
    ch = S1[0][0]
    morse_str = morse_str + ch


def check_symbol(n):
    global morse_str
    Sql = "SELECT code FROM morse2 WHERE Symbol ="
    Sql = Sql + '\'' + n + '\''
    mycursor.execute(Sql)
    S1 = mycursor.fetchall()
    ch = S1[0][0]
    morse_str = morse_str + ch


def main():
    global morse_str
    Sql = "SELECT Message FROM INPUTS"
    mycursor.execute(Sql)
    L = mycursor.fetchall()
    Message = L[0][0]
    for i in Message:
        if i != ' ':
            if 'A' <= i <= 'Z' or '0' <= i <= '9' or 'a' <= i <= 'z':
                check_non_symbol(i)
                morse_str = morse_str + " "
            else:
                check_symbol(i)
                morse_str = morse_str + " "

    Sql = " UPDATE INPUTS SET Message = %s WHERE no = %s"
    val = (morse_str, 1)
    mycursor.execute(Sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Record Updated")
