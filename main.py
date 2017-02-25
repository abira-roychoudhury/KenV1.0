import os
import os.path
import sys
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
import json
import logging
import actions
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def main_page():

	logging.info("inside POST")
	req = request.get_json(silent=True, force=True)

	logging.info(type(req) )
	logging.info(req)

	parameters = req['result']['parameters']
	action = req['result']['action']
	
	# Reading the access token now
	access_token = req['originalRequest']['data']['user']['access_token']
	logging.info(access_token)

	profile_json = requests.get("https://graph.facebook.com/me?fields=id,name,email,about,birthday,education,hometown,likes,location,relationship_status,family&access_token="+access_token)
	logging.info(profile_json.json())

	speechTosend = actions.handler[action](parameters)

	req = {
			"speech": speechTosend["response"],
			"displayText": speechTosend["response"],
			"data": {"speech": speechTosend["response"]},
			"contextOut": speechTosend["contextOut"]
		}
		
	req = json.dumps(req, indent=4)
	r = make_response(req)
	r.headers['Content-Type'] = 'application/json'
	return r
