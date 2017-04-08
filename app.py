# app.py for Change4Change
import flask
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

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


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404



