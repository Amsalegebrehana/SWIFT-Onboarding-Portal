import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Amsa1e-Ge"
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE swiftconnectdb")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)