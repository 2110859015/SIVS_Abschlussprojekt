import json
import mariadb
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="sivs",
        password="sivs123!",
        host="127.0.0.1",
        port=3306,
        database="sivs"
    )
    print("Connected to Database!")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def login(name=None):
    username = request.form.get('username')
    password = request.form.get('password')

    # Standard values vulnerable to SQL Injection
    # sql_query = "SELECT COUNT(*) FROM user WHERE username = '"+username+"' AND password = '"+password+"';"
    # print(sql_query)
    # cur.execute(sql_query)

    # Parameterized values to prevent SQL Injection
    cur.execute("SELECT COUNT(*) FROM user WHERE username = ? AND password = ?;",
                (username, password))

    row_count = cur.fetchone()[0]

    if row_count > 0:
        return render_template('dashboard.html', name=username)
    return render_template('login.html')

@app.route('/users', methods=['POST'])
def check_user():
    username = request.json['username']
    password = request.json['password']

    cur.execute("SELECT COUNT(*) FROM user WHERE username = ? AND password = ?;",
                (username, password))
    row_count = cur.rowcount

    if row_count > 0:
        return "OK"
    return "NOT OK"


if __name__ == '__main__':
    app.run(debug=True)
