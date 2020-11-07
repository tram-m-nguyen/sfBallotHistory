# Create flask application

from flask import Flask, request, render_template

from flask_debugtoolbar import DebugToolbarExtension
#import searchForm
from forms import searchForm
searchForm
#from project_secret import API_SECRET_KEY


# render_template - jinja looks like html, but we use a library to get 
# data and apply

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
    Initially - will render ballots on 1962 to render."
    o has to make an api request to render. """

    # automaticall load ballots for 1961 - this only happens onces

    # show the form 
    print("this will show in the console, where does this show")

    return render_template("search-form.html")

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

        flash(f"searching for your query")

        return redirect("/")
    else:
        # do something

        return render_template("search-form.html")
        




    


