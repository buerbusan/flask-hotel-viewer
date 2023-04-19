from hotelAPI import create_app
from flask_cors import CORS
from flask_socketio import SocketIO
from flask import  render_template
import os
import json
import sqlite3
from flask_socketio import  emit

application = create_app()
socketio = SocketIO(application)
CORS(application)

url = "db.sqlite"

def dbConnection(url):
    """
    Establishes a connection to the SQLite database.

    Args:
        url (str): URL or path of the SQLite database.

    Returns:
        connection (sqlite3.Connection): SQLite database connection object.
    """
    connection = sqlite3.connect(url)
    return connection

@application.route('/')
def index():
    """
    Renders the index.html template for the root URL.

    Returns:
        Response: Flask response object containing the rendered HTML template.
    """
    return render_template('index.html')

@application.route('/hotelfinder', methods=['POST', 'GET'])
def tester():
    """
    Renders the hotelmap.html template for the /hotelfinder URL.

    Returns:
        Response: Flask response object containing the rendered HTML template.
    """
    return render_template('hotelmap.html')

@socketio.on('category')
def handle_my_custom_event(json_data):
    """
    Event handler for handling 'category' event from the client.

    This function is triggered when a 'category' event is emitted from the client.
    It retrieves the selected amenity from the JSON data, checks if a cached JSON file
    exists for that amenity, and either returns the cached data or queries the database
    for the data and caches it for future use.

    Args:
        json_data (dict): JSON data containing the selected amenity value.

    Returns:
        None
    """
    amenity = json_data['selectedValue']
    cache_file = "{}.json".format(amenity) # Cache file name based on amenity
    if os.path.exists(cache_file):
        # If cache file exists, load data from file
        with open(cache_file, "r") as infile:
            cached_json = json.load(infile)
        return emit('response', cached_json)
    else:
        # If cache file doesn't exist, query the database
        connection = dbConnection(url)
        cursor = connection.cursor()
        cursor.execute("select * from michigan where amenity = '{}'".format(amenity))
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        # Convert the list of tuples to a list of dictionaries
        result_list = [dict(zip(column_names, row)) for row in rows]
        json_object = json.dumps(result_list, indent=4)
        print(json_object)
        with open(cache_file, "w") as outfile:
            outfile.write(json_object)
        return emit('response', result_list)

if __name__ == '__main__':
    socketio.run(application, debug=True)
