"""BallotsFromMainDB model tests."""

# run these tests like:
#
# python -m unittest test_ballot_main_model.py 

import os 
from unittest import TestCase
from sqlalchemy import exc 

from models import db, BallotsFromMainDB

#mainly testing can you and and delete to the db correctly

# before app import, set an environmental variable to use a separate db for the 
# tests -- need this before app import since it's already connected to the db

os.environ['DATABASE_URL'] = "postgresql:///ballot_history_test"

# now import app

from app import app

# Create tables here and create the table once for all the tests -- in each 
# test - will delete the data and crate new test data
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.create_all()

#create class model test, naming exactly
class BallotsFromMainDBModelTestCase(TestCase):
    """Test Models for BallotsFromMainDB."""

    #this stuff to do before every test.
    def setUp(self):
        """Create test, and add sample data."""

        # BallotsFromMainDB.query.delete()
        # BallotsFromMainDB.query.delete()
        db.drop_all()
        db.create_all()


        #create a ballot
        ballot1 = BallotsFromMainDB(
            year = 2900, 
            month = "November",
            prop_letter= "1",
            subject= "Recall of Elected Officials", 
            type_of_measure= "Charter Amendment", 
            measure_placed_on_ballot_by="Supervisors", 
            description= "Setting forth a proposal relating to bonds issued for \
            the acquisition of public utilities, the registration thereof, and \
            the levy of taxes to provide for the interest thereon and a sinking \
            fund, and to bonds issued for the acquisition of land and the \
            construction or acquisition of any permanent building or buildings, \
            improvement or improvements.", 
            pass_of_fail= "P",
            votes_counts="Yes: 23,257  /  No: 4,637",
            percent= "Yes: 64.3%  /  No: 35.6%", 
            percent_required_to_pass= "50%+1", 
            pdf_avail= "November5_2900"

        )

        #create a ballot
        ballot2 = BallotsFromMainDB(
            year = 3900, 
            month = "December",
            prop_letter= "1",
            subject= "Recall of Elected Officials", 
            type_of_measure= "Charter Amendment", 
            measure_placed_on_ballot_by="Supervisors", 
            description= "Fix school parks",
            pass_of_fail= "P", 
            votes_counts="Yes: 3  /  No: 4,637",
            percent= "Yes: 64.3%  /  No: 35.6%", 
            percent_required_to_pass= "50%+1", 
            pdf_avail= "November5_2900"

        )

        #add and commit to db
        db.session.add_all([ballot1, ballot2])
        db.session.commit()

        #get ballots from database
        ballots = BallotsFromMainDB.query.all()

        ballot1 = ballots[0]
        print('this is ballot1', ballot1)
        ballot2 = ballots[1]

        self.ballot1 = ballot1
        self.ballot2 = ballot2

        self.client = app.test_client()

        def tearDown(self):
            """Clean up transactions after each test."""

            result = super().tearDown()
            db.session.rollback()
            return result

        def test_ballot_main_model(self):
            """Does my basic model work?"""
            
            ballot3 = BallotsFromMainDB(
            year = 3000, 
            month = "January",
            prop_letter= "1",
            subject= "More Money For Clinics", 
            type_of_measure= "Charter Amendment", 
            measure_placed_on_ballot_by="Supervisors", 
            description= "Fix clinics",
            pass_of_fail= "P",
            votes_counts="Yes: 300001 /  No: 47",
            percent= "Yes: 64.3%  /  No: 35.6%", 
            percent_required_to_pass= "50%+1", 
            pdf_avail= "noimage"

            )

            #add this test ballot to db
            db.session.add(ballot3)
            db.session.commit()

            ballots = BallotsFromMainDB.query.all()
            ballot3 = ballots[2]
            #there should be 2 ballots in the db
            self.assertEqual(len(ballots), 3)
            self.assertEqual(self.ballot1.year, 2009)
            self.assertEqual(self.ballot2.year, 2000)
            self.assertEqual(ballot3.subject, "More Money For Clinics")