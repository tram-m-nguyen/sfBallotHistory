"""Seed database with real and sample data from CSV Files."""

from csv import DictReader 
from app import db  
from models import BallotSearch, BallotsFromMainDB

db.drop_all()
db.create_all()

# map ballotSearch model with csv search info
with open('generator/searches.csv') as ballot_searches:
    db.session.bulk_insert_mappings(BallotSearch, DictReader(ballot_searches))


with open('generator/ballots.csv', encoding = "ISO-8859-1") as ballots:
    db.session.bulk_insert_mappings(BallotsFromMainDB, DictReader(ballots))

db.session.commit()