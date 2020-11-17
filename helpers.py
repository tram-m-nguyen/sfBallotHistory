"""Helpers for jinja templates."""

# run doc test verbosely:
#     python -m doctest -v helpers.py


def yes_votes(string):
    """Takes in a string of yes and no votes, and return string with values
    of yes votes.
    
    string: "Yes: 23,257 / No: 4,637" returns "23,257 "

        >>> yes_votes('Yes: 23,257  /  No: 4,637')
        '23,257 '

        >>> yes_votes('Yes: 21,000  /  No: 5,809')
        '21,000 '

        >>> yes_votes('Yes: 14,404  /  No: 7,805')
        '14,404 '

    """

    votes = string.split(" / ")
    yes_votes = votes[0]
    idx = yes_votes.find(" ")

    return yes_votes[idx+1:]


def no_votes(string):
    """Takes in a string of yes and no votes, and return string with values
        of yes votes.
    
    string: "Yes: 23,257 / No: 4,637" returns "4,637"

        >>> no_votes('Yes: 23,257 / No: 4,637')
        '4,637'

        >>> no_votes('Yes: 21,000  /  No: 5,809')
        '5,809'

        >>> no_votes('Yes: 14,404  /  No: 7,805')
        '7,805'

    """

    votes = string.split(" / ")
    no_votes = votes[1]
    idx = no_votes.find("N")

    return no_votes[idx+4:]


def display_vote_percents(string):
    """
    Returns a cleaner percent_vote string. 

    Original string: 'Yes: 83.3%  /  No: 16.7%'

    Final string: 'Yes: 83.3%  |  No: 16.7%'

        >>> display_vote_percents('Yes: 91.8%  /  No: 8.2%')                        
        'Yes: 91.8%  |  No: 8.2%'
        >>> display_vote_percents('Yes: 54.3%  /  No: 45.7%')                       
        'Yes: 54.3%  |  No: 45.7%'
        >>> display_vote_percents('Yes: 57.4%  /  No: 42.6%')                       
        'Yes: 57.4%  |  No: 42.6%'


    """

    return string.replace(" / ", " | ")


def is_form_empty(formInputs):
    """
    Returns a Boolean. True is all inputs are empty or None. Else, return False.

    formInputs is an object of form keys and values. 

    Before: {'subject': '', 'month': '', 'year': None, 'prop_letter': '', 
    'type_of_measure': '', 'measure_placed_by': '', 'pass_or_fail': ''}


        >>> is_form_empty({'subject': '', 'month': '', 'year': None, \
            'prop_letter': '', 'type_of_measure': '', 'measure_placed_by': '', \
            'pass_or_fail': ''})               
        True

        >>> is_form_empty({'subject': 'education', 'month': '', 'year': 2015, \
            'prop_letter': '', 'type_of_measure': '', 'measure_placed_by': '', \
            'pass_or_fail': ''})                     
        False

        >>> is_form_empty({'subject': 'education', 'month': '', 'year': None, \
            'prop_letter': '', 'type_of_measure': '', 'measure_placed_by': '', \
            'pass_or_fail': 'Pass'})                     
        False



    """

    inputs = formInputs.values()

    # any return True for any values in iterable that's true
        
    return not any(inputs)


def canTurnIntoInteger(ballot_subject):
    """Return True if can turn string into integer."""
    try:
        ballot = int(ballot_subject)
        return True
    except ValueError:
        return False 