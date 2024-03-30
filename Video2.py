import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #port = "3306",
    database = "paises"
)
#print(con)

cursor = con.cursor()
cursor.execute("SHOW DATABASES")
#cursor.execute("CREATE DATABASE PAISES")

for bd in cursor:
    print(bd)

con.close()