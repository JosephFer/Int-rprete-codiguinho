from flask import Flask, render_template, request
from src.main import codigo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mi-ruta', methods=['POST'])
def mi_funcion():
    data = request.json
    cod = codigo(data['texto'])
    
    return cod

if __name__ == '__main__':
    app.run(debug=True)
