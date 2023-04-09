import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()


Sql = "CREATE TABLE morse2 ( no INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), symbol VARCHAR(20), code VARCHAR(20))"
mycursor.execute(Sql)


Sql = " INSERT INTO morse2 (name, symbol, code) VALUES (%s, %s, %s)"
val = [('Error (also <HH>)', 'Error', '........'),
       ('Ampersand', '&', '.-...'),
       ('Apostrophe', '\'', '.----.'),
       ('At sign', '@', '.--.-.'),
       ('Bracket, close (parenthesis)', ')', '-.--.-'),
       ('Bracket, open (parenthesis)', '(', '-.--.'),
       ('Colon', ':', '---...'),
       ('Comma', ',', '--..--'),
       ('Equals sign', '=', '-...-'),
       ('Exclamation mark', '!', '-.-.--'),
       ('Full-stop (period)', '.', '.-.-.-'),
       ('Hyphen', '-', '-....-'),
       ('Multiplication sign (also x)', 'X', '-..-'),
       ('Percentage (literally 0/0)', '%', '----- -..-. -----'),
       ('Plus sign', '+', '.-.-.'),
       ('Quotation marks', '\"', '.-..-.'),
       ('Question mark (query)', '?', '..--..'),
       ('Slash', '/', '-..-.'),
       ('Semicolon', ';', '-.-.-')]

mycursor.executemany(Sql,val)

mydb.commit()

print(mycursor.rowcount, "Was Inserted")

#mycursor.execute("SELECT * FROM morse2")

#for x in mycursor:
#  print(x)


#mycursor.execute("DROP TABLE morse2")
