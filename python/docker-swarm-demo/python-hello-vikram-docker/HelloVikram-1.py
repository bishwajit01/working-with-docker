from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def printHelloVikram(name):
    print("+++++++++++++++++++++")
    print("+   HELLO VIKRAM-1  +")
    print("+++++++++++++++++++++")
    return '<h1>Hello-Vikram :: ' + name + '</h1>'

@app.route("/public/v1/healthcheck")
def healthCheck():
    return "OK"

if __name__ == '__main__':
    app.run(debug='true', port='4444', host='0.0.0.0')
    printHelloVikram();