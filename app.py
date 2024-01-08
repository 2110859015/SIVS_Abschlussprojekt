from db_connector import get_db_connection
import mariadb
from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
app.secret_key = "asdasdasd324"

conn = get_db_connection()

is_sql_inject = False
is_https = True


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
        print(f"Error executing SQL query: {mariadb.Error}")
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
            print(username + ' logged in')
            return redirect(url_for("dashboard"))
            # return render_template('dashboard.html', name=username)
        return redirect(url_for("home"))
    except mariadb.Error:
        return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    if is_https:
        app.run(host="0.0.0.0", port=443, debug=True,
                ssl_context=("certificates/cert.pem", "certificates/key.pem")
                )
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
