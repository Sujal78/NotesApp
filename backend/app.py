from flask import Flask, request, jsonify
from database import Notesdatabase
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config["JWT_SECRET_KEY"] = "b00281554a38997dfeb0727bda740f49ff09c4d7b41bd60ffc894403394b8c64" 
jwt = JWTManager(app)
@app.get('/')
def home():
    return 'Hello, Flask is!'


@app.post('/login')
def login():
    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')
    # password = bcrypt.generate_password_hash(request_data.get('password')).decode('utf-8')
    db = Notesdatabase()
    result = db.login_user(username)
    if result is None:
        return jsonify({
            "message":"User Does Not Exist"
        })
    user_password = result.get('userpassword')
    is_valid = bcrypt.check_password_hash(user_password,password )
    if not is_valid:
        return jsonify({
            "message":"Wrong Password"
        })
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
    

@app.post('/add_user')
@jwt_required()
def add_user():
    request_data = request.get_json()
    username = request_data.get('username')
    # password = request_data.get('password')
    password = bcrypt.generate_password_hash(request_data.get('password')).decode('utf-8')
    db = Notesdatabase()
    result = db.add_user(username,password)
    return result

#query params
@app.get('/get_user')
@jwt_required()
def get_user():
    username = request.args.get('username')  
    if not username:
        return jsonify({
            "message": "Username query parameter is required",
            "result": "error"
        }), 400
    print(username)
    db = Notesdatabase()
    result = db.get_user(username)
    return result
    


@app.post('/add_note')
@jwt_required()
def add_note():
    request_data = request.get_json()
    username = request_data.get('username')
    note = request_data.get('note')
    db = Notesdatabase()
    db.add_note(username,note)
    return {"result": "Note added successfully"}


@app.get('/get_notes')
@jwt_required()
def get_notes():
    username = request.args.get('username')
    print(username)
    # return {"result": username}
    db = Notesdatabase()
    res = db.get_notes(username)
    return {
        "result": res
    }





if __name__ == '__main__':
    app.run(debug=True)



