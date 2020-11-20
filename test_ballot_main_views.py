from app import app

# run these tests like:
#
# FLASK_ENV=production python -m unittest test_ballot_main_views.py


import os
from unittest import TestCase
from flask import session
from models import db, connect_db, BallotsFromMainDB

# to sue diff db for testing
os.environ['DATABASE_URL'] = "postgresql:///ballot_history_test"

from app import app, SEARCH_INPUTS

# create table once for all tests, in each test, will del data and create a fresh 
# new clean test dat

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False

class BallotMainViewTestCase(TestCase):
    """Test views for search form."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()
 
        ballot1 = BallotsFromMainDB(
             year=2900, 
             month="November",
             day=2,
             date="November 2, 2900",
             prop_letter="1",
             ballot_subject="Recall of Elected Officials", 
             type_of_measure="Charter Amendment", 
             measure_placed_on_ballot_by="Supervisors", 
             description= "Setting forth a proposal relating to bonds issued for \
             the acquisition of public utilities, the registration thereof, and \
             the levy of taxes to provide for the interest thereon and a sinking \
             fund, and to bonds issued for the acquisition of land and the \
             construction or acquisition of any permanent building or buildings, \
             improvement or improvements.", 
             pass_or_fail="P",
             vote_counts="Yes: 23,257  /  No: 4,637",
             percent_vote="Yes: 64.3%  /  No: 35.6%", 
             percent_required_to_pass="50%+1", 
             pdf_available="November5_2900",
 
         )
 
        ballot2 = BallotsFromMainDB(
             year=2001, 
             month="December",
             day=2,
             date="December 2, 2001",
             prop_letter="1",
             ballot_subject="Recall of Elected Officials", 
             type_of_measure="Charter Amendment", 
             measure_placed_on_ballot_by="Supervisors", 
             description="Fix school parks",
             pass_or_fail="P", 
             vote_counts="Yes: 3  /  No: 4,637",
             percent_vote="Yes: 64.3%  /  No: 35.6%", 
             percent_required_to_pass="50%+1", 
             pdf_available="November5_2900",
 
         )
 
        db.session.add_all([ballot1, ballot2])
        db.session.commit()
 
        self.ballot1 = ballot1 
        self.ballot2 = ballot2
        self.client = app.test_client()

    def tearDown(self):
        """Clean up fouled transaction."""

        result = super().tearDown()
        db.session.rollback()
        return result

    def test_search_index(self):
        #this allows you to make request to flask
        with self.client as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            htmlString = '<h1 class="pt-5 text-center text-primary">San Francisco Ballot Propositions</h1>'
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn(htmlString, html)
            # can test for certain strings in html
            self.assertIn("Amendment", str(resp.data))
            self.assertIn("Ballot Status", str(resp.data))
            self.assertIn("Labor Dispute", str(resp.data))

    def test_redirection(self):
        with self.client as client:
            resp = client.get("/search")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")
            self.assertIn('<title>Redirecting...</title>', html)
    
    # def test_search_submit(self):
    #     # there's a new search object in the db

    #     ballot3 = BallotsFromMainDB(
    #          year=2000, 
    #          month="December",
    #          day=2,
    #          date="December 2, 2000",
    #          prop_letter="F",
    #          ballot_subject="No More Elected Officials", 
    #          type_of_measure="Charter Amendment", 
    #          measure_placed_on_ballot_by="Board of Supervisors", 
    #          description="Decrease pay for elected officials",
    #          pass_or_fail="P", 
    #          vote_counts="Yes: 3  /  No: 4,637",
    #          percent_vote="Yes: 64.3%  /  No: 35.6%", 
    #          percent_required_to_pass="50%+1", 
    #          pdf_available="November5_2000",
 
    #     )

    #     #db.session.add(ballot3)
    #     #db.session.commit()
 
    #     with self.client as client:
    #         with client.session_transaction() as session:
    #             session[SEARCH_INPUTS] = ballot3

    #         resp = client.get("/search/results", data={'year':2000})
    #         self.assertEqual(resp.status_code, 200)

    #         htmlString = '<h1 class="pt-5 text-center text-primary">San Francisco Ballot Propositions</h1>'
    #         self.assertIn(htmlString, html)
