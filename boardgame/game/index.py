from flask import render_template, Flask, jsonify
from game import app
from utils import 


@app.route("/", method = ['POST'])

def home():
    cates = utils.load_()

    return  render_template('index.html')

def player_number():
    data = request.get_json()
    numPlayers = float
    




if _name_ == '_main_'
    app.run(debug=True)
