from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'OK'

@socketio.on('connect')
def connect():
    warn = 'OK'
    send(warn)
    emit('receive', 'Recebdo')
    print('New connection')

@socketio.on('mesg')
def handle_return(message1, message2):
    print(message1)
    print(message2)
    #print(request.sid)

@socketio.on('my message')
def message(data):
    print(request.sid)
    print(data)
    emit('reply', "emitreturn")
    pass



#socketio.on_event('my event', my_function_handler, namespace='/')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)

