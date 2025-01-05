// Script for the login page
document.getElementById('loginBtn').addEventListener('click', function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (username && password) {
        window.location.href = `/chat/${username}`;
    } else {
        alert('Please enter both username and password.');
    }
});

// Script for the chat page
const socket = io();

// Display username on the chat page
const username = window.location.pathname.split('/').pop();
document.getElementById('usernameDisplay').textContent = username;

// Sending a message
document.getElementById('sendBtn').addEventListener('click', function() {
    const message = document.getElementById('messageInput').value;
    if (message) {
        socket.emit('chat message', { username: username, message: message });
        document.getElementById('messageInput').value = ''; // clear input field
    }
});

// Displaying received messages
socket.on('chat message', function(data) {
    const messagesContainer = document.getElementById('messages');
    const messageElem = document.createElement('p');
    messageElem.textContent = `${data.username}: ${data.message}`;
    messagesContainer.appendChild(messageElem);
});
