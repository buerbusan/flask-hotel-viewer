from contextlib import redirect_stderr
from urllib import response
from flask import Blueprint,request,render_template,redirect,url_for,Response,session
import psycopg2
from dotenv import load_dotenv
import os
import geopy
from geopy.geocoders import Nominatim,GoogleV3
import json
import warnings
import sqlite3

warnings.filterwarnings("ignore")

# Define the views blueprint
views = Blueprint('views', __name__, template_folder='templates')

# Import socketio here
from application import socketio

url = "db.sqlite"

def dbConnection(url):
    connection = sqlite3.connect(url)
    return connection

@views.route('/')
def index():
    return render_template ('index.html')

@views.route('/hotelfinder', methods=['POST', 'GET'])
def tester():
    return render_template('hotelmap.html')

@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))
    # You can emit a response back to the client using the `emit` function
    emit('my response', {'data': 'Server response'})

