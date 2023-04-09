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
        List[i] = List[i] - ((n - 1) - i)
        List[n - (i + 1)] = List[n - (i + 1)] - i
    return List


def Second_Case(List, n, k):
    for i in range(0, n):
        List[i] = List[i] + k
    return List


def Third_Case(List, n):
    for i in range(0, n):
        if i % 2 == 0:
            List[i] = List[i] - ((n - 1) - i)
        else:
            List[i] = List[i] + ((n - 1) - i)
    return List


def Fourth_Case(List, n, k):
    for i in range(0, n):
        List[i] = List[i] + (k - i)
    return List


def main(list_1):
    list_2 = []
    str1 = ''
    for i in list_1:
        if i != ' ':
            str1 = str1 + i
        else:
            list_2.append(str1)
            str1 = ''
    list_2.append(str1)
    print(list_2)
    Message = ''
    for morse in list_2:
        Sql = "SELECT letter FROM morse WHERE code ="
        Sql = Sql + '\'' + morse + '\''
        mycursor.execute(Sql)
        S1 = mycursor.fetchall()
        if len(S1) == 0:
            Sql = "SELECT Symbol FROM morse2 WHERE code ="
            Sql = Sql + '\'' + morse + '\''
            mycursor.execute(Sql)
            S1 = mycursor.fetchall()
        if len(S1) != 0:
            Message = Message + S1[0][0]
    print(Message)
    Message = list(Message)
    k_pos = int(((len(Message) - 1) / 10) * 7)
    key = int(Message[k_pos])
    Message.pop(k_pos)
    N_list = []
    list_1 = []
    specials = {'A:1': 35, 'A:2': 36, 'A:3': 42, 'A:4': 60, 'A:5': 62, 'A:6': 91, 'A:7': 92, 'A:8': 93, 'A:9': 94,
                'A:A': 95, 'A:B': 96}

    i = 0
    while i in range(0, len(Message)):
        if Message[i] == '-':
            Message[i + 1] = Message[i + 1].lower()
            Message.remove(Message[i])
        i = i + 1

    i = 0
    while i in range(0, len(Message)):
        if Message[i] == ':':
            check = Message[i - 1] + Message[i] + Message[i + 1]
            if check in specials:
                Message[i] = chr(specials[check])
                Message.pop(i - 1)
                Message.pop(i)
        i = i + 1

    i = 0
    while i in range(0, len(Message)):
        if i < len(Message) - 2:
            if '0' <= Message[i] <= '9' and '0' <= Message[i + 1] <= '9' and '0' <= Message[i + 2] <= '9':
                num = Message[i] + Message[i + 1] + Message[i + 2]
                print(num)
                Message.pop(i)
                list_1.append(int(num))
                i = i + 1
            else:
                list_1.append(ord(Message[i]))
        i = i + 1
    list_1.append(ord(Message[len(Message) - 2]))
    list_1.append(ord(Message[len(Message) - 1]))

    l_len = len(list_1)

    for i in range(key - 1, -1, -1):
        if i % 2 == 0:
            N_list = First_Case(list_1, l_len)
        elif i % 3 == 0:
            N_list = Second_Case(list_1, l_len, key)
        elif i % 5 == 0:
            N_list = Third_Case(list_1, l_len)
        else:
            N_list = Fourth_Case(list_1, l_len, key)

    D_message = ""
    for i in N_list:
        D_message = D_message + chr(i)
    return D_message
