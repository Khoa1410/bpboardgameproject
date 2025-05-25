from data.players_name import randchoice
from flask import Flask, jsonify, request, render_template
from data.data import randomChoice
from data.chose_player import score_data

app = Flask(__name__)

@app.route('/')

def get_templates():
    return render_template("index.html")

@app.route("/Random-Player", methods=["POST"])
def random_data():
    chosen_name = randomChoice()
    chosen_event = randomChoice()    
    return jsonify({"namevalue": chosen_name,
                    "eventvalue": chosen_event})

@app.route('/game')
def game_page():
    return render_template("game.html")

@app.route("/data-score", method=["POST"])
def score_json():
    score_name = score_data("name")
    score_value = score_data("point")
    return jsonify({"Score_Name": score_name,
                    "Score_Value": score_value})
if __name__ == '__main__':
    app.run(debug = True)

