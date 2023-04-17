# Flask Based Hotel Finder 

This projects using web GIS to locate and find Different hotels and eateries of the State of MICHIGAN

## Technologies Used

- Python for backend (Flask), SQLITE Database, Front end using HTML,CSS,Javascript, LeafletJS, SocketIO and TurfJS

## Workflow

- it is a flask application in which i created custom APIs to communicate between the server and the client for seamless data transfer and reception, this 
- It works mainly on sockets to receive communicate the data bi directionally between the client and server.
- Client selects category, and that category is trasmitted to the server realtime using socketIO at both client and server side, client side uses flask-SOcketIO and server uses SocketIO.JS
- Uses SQL to query and feed back the data to the server in real time using SocketIO 
- Handle data caching to check if the requests have already been made and if a JSON exists then use that instead of running query from the database.

## GIS

- Use of Geospatial Technologies for mapping and processing of Location based data using leaflet JS and Flask for managing JSON data types

## Data Formats
- Data is read by the database in B-Tree format  by the SQLITE Database and then converted to JSON after a database transaction is carried out. 
- The communication between the client server is JSON.
- Front end GIS is handled using GeoJSON data.
- 

## Installation

- requirements.txt is included
- pip install -r requirements.txt

## Usage

- After setting up the python environment run the python file application.py
- python application.py
-Open the link 127.0.0.1:5000 on the browser

## DEMO

- Link

