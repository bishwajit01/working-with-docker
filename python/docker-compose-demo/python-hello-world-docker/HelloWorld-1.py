from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def printHelloWorld(name):
    print("+++++++++++++++++++++")
    print("+   HELLO WORLD-1   +")
    print("+++++++++++++++++++++")
    return '<h1>Hello-World :: ' + name + '</h1>'
    # return '<h1>Hello %s!<h1>' %name

@app.route("/public/v1/healthcheck")
def healthCheck():
    return "OK"

if __name__ == '__main__':
    app.run(debug='true', port='5555', host='0.0.0.0')
    printHelloWorld();

# printHelloWorld()