# app.py for Change4Change
import flask
from flask import Flask, request, url_for, jsonify

import json
import logging

###
# Globals
###
app = flask.Flask(__name__)

import CONFIG


import uuid
app.secret_key = str(uuid.uuid4())
app.debug = CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)
#############
####Pages####
#############

### Home Page ###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('index.html')
    
    
if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug = CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT,threaded=True)9



