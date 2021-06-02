import json

from flask import Flask, session
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime
import time
import pymysql

connection = pymysql.connect(host="localhost", user="root", passwd="", database="chatbot")

app = Flask(__name__)
CORS(app)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'chatbot'

mysql = MySQL(app)


def register_db(email, name, password):
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
        cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s)',
                       (email, name, password))
        mysql.connection.commit()
        msg = 'You have successfully registered !'
        return True, msg


def login_db(email, password):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE email = % s AND password = % s', (email, password,))
    account = cursor.fetchone()
    if account:
        session['loggedin'] = True
        session['id'] = account['id']
        session['email'] = account['email']
        return True
    else:
        return False


def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    # RETURNING.
    # By default itll be FALSE since user will be logged in
    # return TRUE when function is invoked and route to login page


def save_chat(email, client_request, server_response):
    cursor = connection.cursor()

    emailQuery = 'select id from users where email="' + email + '"'
    cursor.execute(emailQuery)
    userIDTuple = cursor.fetchone()
    userID = userIDTuple[0]

    formatted_date = str(datetime.date.today())
    current_date = formatted_date

    formatted_time = time.strftime("%H:%M:%S", time.localtime())
    current_time = formatted_time

    chatJSONObject = str(json.dumps({'user_message': client_request, 'bot_response': server_response}))

    cursor.execute('INSERT INTO chats VALUES (NULL, % s, % s, % s, % s)', (userID, chatJSONObject, current_date, current_time))
    connection.commit()
