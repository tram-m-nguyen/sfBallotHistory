# Create flask application

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

# render_template - jinja looks like html, but we use a library to get 
# data and apply

# this is how Flask app needs to know what module to scan for for things 
# like routes the __name__ is required and must be written like this
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# in order to use the debugger
debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """Shows ballot search form.
    Initially - will render ballots form 1961 
    So has to make an api request to render """

    return render_template("search-form.html")

    


#