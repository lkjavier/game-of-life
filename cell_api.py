from flask import Flask
from flask import request
from CellGrid import CellGrid

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def advance_state():
    if request.method == 'GET':
        grid = CellGrid()
        return grid.get_json_state()
    else:
        grid = CellGrid(request.data)
        grid.advance()
        return grid.get_json_state()