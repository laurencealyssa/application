from flask import Flask
app = Flas(__name__)

@app.route('/')
def index():
  return 'Hello, Welcome to the sample deployment of Alyssa Laurence from Heroku'
