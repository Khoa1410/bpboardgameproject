from data.players_name import randchoice
from flask import Flask, jsonify, request, render_template
from data.data import nameList, event

app = Flask(__name__)

@app.route('/')

def get_templates():
    return render_template("index.html")

@app.route("/Random-Player", methods=["POST"])
def random_data():
    chosen_name = randchoice(nameList)
    chosen_event = randchoice(event)    
    return jsonify({"namevalue": f"chosen_name"})

if __name__ == '__main__':
    app.run(debug = True)
