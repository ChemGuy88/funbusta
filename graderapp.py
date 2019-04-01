#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Project Name
------------

    funbusta

File name
---------

    grader.py

File Description
----------------

    For API calls see
        http://api-explorer.khanacademy.org

    Khan Academy API keys for FunBuSta Grader app

    App name:           ???
    Consumer Key:       8hBQx2rmajKxGZJt # Doesn't work?
    Consumer Secret:	GPNfJa6q7gYZTP4C

    App name:           Funbusta Grader
    Consumer Key:       JqTcQjbh9NncCBJy
    Consumer Secret:	BwHpLJHydvhSqHtJ

'''

import os, sys
from flask import Flask

dir = os.getcwd()
os.chdir('/Users/Herman/Documents/funbusta/khan-api/examples/flask_test_client/')
import khan_api
from khan_api import *
os.chdir(dir)

'''
################################################################################
##### Boilerplate? #############################################################
################################################################################
'''

app = Flask(__name__)

'''
################################################################################
##### Global Variables #########################################################
################################################################################
'''

CONSUMER_KEY = "8hBQx2rmajKxGZJt"
CONSUMER_SECRET = "GPNfJa6q7gYZTP4C"
DIR = '/Users/Herman/Documents/funbusta/'

'''
################################################################################
##### Functions ################################################################
################################################################################
'''

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/pie')
def pie():
    return "Hello Cake!"

@app.route('/done')
def done():
    return 'You\'re done!'

@app.route('/test')
def test():
    kapi = KhanAPI(CONSUMER_KEY, CONSUMER_SECRET)
    return access_token, access_token_secret
    # return kapi.user()

# 1. An authorize endpoint, like @app.route('/authorize'), where you will
#    instantiate the class and call the authorize method. i.e:
@app.route('/authorize')
def authorize():
    oauth = KhanAcademySignIn()
    return oauth.authorize()

# 2. A callback endpoint that you can use to store your token and secret:
@app.route("/oauth_callback")
def oauth_callback():
    oauth = KhanAcademySignIn()
    ka_user, access_token, access_token_secret = oauth.callback()
    ## Developer created function to store the tokens ##
    # set_access_tokens(access_token, access_token_secret) # I don't think this is a real function
    with open(DIR+'apptokens.txt', 'w') as f:
        l = [access_token, access_token_secret]
        f.writelines('\n'.join(l))
    # return redirect(url_for("done"))
    return redirect(url_for("test"))

if __name__ == '__main__':
    app.secret_key = CONSUMER_KEY
    app.config['SESSION_TYPE'] = 'filesystem'

    # sess.init_app(app)

    app.debug = True
    app.env = ''
    app.run()
