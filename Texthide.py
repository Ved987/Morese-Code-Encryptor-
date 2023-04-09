import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()


def Texthide(Cover):
    mycursor.execute("SELECT * FROM INPUTS")
    morse = ""
    for x in mycursor:
        morse = x[1]
    Cover1 = []
    word = ''
    for i in Cover:
        if i != ' ':
            word = word + i
        else:
            Cover1.append(word)
            word = ''
    Cover1.append(word)
    pos = 1
    while pos < len(Cover1):
        for i in morse:
            if i == '.':
                Cover1.insert(pos, ' ')
                pos = pos + 2
                Cover1.insert(pos, '  ')
                pos = pos + 2
            elif i == '-':
                Cover1.insert(pos, '  ')
                pos = pos + 2
                Cover1.insert(pos, ' ')
                pos = pos + 2
            elif i == ' ':
                Cover1.insert(pos, ' ')
                pos = pos + 2
                Cover1.insert(pos, ' ')
                pos = pos + 2
            elif i == '\t':
                Cover1.insert(pos, '  ')
                pos = pos + 2
                Cover1.insert(pos, '  ')
                pos = pos + 2
        else:
            Cover1.insert(pos, ' ')
            pos = pos + 2
    key = 0
    for i in morse:
        if i == " ":
            key = key + 1
    Cover1.insert(0, str(key) + ' ')
    Cover = ""
    for i in Cover1:
        Cover = Cover + i
    return Cover


def Text_recover(Cover):
    Cover1 = []
    word = ''
    check = 0
    for i in Cover:
        if i != ' ':
            word = word + i
            check = 0
        else:
            if check == 0:
                Cover1.append(word)
            word = ''
            Cover1.append(i)
            check = 1
    Cover1.append(word)
    key = int(Cover1.pop(0))
    Cover1.pop(0)
    pos = 1
    morse = ''
    check = 0
    while pos < len(Cover1)-5 and check < key:
        if Cover1[pos + 1] == ' ':
            before = 2
            pos = pos + 3
        else:
            before = 1
            pos = pos + 2
        if Cover1[pos + 1] == ' ':
            after = 2
            pos = pos + 3
        else:
            after = 1
            pos = pos + 2

        if before == 1 and after == 2:
            morse = morse + '.'
        elif before == 2 and after == 1:
            morse = morse + '-'
        elif before == 1 and after == 1:
            morse = morse + ' '
            check = check + 1
        elif before == 2 and after == 2:
            morse = morse + '   '

    return morse
