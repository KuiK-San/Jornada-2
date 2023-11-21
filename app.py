from flask import Flask, render_template, url_for,redirect, jsonify
from flask_socketio import SocketIO
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['jornadaAprendizagem']
colecao = db['cards']


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods = ['GET'])
def index():
    cards_list = list(colecao.find())
    return render_template('index.html', cards=cards_list)

@app.route('/btn', methods=['GET'])
def btn():
    return render_template('button.html')

@app.route('/atualizar', methods=['POST'])
def att():
    socketio.emit('atualizacao', 'Att')

    return redirect(url_for('btn'))

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)