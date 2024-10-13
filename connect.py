import mysql.connector

def db_connection():
    conn = mysql.connector.connect(
        host="kr-mysql-server.mysql.database.azure.com",  
        user="Ruby",  
        password="Password123!",  
        database="krindustriesdb" 
    )
    return conn
