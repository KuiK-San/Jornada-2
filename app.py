from flask import Flask, render_template, url_for,redirect, jsonify
from flask_socketio import SocketIO
import pymongo
from bson import ObjectId


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

apertos = 0

@app.route('/atualizar', methods=['POST'])
def att():

    global apertos
    apertos += 1

    if apertos == 1:
        colecao.update_one({'_id': ObjectId('655d65c65c59a012d616b184')}, {'$set': {"operador": "Guilherme Casagrande", "indexAtual": 5}})
    elif apertos == 2:
        colecao.update_one({'_id': ObjectId('655ec7fb93f6fa1d68f436ce')}, {'$set': {"indexAtual": 0}})
    elif apertos == 3:
        colecao.update_one({'_id': ObjectId('655ec7fb93f6fa1d68f436ce')}, {'$set': {"operador": "João Texeira", "indexAtual": 1}})
    elif apertos == 4:
        colecao.update_one({'_id': ObjectId('655ec7fb93f6fa1d68f436ce')}, {'$set': {"operador": "Noah", "indexAtual": 2}})
        apertos = 0

    socketio.emit('atualizacao', 'Att')

    return redirect(url_for('btn'))

@app.route('/reset', methods=['POST'])
def marcelo():
    global apertos
    apertos = 0

    colecao.update_one({'_id': ObjectId('655d65c65c59a012d616b184')}, {'$set': {"ordemProd": "XXXXXXX",
    "operador": "João Texeira",
    "modelo": "ONIX/PN9855342",
    "processos": [
        "Corte",
        "Limpeza",
        "Moldagem",
        "Solda",
        "Descascar",
        "Lixamento Int.",
        "Polimento Int.",
        "Lixamento Ext."
    ],
    "indexAtual": 4,
    "tempoInicio": ""}})

    colecao.update_one({'_id': ObjectId('655ec7fb93f6fa1d68f436ce')}, {'$set': {"ordemProd": "XXXXXXX",
    "operador": "João Texeira",
    "modelo": "ONIX/PN9855342",
    "processos": [
        "Corte",
        "Limpeza",
        "Moldagem",
        "Solda",
        "Descascar",
        "Lixamento Int.",
        "Polimento Int.",
        "Lixamento Ext."
    ],
    "indexAtual": -1,
    "tempoInicio": ""}})
    
    socketio.emit('atualizacao', 'Att')

    return redirect(url_for('btn'))

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)