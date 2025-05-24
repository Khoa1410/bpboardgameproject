from flask import Flask, redirect, url_for, render_template
import random

app = Flask(__name__)
@app.route('/', method = ['POST'])

def player_number():
    data = request.get_json()
    numPlayers = float(data.get('numPlayers', 0))
    PlayerName = data.get('players', [])
    DePlayer = random.choice(PlayerName)
    return jsonify({'DePlayer':DePlayer})






        






