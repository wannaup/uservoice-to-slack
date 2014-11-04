from flask import Flask
from flask import render_template
from flask import request, session, redirect, url_for,abort, Response, current_app, make_response
import json
import requests
import os

app = Flask(__name__)

@app.route('/notifyslack/<key>', methods=['POST'])
def notifyslack(key):
    if key != os.environ.get('MY_KEY'):
        abort(404)
    slackurl = os.environ.get('SLACK_URL')
    payload = {'text': 'Just received a new support request or user reply for WURE, go to <http://wure.uservoice.com/admin|Uservoice> to see it.'}
    r = requests.post(slackurl, data=json.dumps(payload))
    if r.status_code != requests.codes.ok:
        return '***ERROR: error posting to #SLACK, sorry :('
    else:
        return 'Posted to #SLACK OK'