from flask import Flask , render_template
from flask_socketio import SocketIO, emit
from DateTime import DateTime


app = Flask(__name__, template_folder='templates')

number_of_clients = 0

socketio = SocketIO(app)




@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connection():
    print("connected")
    emit('log',{'data':'Lets dance'})
    increment_number_of_clients()

@socketio.on('disconnect')
def test_connection():
    print("disconnected")
    decrement_number_of_clients()


@socketio.on('client count')
def get_client_count(data):
    global number_of_clients
    print("client count is",  number_of_clients)
    emit('client count is', {'data':  number_of_clients})


@socketio.on('server time')
def get_server_time(data):
    current_server_time = DateTime().millis()
    emit('server time is', {'data':current_server_time})


def increment_number_of_clients():
    global number_of_clients
    number_of_clients = number_of_clients + 1

def decrement_number_of_clients():
    global number_of_clients
    number_of_clients = number_of_clients - 1







if __name__ == '__main__':
    socketio.run(app, debug = True)