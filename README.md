# game-of-life
Playground for building out some ideas on Cellular Automata

1. Game Of Life
- Starting with a 'naive' implementation of Conway's Game Of Life
2. API
- An api will provide access to the functionality 
3. Notebook
- Contains a Jupyter notebook for some doodling
4. Requirements
- Flask

## Virtual Environment
```
virtualenv -p python3 venv 
source venv/bin/activate
pip install -r app/requirements.txt
```  

## Docker
```
docker build -t gameoflife .
docker run -p 80:80 gameoflife
```  
