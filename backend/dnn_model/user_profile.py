from flask import Flask, session
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'chatbot'

mysql = MySQL(app)


def register_db(email, name, password):
    hashed_password = generate_password_hash(password)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE email = % s', (email,))
    account = cursor.fetchone()
    if account:
        msg = 'Account already exists !'
        return False, msg
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address !'
        return False, msg
    elif not re.match(r'[A-Za-z0-9]+', email):
        msg = 'name must contain only characters and numbers !'
        return False, msg
    else:
        cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s)', (email, name, hashed_password))
        mysql.connection.commit()
        msg = 'You have successfully registered !'
        return True, msg


def login_db(email, password):
    msg = ""
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    account = cursor.fetchone()
    if account is not None:
        stored_password = account['password']
        if check_password_hash(stored_password, password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            return True
        else:
            msg = "Incorrect Password"
            return False, msg
    else:
        msg = "Account does not exist."
        return False, msg


def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    # RETURNING.
    # By default itll be FALSE since user will be logged in
    # return TRUE when function is invoked and route to login page
