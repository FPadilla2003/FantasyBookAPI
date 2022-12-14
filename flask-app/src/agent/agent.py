from flask import Blueprint, request, jsonify, make_response
import json
from src import db


agent = Blueprint('agent', __name__)

# Get all agents from the DB
@agent.route('/agent', methods=['GET'])
def get_books():
    cursor = db.get_db().cursor()
    cursor.execute('select * from agent')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get agent detail for agent with particular agentid
@agent.route('/agent/<agentid>', methods=['GET'])
def get_book(agentid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from agent where agentid = {0}'.format(agentid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response