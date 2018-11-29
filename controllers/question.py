from app import app
from flask import render_template, request
from helpers import GENRES_LIST
from helpers import get_score

@app.route('/question', methods=["POST"])
def question():

    data = {
        "songs": get_four_songs(request)
    }

    return render_template("question.html", **data)
