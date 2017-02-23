import os
import os.path
import sys
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
import json
import logging
import actions

app = Flask(__name__)

@app.route("/", methods=['POST'])
def main_page():

	logging.info("inside POST")
	req = request.get_json(silent=True, force=True)

	logging.info(type(req) )
	logging.info(req)

	parameters = req['result']['parameters']
	action = req['result']['action']

	speechTosend = actions.handler[action](parameters)

	req = {
			"speech": speechTosend,
			"displayText": speechTosend,
			"data": {"speech": speechTosend},
		}
		
	req = json.dumps(req, indent=4)
	r = make_response(req)
	r.headers['Content-Type'] = 'application/json'
	return r