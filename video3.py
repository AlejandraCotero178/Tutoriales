import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #port = "3306",
    database = "paises"
)
print(con)

cursor = con.cursor()

#sql ="""CREATE TABLE clientes (nombre VARCHAR(100), direccion VARCHAR(200))"""
sql = """ALTER TABLE clientes ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY """

cursor.execute(sql)
con.commit()

cursor.execute("SHOW TABLES")
for dato in cursor:
 print(dato)


con.close()