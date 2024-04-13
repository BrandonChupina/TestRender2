from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Prueba de datos en render..."

if __name__ == '__main__':
    app.run(debug=True)
