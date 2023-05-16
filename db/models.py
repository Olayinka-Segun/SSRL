import mysql.connector 


mydb = mysql.connector.connect (
  host="localhost",
  user="root",
  password="sege_d_boy@2002",
  database = "internDB",
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE internDB")
#mycursor.execute("CREATE TABLE interninfo(Intern_id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100) NOT NULL, Email VARCHAR(100)UNIQUE NOT NULL, Phone_number VARCHAR(50)UNIQUE NOT NULL, Role VARCHAR(10) NOT NULL, Section VARCHAR(100) NOT NULL)")
