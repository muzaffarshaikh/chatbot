from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

from user_profile import register_db, login_db, save_chat
from bot_main import bot_response

app = Flask(__name__)
CORS(app)

app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'chatbot'
mysql = MySQL(app)


@app.route("/", methods=['GET'])
def index():
    return "Rest Service Index Page. \n Waiting for response from Angular App."


# making it global for the use in next function "/user_response"
global register_input, login_input


@app.route('/register_data/', methods=['GET', 'POST'])
def register_service():
    if request.method == 'POST' and 'firstName' in request.get_json() and 'lastName' in request.get_json() and 'email' in request.get_json() and 'password' in request.get_json():
        firstName = request.get_json()['firstName']
        lastName = request.get_json()['lastName']
        email = request.get_json()['email']
        password = request.get_json()['password']
        confirmPassword = request.get_json()['confirmPassword']

        name = firstName + " " + lastName
        print(name, email, password, confirmPassword)  # prints the extracted value
        db_response = register_db(email, name, password)
        print(db_response)

        if db_response[0] is True:
            return jsonify({'response': True})
        else:
            return jsonify({'response': False, 'message': db_response[1]})


@app.route('/login_data/', methods=['GET', 'POST'])
def login_service():
    if request.method == "POST" and 'email' in request.get_json() and 'password' in request.get_json():
        email = request.get_json()['email']
        password = request.get_json()['password']
        print(email, password)

        db_response = login_db(email, password)
        if db_response is True:
            print("Logged in successfully !")
            return jsonify({'response': True})
        else:
            print("Incorrect username / password !")
            message = 'Incorrect username / password !'
            return jsonify({'response': False, 'message': message})


# function for getting the users response from the frontend Angular
@app.route('/input_data/', methods=['GET', 'POST'])
def chat_messaging():
    # make provision for request ID.
    if request.method == "POST":
        email = 'gg@gmail.com'
        # gets the json data from angular which is in array {"userinput":"as"}
        client_request = request.get_json()['userinput']
        server_response = bot_response(client_request, email)
        # Server side terminal statements
        print("Request from Client (User) : " + client_request)
        print("Response from Server (Bot) : " + server_response)

        save_chat(email, client_request, server_response)

        return jsonify({'response': server_response, 'userinput': client_request})


@app.route('/user_info/', methods=['GET', 'POST'])
def user_profile():
    # global user_fname, user_lname
    user_fname = 'Taylor'
    user_lname = 'Swift'
    return jsonify({'user_fname': user_fname, 'user_lname': user_lname})


@app.route('/edit_user_info/', methods=['GET', 'POST'])
def edit_user_profile():
    if request.method == "POST":
        new_info = request.get_json()
        new_user_image = new_info['user_image']
        new_user_fname = new_info['user_fname']
        new_user_lname = new_info['user_lname']
        print(new_user_image, new_user_fname, new_user_lname)
    return jsonify({'user_fname': new_user_fname, 'user_lname': new_user_lname})


if __name__ == '__main__':
    app.run(debug=True)
