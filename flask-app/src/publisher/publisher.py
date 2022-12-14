from flask import Blueprint, request, jsonify, make_response
import json
from src import db


publisher = Blueprint('publisher', __name__)

# Get all publishers from the DB
@publisher.route('/publisher', methods=['GET'])
def get_publishers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from publisher')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get publisher detail for publisher with particular publisherid
@publisher.route('/publisher/<publisherid>', methods=['GET'])
def get_publisher(publisherid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from publisher where publisherid = {0}'.format(publisherid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response