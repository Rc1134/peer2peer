# Peer-2-Peer
## Description
Peer-2-Peer is a web-based platform designed to assist college students in their placement journey by offering a collaborative environment. 
It enables students to share resources, participate in discussions, and prepare for interviews through peer support and real-time collaboration.
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- ## Features
- User authentication (registration, login, and profile management)
- Resource sharing (notes, articles, interview tips)
- Real-time collaboration via discussion forums
- Peer mentorship system
- Track placement-related events
- User profiles with achievements and skills
- ## Tech Stack
- **Backend**: Django
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite3
- **Rich Text Editing**: CKEditor
- ## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/peer-2-peer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd peer-2-peer
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

7. Open the app in your browser at `http://127.0.0.1:8000/`.
