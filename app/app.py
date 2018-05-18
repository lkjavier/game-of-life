from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit, join_room
import json
from CellGrid import CellGrid
from refactor import GridGame

import logging 
logging.basicConfig(filename='error.log',level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
GAMES = {}

@app.route('/', methods=['GET','POST'])
def start():
    if request.method == 'GET':
        grid = CellGrid(state = None, size = 30)
    else:
        grid = CellGrid(request.data)
        grid.advance() 
    return render_template('index.html', state=grid.state)

@app.route('/advance', methods=['POST'])
def advance():
    grid = CellGrid(request.data)
    grid.advance()
    return grid.get_json_state()

@socketio.on('Call')
def handle_message(message):
    print("Messagetype: {}, message:{}".format(type(message), message))
    print(len(json.loads(message)))

    grid = CellGrid(json.loads(message))
    grid.advance()
    emit('Response', grid.get_json_state())
    #pass

@socketio.on('Randomize')
def handle_message(message):
    grid = CellGrid(json.loads(message))
    grid.randomize()
    emit('Response', grid.get_json_state())
    #pass

@app.route('/cell/<rule>', methods=['GET'])
def create_cell(rule):
    app.logger.info('%s size args', request.args.get('size', default = 30, type = int))
    g = GridGame(size = request.args.get('size', default = 30, type = int))
    # we should save this in a table and get a unique id for this game based on
    # ruletype, size, rule_params, initial_state
    GAMES["test"] = g
    return render_template('index.html', state=g.cellGrid.state)

@socketio.on('start')
def handle_message(message):
    g = GAMES["test"]
    join_room("test")
    g.start(socketio)

if __name__ == '__main__':
    socketio.run(app)