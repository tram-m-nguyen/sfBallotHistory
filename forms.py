from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import NumberRange



class searchForm(FlaskForm):
    """Form for searching ballots."""

    class Meta:
        csrf = False

    year = IntegerField("Year", validators=[NumberRange(1961, 2010)])
    month = SelectField("Month", choices=[ ('FEB'),
                                            ('MAR'), 
                                            ('APR'),
                                            ('JUN'),
                                            ('AUG'),
                                            ('NOV'),
                                            ('DEC')])
    subject = StringField("Ballot Subject")
    # refers to type_measure
    type_of_measure = SelectField('Type of Measure', 
                          choices=[ ('B',  'Bond Issue'), 
                                    ('C',  'Charter Amendment'),
                                    ('L',  'Lease Revenue Bond Issue'),
                                    ('O',  'Ordinance'),
                                    ('P',  'Policy Declaration'),
                                    ('R',  'Recall'),
                                    ('RM', 'Regional Measure'),
                                    ('T',  'Tax Authority for School District')])
    #refers to col "by" in search query
    measure_placed_by = SelectField('How measure was placed on ballot',
                    choices=[ ('C', 'Charter Commission, elected by the voters'),
                              ('I', 'Initiative Petition'),
                              ('L', 'Labor Disputes'),
                              ('M', 'Mayor'),
                              ('R', 'Referendum Petition'),
                              ('S', 'The Board of Supervisors'),
                              ('SE', 'Special Board of Education'),
                              ('SFUSD', 'San Francisco Unified School District')])
    pass_or_fail = SelectField("Pass or Fail", choices=[('P', 'Pass'), ('F', 'Fail')])
    #keywords search must be very specific - user inputs 1 keyword, 
    # will make request for all 5 keywords: Keyword1, Keyword2, Keyword3, Keyword4
    keyword1 = StringField("Enter a keyword1")
    keyword2 = StringField("Enter a keyword2")                          
    keyword3 = StringField("Enter a keyword3")       
    keyword4 = StringField("Enter a keyword4")       
    keyword5 = StringField("Enter a keyword5")       

