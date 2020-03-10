from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'OK'

@socketio.on('connect')
def connect():
    print('New connection')

@socketio.on('message')
def message(message):
    print(message)
    print(request.sid)
    

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)

