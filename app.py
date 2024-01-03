from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password are valid
    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid username or password. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
