import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "2522"
)

mycursor = mydb.cursor()
#mycursor.execute("create database testdb")

mycursor.execute("show databases")
for dp in mycursor:
    print(dp)
