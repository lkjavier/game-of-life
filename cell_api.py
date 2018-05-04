from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit
import json
from CellGrid import CellGrid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET','POST'])
def start():
    if request.method == 'GET':
        grid = CellGrid()
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
    print(json.dumps(message))
    emit('Response', [['Response']])
    #pass

if __name__ == '__main__':
    socketio.run(app)