from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  """Connect to the database"""

  db.app = app 
  db.init_app(app)


class BallotSearch(db.Model):
    """
    BallotSearch Table captures for ballot search inputs from the user.
    """
    
    __tablename__ = "ballot_searches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False, default=0)
    month = db.Column(db.Text, nullable=False, default="")
    subject = db.Column(db.String(100), nullable=False, default="")
    type_of_measure = db.Column(db.Text, nullable=False, default="")
    measure_placed_on_ballot_by = db.Column(db.Text, nullable=False, default="")
    pass_or_fail = db.Column(db.Text, nullable=False, default="")
    keyword = db.Column(db.Text, default="")


    def __repr__(self):
      """Return representation of search instance."""

        return f"<BallotSearch year: {self.year}, month: {self.month}, \
                subject: {self.subject}, type_of_measure: {self.type_of_measure}, \
                measure_placed_by: {measure_placed_by}, pass_of_fail: {self.pass_of_fail},\
                keyword: {self.keyword} >"



class BallotFromMainDatabase(db.Model):
    """
    This is the main ballot database from SF library.
    Date: November 1907- March 2020.

    API data only goes through 1961-2010.
    This table will be used to get detailed info on all ballots and from dates
    outside range of 1907-1960 and 2011-2020.

    From the excel spreadsheet, columns prop_letter, pass_for_fail, vote_counts, 
    and measure_placed_on_ballot_by have blanks, so these columns will have nullable=True

    pdf_available: tells if there's a pdf voter pamphet available, else - noimage
    """

    __tablename__ = "ballots"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    month = db.Column(db.Text, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    prop_letter = db.Column(db.Text, nullable=True)
    subject = db.Column(db.String, nullable=False) #subject from API
    type_of_measure = db.column(db.Text, nullable=False)
    measure_placed_on_ballot_by = db.Column(db.Text, nullable=True)
    description = db.Column(db.String, nullable=False)
    pass_or_fail = db.Column(db.String, nullable=True)
    vote_counts = db.Column(db.String, nullable=True)
    percent = db.Column(db.String, nullable=False)
    percent_required_to_pass = db.Column(db.String, nullable=False)
    pdf_available = db.Column(db.String, nullable=False)
  
    def __repr__(self):
        """Returns a representation of ballot instance."""

        return f"<BallotFromMainDatabase year: {self.year}, month: {self.month}, \
                prop_letter: {self.prop_letter}, subject: {self.subject}, 
                type_of_measure: {self.type_of_measure}, \
                measure_placed_on_ballot_by: {measure_placed_by}, \
                description: {self.description}, pass_of_fail: {self.pass_of_fail},\
                votes_counts: {self.vote_counts}, percent: {self.percent}, \
                percent_required_to_pass: {self.percent_required_to_pass}, \
                pdf_avail: {self.pdf_available} >"
  
   
  
# old dataset before cleaning excel spreadsheet

#   compare api to main excel spreasheet
# {   name_in_api: col_name_in_excel: values_format
#     "month- NOV": "Month-November", 
#     "year": "Year",
#     "letter": "PropLetter",
#     "subject": "PropTitle",
#     "yes_votes": "66982",
#     "no_votes": "69060",
#     "pass_or_fail": "F",
#     "percent": "0.49236265271019242",
#     "type_measure": "KindOfProp",
#     "by": "HowPlaced",
#     "keyword1": "Annual Budget",
#     "keyword2": "Fiscal Year",
#     "keyword3": "General Fund"

#     extras: excel spreasheet has Month, Day, Year Nov-7-1961 
#     fullImage: name of pdf of the ballots 
#     ex: fullImage: November7_1961 -> go to sf https://sfpl.org/locations/main-library/government-information-center/san-francisco-government/san-francisco-1/san
#     and click on November 7, 1961 and you'll go to this site with pdf: 
#     https://webbie1.sfpl.org/multimedia/pdf/elections/November7_1961.pdf
#   }