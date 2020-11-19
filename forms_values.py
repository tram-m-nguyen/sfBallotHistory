#Valid months, type of measures and measure_placed_by
VALID_MONTHS = [("", "- Month - "),
                ("January",'JAN'),
                ("February",'FEB'),
                ("March",'MARCH'),
                ("April",'APRIL'),
                ("May",'MAY'),
                ("June",'JUNE'),
                ("July",'JULY'),
                ("August",'AUG'),
                ("September",'SEPT'),
                ("October",'OCT'),
                ("November",'NOV'),
                ("December",'DEC')]

#when you query, do bond or bonds to the large database
VALID_TYPES_OF_MEASURES = [
("", "----"),
("Amendment","Amendment"),
('Bond', "Bond"),
("Bond Issue", "Bond Issue"),
("Bond Measure", "Bond Measure"),
("Charter Amendment", "Charter Amendment"),
("Consolidated into another Proposition", "Consolidated into another Proposition"),
("District Bond Issue (San Francisco Bay Area Rapid Transit District)",  \
"District Bond Issue (San Francisco Bay Area Rapid Transit District)"),
("Failed to Qualify", "Failed to Qualify"),
("Initiative", "Initiative"),
("Lease Financing", "Lease Financing"),
("Measure", "Measure"),  
("New Charter",  "New Charter"), 
("Not Placed on Ballot",  "Not Placed on Ballot"), 
("Ordinance",  "Ordinance"), 
("Parcel Tax",  "Parcel Tax"), 
("Policy Declaration",  "Policy Declaration"), 
("Proposition",  "Proposition"), 
("Recall",  "Recall"), 
("Referendum",  "Referendum"), 
("Regional Measure",  "Regional Measure"), 
("School District",  "School District"), 
("Tax",  "Tax"), 
("Withdrawn", "Withdrawn"),]

VALID_MEASURES_PLACED_ON_BALLOT_BY = [
("", "----"), 
("Board of Directors of the San Francisco Bay Area Rapid Transit District ", "Board of Directors of the San Francisco Bay Area Rapid Transit District "),
("Board of Education", "Board of Education"),
("Board of Supervisors", "Board of Supervisors"),
("Charter Commission", "Charter Commission"),
("Community College Board", "Community College Board"),
("Community College District", "Community College District"),
("Consolidated into another Proposition", "Consolidated into another Proposition"),
("Ethics Commission", "Ethics Commission"),
("Failed to Qualify", "Failed to Qualify"),
("Four or More Supervisors", "Four or More Supervisors"),
("Governing Board of the San Francisco Bay Restoration Authority", "Governing Board of the San Francisco Bay Restoration Authority"),
("Initiative", "Initiative"),
("Labor Dispute", "Labor Dispute"),
("Mayor", "Mayor"),
("Not Placed on Ballot", "Not Placed on Ballot"),
("Referendum", "Referendum"),
("Senate Bill 916 (Perata) 2003-2004 Session; Senate Select Committee on Bay Area Transportation", "Senate Bill 916 (Perata) 2003-2004 Session; Senate Select Committee on Bay Area Transportation"),
("Supervisors", "Supervisors"),
("Withdrawn", "Withdrawn")]