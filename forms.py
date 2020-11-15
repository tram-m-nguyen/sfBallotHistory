from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField 
from wtforms.validators import NumberRange, AnyOf, Optional, Length
from forms_values import VALID_MONTHS, VALID_TYPES_OF_MEASURES, VALID_MEASURES_PLACED_BY



class searchForm(FlaskForm):
    """Form for searching ballots."""

    class Meta:
        csrf = False

    subject = StringField("Subject")

    month = SelectField("Month", 
                             choices=VALID_MONTHS)

    year = IntegerField("Year", 
                            validators=[NumberRange(1907, 2020)])
    
    prop_letter = StringField("Proposition letter or number", validators=[Optional(), Length(max=2)])

    # refers to type_measure
    type_of_measure = SelectField('Type of Measure', 
                                    choices=VALID_TYPES_OF_MEASURES)

    #refers to col "by" in search query
    measure_placed_by = SelectField('How measure was placed on ballot',
                                        choices=VALID_MEASURES_PLACED_BY)
 
    pass_or_fail = SelectField("Pass or Fail", 
                                choices=[   ("", "- Ballot Status -"),
                                            ('P', 'Pass'), 
                                            ('F', 'Fail')])




