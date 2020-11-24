# sfBallotHistory

## Overview
* This is a search application, where users can search for San Francisco Ballots from 1907 - 2020.

## Setup
* Create a virtual environment and install dependencies


> $ python3 -m venv venv \
> $ source venv/bin/activate \
> (venv) $ pip install -r requirements.txt`

* Create and seed the database
> (venv) $ createdb ballot_history \
> (venv) $ python seed.py \

* Start server
> (venv) $ flask run

## Run Tests
* Run a unittest file:

> FLASK_ENV=production python -m unittest NAME_OF_FILE
