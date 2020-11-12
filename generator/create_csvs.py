"""Generate random searches csv.

Run this file to generate files."""

import csv
from faker import Faker
import random

SEARCH_BALLOTS_HEADERS=["year", "month", "subject", "type_of_measure", \
                          "measure_placed_on_ballot_by", "pass_or_fail", \
                          "keyword"]
                          
VALID_MONTHS = ['FEB','MAR', 'APR', 'JUN', 'AUG', 'NOV', 'DEC']


SUBJECTS = [ "Earthquake Safety and Emergency Response Bond",
    "Retirement Benefit Costs",
    "Film Commission",
    "Budget Line Item for Police Department Security for City Officials and Dignitaries",
    "Renters’ Financial Hardship Applications",
    "Transbay Transit Center",
    "Vehicle Registration Fee",
    "Earthquake Retrofit Bond",
    "City Retirement and Health Plans",
    "Mayoral Appearances at Board Meetings",
    "Non-Citizen Voting in School Board Elections",
    "Election Day Voter Registration"]

TYPES_OF_MEASURES = ['Bond Issue', 
                            'Charter Amendment',
                             'Lease Revenue Bond Issue',
                             'Ordinance',
                             'Policy Declaration',
                             'Recall',
                             'Regional Measure',
                             'Tax Authority for School District']

measure_placed_on_ballot_by = ['Charter Commission, elected by the voters',
                                'Initiative Petition',
                                'Labor Disputes']

NUM_SEARCHES = 5

fake = Faker()

# Generate random searches
with open("generator/searches.csv", "w") as searches_csv:
    # write to searches cv
    searches_writer = csv.DictWriter(searches_csv, fieldnames=SEARCH_BALLOTS_HEADERS)
    searches_writer.writeheader()

    # loop through and turn into dictionary
    for i in range(NUM_SEARCHES):
        searches_writer.writerow(dict(
          year=random.randrange(1907, 2020),
          month=random.choice(VALID_MONTHS),
          subject=random.choice(SUBJECTS),
          type_of_measure=random.choice(TYPES_OF_MEASURES),
          measure_placed_on_ballot_by="",
          pass_or_fail=random.choice(["F", "P"]),
          keyword="Education"
        ))



