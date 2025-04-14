from flask import Flask, request
from database import Notesdatabase
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.get('/')
def home():
    return 'Hello, Flask is!'

@app.post('/add_note')
def add_note():
    request_data = request.get_json()
    username = request_data.get('username')
    note = request_data.get('note')
    db = Notesdatabase()
    db.add_note(username,note)
    return {"result": "Note added successfully"}



if __name__ == '__main__':
    app.run(debug=True)



