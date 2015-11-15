from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS

application = Flask(__name__)
CORS(application)

@application.route("/")
def index():
    #need to setup index page
    return "Hello World!"

@application.route("/validate", methods=['POST'])
def validate():
    #get the domain

    #check the domain against the getdns stack
    status = "status"
    request.json[status] = 'ok'
    return jsonify(request.json)

if __name__ == "__main__":
    application.debug = True 
    application.run(host='0.0.0.0')
