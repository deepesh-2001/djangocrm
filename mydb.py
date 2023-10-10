
import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
)

#prepare a cursor object

cursorObject= dataBase.cursor()

#Create a database
print('creating')
cursorObject.execute("CREATE DATABASE project")

print("ALL DONE!")