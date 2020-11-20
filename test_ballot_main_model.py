"""BallotsFromMainDB model tests."""

# run these tests like:
#
# python -m unittest test_ballot_main_model.py 

import os 
from unittest import TestCase

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


class BallotsMainDBModelTestCase(TestCase):
    """Test Models for BallotsFromMainDB."""

    def setUp(self):
        """Create test, and add sample data before every test."""
        
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

        #add and commit to db
        db.session.add_all([ballot1, ballot2])
        db.session.commit()

        #get ballots from database
        ballots = BallotsFromMainDB.query.all()

        self.ballot1 = ballot1
        self.ballot2 = ballot2


    def tearDown(self):
        """Clean up transactions after each test."""
            
        result = super().tearDown()
        db.session.rollback()
        return result


    def test_ballotMainModel(self):
        """Does my basic model work?"""
        
        ballot3 = BallotsFromMainDB(
        year = 3000, 
        month = "January",
        day=29,
        date="January 29, 2900",
        prop_letter= "1",
        ballot_subject= "More Money For Clinics", 
        type_of_measure= "Charter Amendment", 
        measure_placed_on_ballot_by="Supervisors", 
        description= "Fix clinics",
        pass_or_fail= "P",
        vote_counts="Yes: 300001 /  No: 47",
        percent_vote= "Yes: 64.3%  /  No: 35.6%", 
        percent_required_to_pass= "50%+1", 
        pdf_available= "noimage"
        )

        db.session.add(ballot3)
        db.session.commit()

        ballot1_description= "Setting forth a proposal relating to bonds issued for \
            the acquisition of public utilities, the registration thereof, and \
            the levy of taxes to provide for the interest thereon and a sinking \
            fund, and to bonds issued for the acquisition of land and the \
            construction or acquisition of any permanent building or buildings, \
            improvement or improvements."

        ballots = BallotsFromMainDB.query.all()

        self.assertEqual(len(ballots), 3)
        self.assertEqual(self.ballot1.year, 2900)
        self.assertEqual(self.ballot1.description, ballot1_description)
        self.assertNotEqual(self.ballot1.description, "Not this description")

        self.assertEqual(self.ballot2.year, 2001)
        self.assertEqual(ballot3.ballot_subject, "More Money For Clinics")
        self.assertEqual(ballot3.pdf_available, "noimage")
        self.assertNotEqual(ballot3.pass_or_fail, "F")


    def test_userRepr(self):
        '''Does the __repr__ method work?'''

        ballotRepr2 = f"<BallotsFromMainDB year: {self.ballot2.year}, month: {self.ballot2.month}, \n \
                ballot_subject: {self.ballot2.ballot_subject}, \n \
                prop_letter: {self.ballot2.prop_letter}, \n \
                type_of_measure: {self.ballot2.type_of_measure}, \n \
                measure_placed_on_ballot_by: {self.ballot2.measure_placed_on_ballot_by}, \n \
                description: {self.ballot2.description}, \n \
                pass_of_fail: {self.ballot2.pass_or_fail}, \n\
                votes_counts: {self.ballot2.vote_counts}, \n \
                percent: {self.ballot2.percent_vote}, \n \
                percent_required_to_pass: {self.ballot2.percent_required_to_pass}, \n \
                pdf_avail: {self.ballot2.pdf_available}>"

        self.assertEqual(repr(self.ballot2), ballotRepr2)
        self.assertNotEqual(repr(self.ballot1), ballotRepr2)


        