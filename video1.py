import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #port = "3306",
    #database = ""
)
print(con)


