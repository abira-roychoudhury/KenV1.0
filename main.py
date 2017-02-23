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

	speech = [unicode("H.R.861 : To terminate the Environmental Protection Agency.", "utf-8"),unicode("S.2266 : H:1B and L:1 Visa Reform Act of 2015", "utf-8"),unicode("H.R.285 : Healthcare Tax Relief and Mandate Repeal Act", "utf-8")]
	 
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