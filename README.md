# How to use?
Start Web-Server by using the console: 
- HTTPS: flask run --host=0.0.0.0 --cert=certificates/cert.pem --key=certificates/key.pem --port=443
- HTTP: flask run --host=0.0.0.0

Web-Server is available under: 
- https://127.0.0.1:443/ if var is_https = True OR
- http://127.0.0.1:5000/ if var is_https = False

## Vulnerabilities
- To activate SQL Injection set var is_sql_inject = True and restart app.py
- To use secure/unsecure communication refer to "How to use" (http/https)
- To activate XSS, change line to {% autoescape false %} in \templates\dashboard.html
- To deactivate XSS, change line to {% autoescape true %} in \templates\dashboard.html

## Flask MongoDB
https://pythonbasics.org/flask-mongodb/

## Flask Mongo Engine error:
pip uninstall flask-mongoengine
pip install git+https://github.com/idoshr/flask-mongoengine.git@1.0.1

## MariaDB
root
qwertz123!!

Service: MariaDB
Port 3306

User SIVS_DB_Export.sql for database (DB + Tables + Data)

### CREATE NEW USER

-- Connect to the database as a privileged user (e.g., root)
-- Replace 'your_root_username' and 'your_root_password' with your actual root credentials
CREATE USER 'sivs'@'localhost' IDENTIFIED BY 'sivs123!';

-- Grant privileges on a specific database ('SIVS' in this case)
GRANT ALL PRIVILEGES ON sivs.* TO 'sivs'@'localhost';

-- Reload the privileges to apply the changes
FLUSH PRIVILEGES;


### INSERT USER IN DB SIVS

#### MARIA:
INSERT INTO user (username, password)
VALUES ('test','test123');

#### PYTHON:
cur.execute("INSERT INTO user (username, password) VALUES (?, ?)",
                (username, password))
conn.commit()

### SQL Injection for LOGIN (no prepared statements)
(careful, space at the end)
hacker' OR 1=1; -- 

### XSS
Enter in search bar after login

<iframe src="javascript:alert(`xss`)">
<script>alert('javascript was executed')</script>

### CERTIFICATE HTTPS
Enter passphrase when starting server.
Passphrase: geheim!

