from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS
from pytodoist import todoist
import tweepy
import pythonwhois


auth = tweepy.OAuthHandler("BcTy74pCRD7EEqyLbEDqVKWpo", "Yw1GUFiuutADvmXV3y4dyUrCDCCzfLNanAOpT6zX4tkIJmivnt")
auth.set_access_token("4241783113-klDOBGvDjaiiOKUEnhJKqvIOv5FrT8O0QpnylMA", "evKFU6VCHWJf99ygD436NICBmJAb2sH6XqStSfhw4pfHn")

api = tweepy.API(auth)
# user = todoist.login('mfeineis@point.io', 'testtree23')

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
    org = who['contacts']['registrant']['organization']
	
    # user.add_project(dom, color=todoist.Color.RED)
    
    twt = "Hey #" + org + " we detected that your DNSSEC sucks. Fix it here"
    api.update_status(status=twt)

    return jsonify(request.json)

@application.route("/task", methods=['POST'])
def task():
    pass

if __name__ == "__main__":
    application.debug = True 
    application.run(host='0.0.0.0')
