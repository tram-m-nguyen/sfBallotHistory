import os

from flask import Flask, request, redirect, render_template, session
import requests
from ballots import get_ballots_for_queries
from models import db, connect_db, BallotSearch, BallotsFromMainDB
from forms import searchForm
from helpers import yesVotes, noVotes, displayVotePercents, isFormEmpty, \
    canTurnIntoInteger, turnStrIntoSqlQuery, removeEmptyValues
import copy
from sqlalchemy import and_
from flask_debugtoolbar import DebugToolbarExtension


SEARCH_INPUTS = 'searchinputs'

# Creates flask application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///ballot_history'))

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     'DATABASE_URL', 'postgres:///flask-heroku')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'shhh')

# this is for staging
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///ballot_history'

# To use debugger
debug = DebugToolbarExtension(app)

#connect to db
connect_db(app)


@app.route("/")
def homepage():
    """ 
    Shows ballot search form.
    
    Initially, will render total ballots since 1907 to 2020, all ballots for that
    year, and total ballots for 1907.
    
    yesVotes, noVotes, displayVotePercents are helper function to ensure proper 
    display.
    """

    # total ballots from 1907-2020
    total_ballots = BallotsFromMainDB.query.count()


    form = searchForm()

    # get all ballots from 1907 from the db and return array of objects.
    year = 1907
    ballots_1907 = BallotsFromMainDB.query.filter_by(year=year) 
    results_total = len(ballots_1907.all())

    return render_template("index.html", ballots=ballots_1907, year=year,
                                        results_total=results_total,
                                        total_ballots=total_ballots, 
                                        form=form, yesVotes=yesVotes, 
                                        noVotes=noVotes,
                                        displayVotePercents=displayVotePercents)


@app.route("/search", methods=['GET','POST'])
def create_ballotsearch():
    """Save search into database.

    Search main db based on form inputs, redirect to "/results" ."""

    form = searchForm()

    if isFormEmpty(form.data):
        return redirect("/")

    if form.validate_on_submit():
        ballot = BallotSearch.add_search(
        month=form.month.data,
        year=form.year.data,
        prop_letter=form.prop_letter.data,
        ballot_subject="" if canTurnIntoInteger(form.ballot_subject.data) else form.ballot_subject.data,
        type_of_measure=form.type_of_measure.data,
        measure_placed_on_ballot_by=form.measure_placed_on_ballot_by.data,
        pass_or_fail=form.pass_or_fail.data,
        )  
        
        db.session.commit()

        # add search inputs into sessions to render results
        session[SEARCH_INPUTS] = {
        "month": ballot.month, 
        "year": ballot.year,
        "prop_letter": ballot.prop_letter, 
        "ballot_subject": ballot.ballot_subject,
        "type_of_measure": ballot.type_of_measure, 
        "measure_placed_on_ballot_by": ballot.measure_placed_on_ballot_by,
        "pass_or_fail": ballot.pass_or_fail
        }
        return redirect("/search/results")


    else:
        return render_template("index.html", form=form)



@app.route("/search/results", methods=['GET', 'POST'])
def searchResult():
    """Get data from form and return the search result.

    yesVotes, noVotes, displayVotePercents are helper function to ensure proper 
    display.
    
    """

    #this is an empty search forms
    form = searchForm()

    search_inputs = session[SEARCH_INPUTS]
    
    # deep copy the search inputs
    search_inputs_copy = copy.deepcopy(search_inputs)
    final_search_inputs = removeEmptyValues(search_inputs_copy)

    # array of filters for SQL    
    filters = []
    for key in list(final_search_inputs.keys()):
        if key == "ballot_subject":
            sql_subject_str = turnStrIntoSqlQuery(final_search_inputs['ballot_subject'])
            expression = (BallotsFromMainDB.ballot_subject.like(f'{sql_subject_str}'))
            filters.append(expression)
        else:
            expression = (getattr(BallotsFromMainDB, key) == final_search_inputs[key])
            filters.append(expression)

    search_results = db.session.query(BallotsFromMainDB).filter(and_(*filters))

    year = final_search_inputs['year'] if "year" in final_search_inputs else ""
    
    results_total = len(search_results.all()) 

    return render_template("result.html", ballots=search_results, year=year,
                                        final_search_inputs=final_search_inputs,
                                        form=form, yesVotes=yesVotes, 
                                        results_total=results_total,
                                        noVotes=noVotes, search_inputs=search_inputs,
                                        displayVotePercents=displayVotePercents)



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
#     search_inputs = request.json
#     print('this is search_inputs', search_inputs)

#     # create instance of search
#     ballotSearch = BallotSearch(
#         year = search_inputs["year"]
#         month = search_inputs["month"]
#         subject = search_inputs["subject"]
#         type_of_measure = search_inputs["type_of_measure"]
#         measure_placed_by = search_inputs["measure_placed_by"]
#         pass_or_fail = search_inputs["pass_or_fail"]
#         keyword = search_inputs["keyword"]
#     )

#     # add it to the database
#     db.session.add(ballotSearch)
#     db.session.commit()

#     return jsonify(ballotSearch=ballotSearch.to_dict()), 201)