from flask import Blueprint, request, jsonify, make_response
import json
from src import db


genre = Blueprint('genre', __name__)

# Get all genres from the DB
@genre.route('/genre', methods=['GET'])
def get_genres():
    cursor = db.get_db().cursor()
    cursor.execute('select * from genre')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get genre detail for genre with particular genreid
@genre.route('/genre/<genreid>', methods=['GET'])
def get_genre(genreid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from genre where genreid = {0}'.format(genreid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response