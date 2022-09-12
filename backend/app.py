from flask import Flask
from mongo_db import get_random_like_from_db

app = Flask(__name__)


@app.route("/random-like")
def get_random_like():
    return get_random_like_from_db()
