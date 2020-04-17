import mysql.connector

cnx = mysql.connector.connect(user='root', password='user_password',host='127.0.0.1',port=3306)
cursor = cnx.cursor()
cursor.execute("show databases")
cursor.fetchall()
cnx.close()
