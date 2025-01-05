from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secret key of your choice
socketio = SocketIO(app)

# In-memory user database for simplicity (use SQLite or PostgreSQL in production)
users = {}

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for user login/registration
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            # Authenticate user
            if check_password_hash(users[username]['password'], password):
                session['username'] = username
                return redirect(url_for('chat'))
            else:
                return "Invalid password"
        else:
            # Register user
            users[username] = {
                'password': generate_password_hash(password),
            }
            session['username'] = username
            return redirect(url_for('chat'))

    return render_template('login.html')

# Route for chat page
@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', username=session['username'])

# Handle joining a chat room
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f"{username} has joined the room.", to=room)

# Handle leaving a chat room
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f"{username} has left the room.", to=room)

# Handle sending a message
@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    username = data['username']
    send(f"{username}: {message}", to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
