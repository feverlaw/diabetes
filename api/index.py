from flask import flask

app=Flask(__name__)

@app.route('/')
def home():
  return  "Hello world"

@app.route('/about')
def about():
  return  'About'
