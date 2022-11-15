import flask
import random

app = flask.Flask(__name__)

# possible_images = [
#     "/static/farquaad.gif",
#     "/static/donkey-smile.gif",
#     "/static/pinocchio-ginger-bread.gif",
# ]


@app.route("/")
def index():
    # img = random.choice(possible_images)
    return flask.render_template(
        "index.html",
        # spooky_image=img,
    )


@app.route("/swamp")
def swamp():
    return flask.render_template("swamp.html")


@app.route("/first")
def first():
    return flask.render_template("first.html")


app.run()
