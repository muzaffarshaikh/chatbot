from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_mysqldb import MySQL

from user_profile import register_db, login_db

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

        global register_input  # making it global for the use in next function "/user_response"
        # User_Input = val3 # assigning the extracted value for response purpose
        register_input = [firstName, lastName, email, password, confirmPassword]

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        print(msg)
        return jsonify(register_input)

    if request.method == "GET":  # GET is not invoked only POST # Same logic as POST
        return jsonify(register_input)


@app.route('/login_data/', methods=['GET', 'POST'])
def login_service():
    if request.method == "POST" and 'email' in request.get_json() and 'password' in request.get_json():
        email = request.get_json()['email']
        password = request.get_json()['password']

        print(email, password)

        db_response = login_db(email, password)
        if db_response is True:
            print("Logged in successfully !")
        else:
            print("Incorrect username / password !")

        global login_Input  # making it global for the use in next function "/user_response"
        # User_Input = val3 # assigning the extracted value for response purpose
        login_Input = [email, password]
        return jsonify(login_Input)

    if request.method == "GET":  # GET is not invoked only POST
        # Same logic as POST
        return jsonify([login_Input])


# sending the users response from the above function to the frontend Angular
@app.route("/user_response/", methods=['GET'])
def response_user():
    #  global bot_response,user_responses
    return jsonify([register_input, login_Input])


if __name__ == '__main__':
    app.run(debug=True)
