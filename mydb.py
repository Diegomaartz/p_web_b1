#Database

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '!Mart!Dieg!23',   
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE cdmx_crime_ratio")
