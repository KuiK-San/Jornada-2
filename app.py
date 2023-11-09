from flask import Flask, render_template, url_for,redirect
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/btn', methods=['GET'])
def btn():
    return render_template('button.html')

@app.route('/atualizar', methods=['POST'])
def att():
    socketio.emit('atualizacao', 'Att')

    return redirect(url_for('btn'))

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)