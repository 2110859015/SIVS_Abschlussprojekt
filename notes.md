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

### CREATE NEW USER

-- Connect to the database as a privileged user (e.g., root)
-- Replace 'your_root_username' and 'your_root_password' with your actual root credentials
CREATE USER 'sivs'@'localhost' IDENTIFIED BY 'sivs123!';

-- Grant privileges on a specific database ('SIVS' in this case)
GRANT ALL PRIVILEGES ON SIVS.* TO 'sivs'@'localhost';

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