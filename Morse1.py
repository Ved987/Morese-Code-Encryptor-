import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkey1505",
    database="3semproject"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE morse (no INT AUTO_INCREMENT PRIMARY KEY, letter CHAR, code VARCHAR(10))")

Sql = " INSERT INTO morse (letter,code) VALUES (%s, %s)"
val = [
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
]

mycursor.executemany(Sql, val)
mydb.commit()
print(mycursor.rowcount, "Was Inserted")

# mycursor.execute("SELECT * FROM morse")
# for x in mycursor:
#    print(x)

#mycursor.execute("DROP TABLE morse")

Sql = " INSERT INTO morse (letter,code) VALUES (%s, %s)"
val = [
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
    ('0', '-----')]

mycursor.executemany(Sql, val)

mydb.commit()

print(mycursor.rowcount, "Was Inserted")
