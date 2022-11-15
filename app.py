import flask
import random

app = flask.Flask(__name__)

possible_images = [
    "/static/shrek-roar.gif",
    "/static/donkey-annoy.gif",
    "/static/pinocchio-ginger-bread.gif",
]


@app.route("/")
def index():
    return flask.render_template(
        "index.html",
    )


@app.route("/swamp")
def swamp():
    return flask.render_template("swamp.html")


@app.route("/first")
def first():
    return flask.render_template("first.html")


@app.route("/second")
def second():
    img = random.choice(possible_images)
    return flask.render_template(
        "second.html",
        spooky_image=img,
    )


app.run()
