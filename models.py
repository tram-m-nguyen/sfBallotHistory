from flask_sqlalchemy import SQLAlchemy
from helpers import canTurnIntoInteger

db = SQLAlchemy()

class BallotSearch(db.Model):
    """
    BallotSearch Table captures for ballot search inputs from the user.
    """
    
    __tablename__ = "ballot_searches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False, default=0)
    month = db.Column(db.Text, nullable=False, default="")
    prop_letter = db.Column(db.Text, nullable=False, default="")
    ballot_subject = db.Column(db.String(200), nullable=False, default="")
    type_of_measure = db.Column(db.String(200), nullable=False, default="")
    measure_placed_on_ballot_by = db.Column(db.String(200), nullable=False, default="")
    pass_or_fail = db.Column(db.Text, nullable=False, default="")
    #don't include keyword form api because the maindB is more exhaustive
    #keyword = db.Column(db.Text, default="")


    def __repr__(self):
        """Return representation of search instance."""

        return f"<BallotSearch year: {self.year}, month: {self.month}, \n \
                ballot_subject: {self.ballot_subject}, type_of_measure: {self.type_of_measure}, \n \
                measure_placed_by: {self.measure_placed_on_ballot_by}, \n \
                pass_of_fail: {self.pass_or_fail} >"
    

    def serialize(self):
        """Serialize search inputs to a dictionary."""

        return {
            "id": self.id,
            "month": self.month,
            "year": self.year,
            "prop_letter": self.prop_letter,
            "ballot_subject": self.ballot_subject,
            "type_of_measure": self.type_of_measure,
            "measure_placed_on_ballot_by": self.measure_placed_on_ballot_by,
            "pass_or_fail": self.pass_or_fail,
            }


    @classmethod
    def add_search(cls, year, month, prop_letter, pass_or_fail, ballot_subject, \
                  type_of_measure, measure_placed_on_ballot_by):
  
        """Create an instance of a search.
        If ballot_subject input is a integer, will add in the db as empty string."""
        
        search = BallotSearch(
            year=year,
            month=month,
            prop_letter=prop_letter,
            pass_or_fail=pass_or_fail,
            ballot_subject="" if canTurnIntoInteger(ballot_subject) else ballot_subject,
            type_of_measure=type_of_measure,
            measure_placed_on_ballot_by=measure_placed_on_ballot_by,
            )
        
        db.session.add(search)

        return search        



class BallotsFromMainDB(db.Model):
    """
    This is the main ballot database from SF library.
    Date: November 1907- March 2020.

    API data only goes through 1961-2010.
    This table will be used to get detailed info on all ballots and from dates
    outside range of 1907-1960 and 2011-2020.

    From the excel spreadsheet, columns prop_letter, pass_for_fail, vote_counts, 
    and measure_placed_on_ballot_by have blanks, percent, percent_required_to_pass,
    so these columns will have nullable=True

    pdf_available: tells if there's a pdf voter pamphlet available, else - noimage
    """

    __tablename__ = "ballots"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    month = db.Column(db.Text, nullable=True)
    day = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    prop_letter = db.Column(db.Text, nullable=True)
    ballot_subject = db.Column(db.String, nullable=False) 
    type_of_measure = db.Column(db.Text, nullable=False)
    description = db.Column(db.String, nullable=False)
    pass_or_fail = db.Column(db.String, nullable=True)
    measure_placed_on_ballot_by = db.Column(db.Text, nullable=True)
    vote_counts = db.Column(db.String, nullable=True)
    percent_vote = db.Column(db.String, nullable=True)
    percent_required_to_pass = db.Column(db.String, nullable=True)
    pdf_available = db.Column(db.String, nullable=False)
  
    def __repr__(self):
        """Returns a representation of ballot instance."""

        return f"<BallotsFromMainDB year: {self.year}, month: {self.month}, \n \
                ballot_subject: {self.ballot_subject}, \n \
                prop_letter: {self.prop_letter}, \n \
                type_of_measure: {self.type_of_measure}, \n \
                measure_placed_on_ballot_by: {self.measure_placed_on_ballot_by}, \n \
                description: {self.description}, \n \
                pass_of_fail: {self.pass_or_fail}, \n\
                votes_counts: {self.vote_counts}, \n \
                percent: {self.percent_vote}, \n \
                percent_required_to_pass: {self.percent_required_to_pass}, \n \
                pdf_avail: {self.pdf_available} >"
  
   
    def serialize(self):
        """Serialize ballot response from database to a dictionary."""

        return {
            "id": self.id,
            "month": self.month,
            "day": self.day, 
            "year": self.year,
            "date": self.date,
            "prop_letter": self.prop_letter,
            "ballot_subject": self.ballot_subject,
            "type_of_measure": self.type_of_measure,
            "measure_placed_on_ballot_by": self.measure_placed_on_ballot_by,
            "description": self.description,
            "pass_or_fail": self.pass_or_fail,
            "vote_counts": self.vote_counts,
            "percent": self.percent,
            "percent_required_to_pass": self.percent_required_to_pass,
            "pdf_available": self.pdf_available
             }

def connect_db(app):
    """Connect to this db to the Flask app.

    Need to call this in Flask app (app.py)

    """
    db.app = app
    db.init_app(app)