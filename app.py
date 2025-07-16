from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

ip_local = "127.0.0.1"

@app.route('/')
def index():
    return render_template('index.html', ip_local=ip_local)

@app.route('/change_video/<filename>')
def change_video(filename):
    socketio.emit('video', {'filename': filename})
    return 'Video changed'

@app.route('/speak/<text>')
def speak(text):
    socketio.emit('speak', {'text': text})
    return 'Text spoken'

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, allow_unsafe_werkzeug=True)