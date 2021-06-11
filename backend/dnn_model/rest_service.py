from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

from user_profile import register_db, login_db, userprofile, editprofile
from bot_main import bot_response, save_chat, load_chat

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
        db_response = register_db(email, name, password)

        if db_response[0] is True:
            return jsonify({'response': True})
        else:
            return jsonify({'response': False, 'message': db_response[1]})


logged_user_email = ""
response = False
message = ""


@app.route('/login_data/', methods=['GET', 'POST'])
def login_service():
    if request.method == "POST" and 'email' in request.get_json() and 'password' in request.get_json():
        email = request.get_json()['email']
        password = request.get_json()['password']

        global logged_user_email
        global response, message
        logged_user_email = email

        db_response = login_db(email, password)
        print(db_response)
        message = db_response
        if db_response is True:
            print("Logged in successfully !")
            response = True
            return jsonify({'response': True, 'email': email})
        else:
            print(message)
            return jsonify({'response': False, 'message': message, 'email': email})


@app.route('/logged_user/', methods=['GET', 'POST'])
def log_user():
    if request.method == "GET":
        global response
        if response:
            print("Logged response -> ", response)
            response = False
            return jsonify({'response': True})
        else:
            # print("not logged in")
            return jsonify({'response': False})


@app.route('/logged_out_user/', methods=['GET', 'POST'])
def log_out_user():
    if request.method == "POST":
        logout = request.get_json()
        global response
        response = False
        print("logout response -> ", response)
        return jsonify({'response': response})


@app.route('/validation/', methods=['GET', 'POST'])
def validate():
    if request.method == "GET":
        global message
        print(message)
        return jsonify({'response': message})


@app.route('/load_chat/', methods=['GET', 'POST'])
def load_chat_into_convo():
    email = logged_user_email
    conversation = load_chat(email)
    for data_item in conversation:
        user = data_item[0]
        bot = data_item[1]

        return jsonify({'response': bot, 'userinput': user})


# function for getting the users response from the frontend Angular
@app.route('/input_data/', methods=['GET', 'POST'])
def chat_messaging():
    # make provision for request ID.
    if request.method == "POST":
        email = logged_user_email
        # gets the json data from angular which is in array {"userinput":"as"}
        client_request = request.get_json()['userinput']
        server_response = bot_response(client_request, email)
        # Server side terminal statements
        print("Logged in User: " + logged_user_email)
        print("Request from Client (User) : " + client_request)
        print("Response from Server (Bot) : " + server_response)

        save_chat(email, client_request, server_response)

        return jsonify({'response': server_response, 'userinput': client_request, 'email': logged_user_email})


@app.route('/user_info/', methods=['GET', 'POST'])
def user_profile():
    # global user_fname, user_lname
    user_details = userprofile(logged_user_email).split(' ')
    user_fname = user_details[0]
    user_lname = user_details[1]
    return jsonify({'user_fname': user_fname, 'user_lname': user_lname})


@app.route('/edit_user_info/', methods=['GET', 'POST'])
def edit_user_profile():
    if request.method == "POST":
        new_info = request.get_json()
        new_user_image = new_info['user_image']
        new_user_fname = new_info['user_fname']
        new_user_lname = new_info['user_lname']
        name = new_user_fname + " " + new_user_lname
        message_f = editprofile(name, logged_user_email)
        print(new_user_image, new_user_fname, new_user_lname)
    return jsonify({'user_fname': new_user_fname, 'user_lname': new_user_lname, 'response': message_f})


if __name__ == '__main__':
    app.run(debug=True)
