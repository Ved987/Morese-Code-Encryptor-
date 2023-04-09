import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()


def First_Case(List, n):
    for i in range(0, int(n / 2)):
        List[i] = List[i] + ((n - 1) - i)
        List[n - (i + 1)] = List[n - (i + 1)] + i
    return List


def Second_Case(List, n, k):
    for i in range(0, n):
        List[i] = List[i] - k
    return List


def Third_Case(List, n):
    for i in range(0, n):
        if i % 2 == 0:
            List[i] = List[i] + ((n - 1) - i)
        else:
            List[i] = List[i] - ((n - 1) - i)
    return List


def Fourth_Case(List, n, k):
    for i in range(0, n):
        List[i] = List[i] - (k - i)
    return List


def main(Message,key):
    list_1 = []
    N_list = []
    for i in Message:
        if i != " ":
            list_1.append(ord(i))
    l_len = len(list_1)
    for i in range(0, key):
        if i % 2 == 0:
            N_list = First_Case(list_1, l_len)
        elif i % 3 == 0:
            N_list = Second_Case(list_1, l_len, key)
        elif i % 5 == 0:
            N_list = Third_Case(list_1, l_len)
        else:
            N_list = Fourth_Case(list_1, l_len, key)
    specials = {35: 'A:1', 36: 'A:2', 42: 'A:3', 60: 'A:4', 62: 'A:5', 91: 'A:6', 92: 'A:7', 93: 'A:8', 94: 'A:9',
                95: 'A:A', 96: 'A:B'}
    e_str = ""

    for i in N_list:
        if i in specials:
            e_str = e_str + specials[i]
        elif i < 33 or i > 122:
            e_str = e_str + str(i)
        else:
            e_str = e_str + chr(i)
    N_list = list(e_str)
    l_len = len(N_list)
    i = 0
    while i in range(0, l_len):
        if 'a' < N_list[i] < 'z':
            N_list[i] = N_list[i].upper()
            N_list.insert(i, '-')
            l_len = l_len + 1
        i = i + 1
    l_len = len(N_list)
    k_position = int((l_len / 10) * 7)
    N_list.insert(k_position, str(key))
    print(N_list)
    e_str = ""
    for i in N_list:
        e_str = e_str + i
    print(e_str)
    Sql = " DELETE FROM INPUTS WHERE no = 1"
    mycursor.execute(Sql)
    mydb.commit()
    print(mycursor.rowcount, "Record Deleted")
    Sql = " INSERT INTO INPUTS (no, Message) VALUES (%s, %s)"
    val = (1, e_str)
    mycursor.execute(Sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Record Inserted")
