from flask import Flask, request, redirect, render_template
import requests
from ballots import get_ballots_for_queries
from models import db, connect_db, BallotSearch, BallotsFromMainDB
from forms import searchForm
from helpers import yes_votes, no_votes, display_vote_percents


from flask_debugtoolbar import DebugToolbarExtension

# Creates flask application
# this is how Flask app needs to know what module to scan for things 
# like routes the __name__ is required & must be written as such
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# where is the db, what to connect to; whether to track table, have sql written
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///ballot_history'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# To use debugger
debug = DebugToolbarExtension(app)

#connect to db
connect_db(app)


@app.route("/")
def homepage():
    """ Shows ballot search form.
    Initially - will render all ballots from 1907 from the database. 
    
    Searches from 1961-2010, results will be from API to sf data.
    Searches 1907-1960 and 2011-March 2020 will be from database."""

    # total ballots 1907-2020
    total_ballots = BallotsFromMainDB.query.count()

    form = searchForm()

    # get all ballots from 1907 in the db and return array of objects.
    ballots_1907 = BallotsFromMainDB.query.filter_by(year = 1915) 
    year = 1915

    
    return render_template("index.html", ballots=ballots_1907, year=year,
                                        total_ballots=total_ballots, 
                                        form=form, yes_votes=yes_votes, 
                                        no_votes=no_votes,
                                        display_vote_percents=display_vote_percents)

# logic for form:
# if year is provided and it's between 1961-2000
# then make API call 

# create an api to store search data in database
@app.route("/search", methods=['POST'])
def create_ballotsearch():
    """Add search query, make an api request for 1961, and return data about all
    ballots in 1961.
    
    Return JSON: { ballots: [ {}, {}, {}, {}, {}, {}, {}, {}, {}, {
                                month, year, letter, subject, yes_votes, 
                                no_votes, pass_or_fail, percent, type_measure, 
                                by, keywork1, keyword2, keyword3, keyword4 or 
                                keyword5}]}"""


    #get data from the front end as through request.json
    #create a new ballotsearch instance
    #add instance into database
    #commit to database 

    #serialized the new cupcake

    return 'should return jsonify'
    





# Adde handles the form submission
# @app.route("/api/search-ballots1", methods=['POST'])
# def get_ballots():
#     """
#     Get search queries from frontend, validate all inputs and return info about 
#     query. Then add search inputs into db, and return data about the search.
    
#     Returns JSON like:
#         { searchInput: 
#             {month, year, subject, pass_or_fail, type_measure, by, keyword} }
#     """

#     # get data from the form
#     inputs_received = request.json
#     print('this is inputs_received', inputs_received)

#     # create instance of search
#     ballotSearch = BallotSearch(
#         year = inputs_received["year"]
#         month = inputs_received["month"]
#         subject = inputs_received["subject"]
#         type_of_measure = inputs_received["type_of_measure"]
#         measure_placed_by = inputs_received["measure_placed_by"]
#         pass_or_fail = inputs_received["pass_or_fail"]
#         keyword = inputs_received["keyword"]
#     )

#     # add it to the database
#     db.session.add(ballotSearch)
#     db.session.commit()

#     return jsonify(ballotSearch=ballotSearch.to_dict()), 201)

    
        

# Adde handles the form submission
# @app.route("/search-ballots", methods=['GET', 'POST'])
# def get_ballots():
#     """ Get data from the front end. Input into db, redirect, and return html."""
#     print('this is get_ballotsget_ballotsget_ballotsget_ballots') 
    
#     #get data from the form
#     inputs_received = request.json
#     print('this is inputs_received', inputs_received)

#     #
#     form = searchForm(data=inputs_received)
#     print("DATATATATATATAT", inputs_received)

#     # this is get request, so don't need to validate all inputs, just to take 
#     # error and send to front end
#     # if post, request, then all inputs must be validated and redirect !!
#     # get back data fr form, feed it to the get_ballots and get a json because
#     # that functions gives you a json 
#     if form.validate_on_submit():
#         print("validate_on_submitvalidate_on_submitvalidate_on_submit", inputs_received)
#         year = inputs_received["year"]
#         # month = inputs_received["month"]
#         # subject = inputs_received["subject"]
#         # type_of_measure = inputs_received["type_of_measure"]
#         # measure_placed_by = inputs_received["measure_placed_by"]
#         # pass_or_fail = inputs_received["pass_or_fail"]
#         # keyword = inputs_received["keyword"]

#         print('year input,', year)

#         ballots = get_ballots_for_queries( year=year, 
#                             # month=month, 
#                             # subject=subject, 
#                             # type_of_measure=type_of_measure,
#                             # by=measure_placed_by,
#                             # pass_or_fail=pass_or_fail,
#                             # keyword=keyword
#                             )

#         print('this is ballotsballotsballotsballots', ballots)
#         return jsonify(ballots=ballots)
    
#     else:
#         return jsonify(errors=form.errors)
        




