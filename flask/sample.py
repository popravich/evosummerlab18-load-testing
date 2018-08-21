import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/huge-json")
def huge_json():
    return json.dumps(list(range(10**5)))
