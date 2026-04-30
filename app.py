import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_default_key_12345')

# Initialize SocketIO with eventlet for better concurrency
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory user database (resets on server restart)
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            # Authenticate existing user
            if check_password_hash(users[username]['password'], password):
                session['username'] = username
                return redirect(url_for('chat'))
            else:
                return "Invalid password", 401
        else:
            # Register new user automatically
            users[username] = {
                'password': generate_password_hash(password),
            }
            session['username'] = username
            return redirect(url_for('chat'))

    return render_template('login.html')

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', username=session['username'])

# --- Socket.io Event Handlers ---

@socketio.on('join')
def on_join(data):
    username = data.get('username')
    room = data.get('room', 'General')
    join_room(room)
    send(f"{username} has joined the room: {room}", to=room)

@socketio.on('leave')
def on_leave(data):
    username = data.get('username')
    room = data.get('room', 'General')
    leave_room(room)
    send(f"{username} has left the room.", to=room)

@socketio.on('message')
def handle_message(data):
    room = data.get('room', 'General')
    message = data.get('message')
    username = data.get('username')
    # Broadcast message to everyone in the room
    send(f"{username}: {message}", to=room)

if __name__ == '__main__':
    # Use socketio.run instead of app.run to enable WebSocket support
    socketio.run(app, debug=True, port=5000)
