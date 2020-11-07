# Create flask application

from flask import Flask, request, render_template, jsonify
import requests
#import searchForm
from forms import searchForm
from project_secret import API_SECRET_KEY

#from flask_debugtoolbar import DebugToolbarExtension

# this is how Flask app needs to know what module to scan for for things 
# like routes the __name__ is required and must be written like this
app = Flask(__name__)
#app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# in order to use the debugger
#debug = DebugToolbarExtension(app)

def get_ballots(year=None, month=None, subject=None, pass_or_fail=None, 
                type_measure=None, by=None, keyword1=None, keyword2=None,
                keyword3=None, keyword4=None, keyword5=None):
    """
    Fetch ballot data from SF API.
    Query strings: month, year, subject, pass_or_fail, type_measure, 
                by (measure_placed_by in forms.py), keyword.
    
    Year is the only Integer, the rest of the parameters are strings.

    year: Integer
    month: abbreviated months
    subject: contains more than one word, each word will be Camel case.
    pass_or_fail: must be in P or F
    type_of_measure: max 2 capital letter. Indicates the type of measure.
    by (measure_placed_by in forms.py): max 2 capital letter. 
        --by indicates how the how the measure was placed on the ballot
    
    keyword: must be Camel case. API takes specific keyword1, keyword2, keyword3,
    keyword4, keyword5. Will make an api call with 1 word provided and feed into
    all the different keywords.
    """

    api_url = "https://data.sfgov.org/resource/xzie-ixjw.json?"

    resp = requests.get(
        api_url,
        params={"$$app_token": API_SECRET_KEY, 
                "year": year, 
                "month": month, 
                "subject": subject, 
                "pass_or_fail": pass_or_fail,
                "type_measure": type_measure,
                "by": by,
                "Keyword1": keyword1,
                "Keyword1": keyword2,
                "Keyword1": keyword3,
                "Keyword1": keyword4,
                "Keyword1": keyword5,
                })


    print ('API RESPONSE', resp.json())

    return resp.json()



@app.route("/")
def show_search_form():
    """Shows ballot search form.
    Initially - will render ballots on 1962 to render."
    o has to make an api request to render. """

    # make api call to load ballots for 1961 
    ballots_1961 = get_ballots(1961)

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
        




    


