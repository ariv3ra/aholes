from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    #need to setup index page
    return "Hello World!"

@app.route("/validate", methods=['POST'])
def validate():
    #get the domain

    #check the domain against the getdns stack
    status = "status"
    request.json[status] = 'ok'
    return jsonify(request.json)

if __name__ == "__main__":
    app.debug = True 
    app.run(host='0.0.0.0')