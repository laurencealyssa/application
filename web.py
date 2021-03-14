from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, Welcome to the sample deployment of Alyssa Laurence from Heroku'
