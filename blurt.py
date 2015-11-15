from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS
import tweepy
import pythonwhois

auth = tweepy.OAuthHandler()
auth.set_access_token()

api = tweepy.API(auth)


# api.update_status(status="Here we go again @pullova1 @tangydoris @twrivera")

# print api.me()

# tint = api.get_user(@amazon)

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
    
    # get domain
    dom = request.json['domain']
    who = pythonwhois.get_whois(dom)
	org = who['contacts']['registrant']['organization'])
	


    return jsonify(request.json)

@application.route("/task", methods=['POST'])
def task():


if __name__ == "__main__":
    application.debug = True 
    application.run(host='0.0.0.0')
