import os
import os.path
import sys
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
import json
import logging
from random import randint

app = Flask(__name__)

@app.route("/", methods=['POST'])
def main_page():

	speech = ["H.R.861 To terminate the Enviornmental Protection Agency.","S.2266 H1B and L1 Visa Reform Act of 2015.","H.R.285 Healthcare Tax Relief and Mandate Repeal Act."]
	 
	speechTosend =speech[randint(0,2)] 

	req = {
			"speech": speechTosend,
			"displayText": speechTosend,
			"data": {"speech": speechTosend},
		}
		
	req = json.dumps(req, indent=4)
	r = make_response(req)
	r.headers['Content-Type'] = 'application/json'
	return r