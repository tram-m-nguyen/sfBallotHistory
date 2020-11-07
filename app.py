# Creates flask application

from flask import Flask, request, render_template, jsonify
import requests
from forms import searchForm
from ballots import get_ballots


from flask_debugtoolbar import DebugToolbarExtension

# this is how Flask app needs to know what module to scan for for things 
# like routes the __name__ is required and must be written like this
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# in order to use the debugger
debug = DebugToolbarExtension(app)


@app.route("/")
def show_search_form():
    """Shows ballot search form.
    Initially - will render all ballots for 1962 to render. """

    ballots_1961 = get_ballots(year=1982)
    print('this is ballots_1961', len(ballots_1961))

    return render_template("search-form.html", ballots_1961=ballots_1961)



#handles the form submission
@app.route("/search", methods=['GET', 'POST'])
def show_result():
    """Handles the form submssion"""

    #call it here because 
    form = searchForm()

    if form.validate_on_submit():
        year = form.year.data
        month = form.month.data
        subject = form.subject.data
        type_of_measure = form.type_of_measure.data
        measure_placed_by = form.measure_placed_by.data
        pass_or_fail = form.pass_or_fail.data
        keyword = form.keyword.data

        print('year input,', year)

        #flash(f"searching for your query")

        return redirect("/")
    else:
        # do something

        return render_template("search-form.html")
        




    


