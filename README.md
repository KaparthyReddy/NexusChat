# 🌌 NexusChat

**NexusChat** is a sophisticated, real-time messaging environment designed for privacy, speed, and modern aesthetics. Moving beyond simple chat, Nexus provides a synchronized "stream" experience with a sleek, dark-mode interface optimized for both desktop and mobile.

![License](https://img.shields.io/badge/Status-Live-brightgreen)
![Python](https://img.shields.io/badge/Backend-Python_3.14-blue)
![SocketIO](https://img.shields.io/badge/Real--Time-Socket.io-orange)

## ✨ Core Features
* **Instant Synchronization:** Zero-latency messaging powered by Flask-SocketIO and Gevent.
* **Nexus Aesthetics:** A custom-engineered "Glassmorphism" UI featuring a deep-space color palette and responsive layouts.
* **Isolated Streams (Rooms):** Create or join specific channels for private, focused collaboration.
* **Ephemeral Security:** In-memory user authentication ensures your data doesn't live on a permanent server footprint.
* **Adaptive Port Configuration:** Optimized for deployment on high-traffic ports (8080) to avoid system conflicts.

## 🛠 Tech Stack
* **Frontend:** Modern HTML5, CSS3 (Custom Glassmorphism), and Vanilla JS.
* **Backend:** Flask (Python 3.14).
* **Communication:** WebSocket (Socket.io) for bi-directional live updates.
* **Deployment:** Gevent WSGI server for production-grade stability.

## 🚀 Quick Start
1. **Clone & Enter:**
   ```bash
   git clone https://github.com/KaparthyReddy/NexusChat.git
   cd NexusChat
   

2. **Initialize Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   

3. **Launch the Engine:**
   ```bash
   python3 app.py
   
4. Access the interface at \`http://localhost:8080`\.

## 📜 Roadmap
- [x] Multi-room Support
- [x] Dark Mode Overhaul
- [x] Port Conflict Resolution
- [ ] SQLite Persistent Storage
- [ ] File & Image Uploads
