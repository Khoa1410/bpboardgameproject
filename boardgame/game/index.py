from flask import render_template
from game import app
from utils import 


@app.route("/")

def home():
    cates = utils.load_()

    return  render_template('index.html')




if _name_ == '_main_'
    app.run(debug=True)
