import mysql.connector
import time

while True:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="testdb"
        )
        print("Connected to MySQL")
        db.close()
    except:
        print("Waiting for DB...")
    time.sleep(5)
