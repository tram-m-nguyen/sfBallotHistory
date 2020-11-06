# Create flask application

from flask import Flask, request

# this is how Flask app needs to know what module to scan for for things 
# like routes the __name__ is required and must be written like this
app = Flask(__name__)



