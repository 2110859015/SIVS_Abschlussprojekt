import json
import mariadb
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
app.secret_key = "asdasdasd324"

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

is_sql_inject = True


# fetch results from database
def search_results(query):
    # Implement the SQL query to fetch search results based on the query
    # Replace this with your actual SQL query logic
    # For example: "SELECT * FROM your_table WHERE column_name LIKE '%query%'"
    try:
        cur = conn.cursor()
        query = f"%{query}%"
        cur.execute("SELECT * FROM note WHERE title LIKE ?", (query,))
        results = cur.fetchall()
        return results
    except mariadb.Error:
        print(f"Error executing SQL query: {e}")
        return None


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' in session and session['username'] is not None:
        if request.method == 'POST':
            search_query = request.form.get('search_query')
            results = search_results(search_query)
            return render_template('dashboard.html', results=results, search_query=search_query)
        else:
            return render_template('dashboard.html')
    else:
        return redirect(url_for("home"))


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    try:
        cur = conn.cursor()

        # Standard values vulnerable to SQL Injection
        if is_sql_inject:
            sql_query = "SELECT COUNT(*) FROM user WHERE username = '" + username + "' AND password = '" + password + "';"
            print(sql_query)
            cur.execute(sql_query)

        # Parameterized values to mitigate SQL Injection
        else:
            cur.execute("SELECT COUNT(*) FROM user WHERE username = ? AND password = ?;",
                        (username, password))

        row_count = cur.fetchone()[0]
        if row_count > 0:
            session['username'] = username
            print("username set")
            return redirect(url_for("dashboard"))
            # return render_template('dashboard.html', name=username)
        return redirect(url_for("home"))
    except e:
        return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
