from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    with open('map.js', 'r') as f:
            
        mapjs = f.read()
        return render_template('fuelmap.html', mapjs=mapjs)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
