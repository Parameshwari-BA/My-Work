from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Connected to MySQL successfully!'")
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
