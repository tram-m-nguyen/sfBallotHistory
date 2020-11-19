import copy

"""Helpers for jinja templates."""

# run doc test verbosely:
#     python -m doctest -v helpers.py


def yesVotes(string):
    """Takes in a string of yes and no votes, and return string with values
    of yes votes.
    
    string: "Yes: 23,257 / No: 4,637" returns "23,257 "

        >>> yesVotes('Yes: 23,257  /  No: 4,637')
        '23,257 '

        >>> yesVotes('Yes: 21,000  /  No: 5,809')
        '21,000 '

        >>> yesVotes('Yes: 14,404  /  No: 7,805')
        '14,404 '

    """
    if len(string) == 0:
        return "Ballot Withdrawn"

    votes = string.split(" / ")
    yesVotes = votes[0]
    idx = yesVotes.find(" ")

    return yesVotes[idx+1:]


def noVotes(string):
    """Takes in a string of yes and no votes, and return string with values
        of yes votes.
    
    string: "Yes: 23,257 / No: 4,637" returns "4,637"

        >>> noVotes('Yes: 23,257 / No: 4,637')
        '4,637'

        >>> noVotes('Yes: 21,000  /  No: 5,809')
        '5,809'

        >>> noVotes('Yes: 14,404  /  No: 7,805')
        '7,805'

    """
    if len(string) == 0:
        return "Ballot Withdrawn"

    votes = string.split(" / ")
    noVotes = votes[1]
    idx = noVotes.find("N")

    return noVotes[idx+4:]


def displayVotePercents(string):
    """
    Returns a cleaner percent_vote string. 

    Original string: 'Yes: 83.3%  /  No: 16.7%'

    Final string: 'Yes: 83.3%  |  No: 16.7%'

        >>> displayVotePercents('Yes: 91.8%  /  No: 8.2%')                        
        'Yes: 91.8%  |  No: 8.2%'
        >>> displayVotePercents('Yes: 54.3%  /  No: 45.7%')                       
        'Yes: 54.3%  |  No: 45.7%'
        >>> displayVotePercents('Yes: 57.4%  /  No: 42.6%')                       
        'Yes: 57.4%  |  No: 42.6%'


    """

    return string.replace(" / ", " | ")


def isFormEmpty(formInputs):
    """
    Returns a Boolean. True is all inputs are empty or None. Else, return False.

    formInputs is an object of form keys and values. 

    Before: {'subject': '', 'month': '', 'year': None, 'prop_letter': '', 
    'type_of_measure': '', 'measure_placed_by': '', 'pass_or_fail': ''}


        >>> isFormEmpty({'subject': '', 'month': '', 'year': None, \
            'prop_letter': '', 'type_of_measure': '', 'measure_placed_by': '', \
            'pass_or_fail': ''})               
        True

        >>> isFormEmpty({'subject': 'education', 'month': '', 'year': 2015, \
            'prop_letter': '', 'type_of_measure': '', 'measure_placed_by': '', \
            'pass_or_fail': ''})                     
        False

        >>> isFormEmpty({'subject': 'education', 'month': '', 'year': None, \
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


def turnStrIntoSqlQuery(string):
    """Return every word in string, capitalized with '%' to search in sql.
    
    For example: 'education attainment ballot' -> '%Education%Attainment%Ballot%'.

        >>> turnStrIntoSqlQuery('affordable housing')                                         
        '%Affordable%Housing%'
        >>> turnStrIntoSqlQuery('affordable')                                                 
        '%Affordable%'
        >>> turnStrIntoSqlQuery('affordable education')                                        
        '%Affordable%Education%'
        >>> turnStrIntoSqlQuery('affordable tax')                                             
        '%Affordable%Tax%'

    """
    words = string.split()

    cap_words = [(word[0].upper() + word[1:]) for word in words]
    #print(" new cap words, new cap new cap new cap new cap ", cap_words)

    sqlString = ''

    for word in cap_words:
        sqlString+= '%' + word

    return sqlString + '%'


def removeEmptyValues(searchInputs):
    """Return new dictionary where 0 and empty values are removed.
    
    searchInput is a dictionary.
    
        # >>> removeEmptyValues({ \
        #     'ballot_subject': '',  \
        #     'measure_placed_on_ballot_by': 'Consolidated into another Proposition',  \
        #     'month': 'June',  \
        #     'pass_or_fail': 'F',  \
        #     'prop_letter': '',  \
        #     'type_of_measure': 'Not Placed on Ballot',  \
        #     'year': 2002 })
        #     {'ballot_subject': '',\
        #     'measure_placed_on_ballot_by': 'Consolidated into another Proposition',\
        #     'month': 'June',\
        #     'pass_or_fail': 'F',\
        #     'prop_letter': '',\
        #     'type_of_measure': 'Not Placed on Ballot',\
        #     'year': 2002}

    """
    #make deep copy to not

    for field in list(searchInputs.keys()):
        if searchInputs[field] == "" or searchInputs[field] == 0:
            del searchInputs[field]

    
    return searchInputs