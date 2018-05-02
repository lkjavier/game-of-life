from flask import Flask
from flask import request
from flask import render_template
from CellGrid import CellGrid

app = Flask(__name__)

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