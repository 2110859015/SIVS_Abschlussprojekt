import mariadb
import sys

def get_db_connection():
    try:
        conn = mariadb.connect(
            user="sivs",
            password="sivs123!",
            host="127.0.0.1",
            port=3306,
            database="sivs"
        )
        print("Connected to Database!")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)