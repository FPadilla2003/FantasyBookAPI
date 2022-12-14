from flask import Blueprint, request, jsonify, make_response
import json
from src import db


ratings = Blueprint('ratings', __name__)

# Get all ratings from the DB
@ratings.route('/ratings', methods=['GET'])
def get_ratingsall():
    cursor = db.get_db().cursor()
    cursor.execute('select * from ratings')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get ratings detail for ratings with particular ratingsid
@ratings.route('/ratings/<ratingsid>', methods=['GET'])
def get_rating(ratingsid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from ratings where ratingid = {0}'.format(ratingsid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@ratings.route("/ratings/addrating")
def get_addrating():
    return """
    <h2>Add a New Review</h2>
    <form action="/fantasy/ratings/addratingconfirmation" method="POST">
    <label for="ratingid">Rating ID:</label><br>
    <input type="text" id="ratingid" name="ratingid"><br>
    <label for="website_name">Website Name:</label><br>
    <input type="text" id="website_name" name="website_name"><br><br>
    <label for="rating_number">Rating Number (0-5):</label><br>
    <input type="text" id="rating_number" name="rating_number"><br><br>
    <label for="ratings_amount">Ratings Amount (How many ratings?):</label><br>
    <input type="text" id="ratings_amount" name="ratings_amount"><br><br>
    <label for="reviews_amount">Reviews Amount (How many reviews?):</label><br>
    <input type="text" id="reviews_amount" name="reviews_amount"><br><br>
    <input type="submit" value="Submit">
    </form> 
    """

@ratings.route("/ratings/addratingconfirmation", methods = ['GET', 'POST'])
def post_rating():
        cursor = db.get_db().cursor()
        ratingid = request.form['ratingid']
        website_name = request.form['website_name']
        rating_number = request.form['rating_number']
        ratings_amount = request.form['ratings_amount']
        reviews_amount = request.form['reviews_amount']
        query = 'insert into ratings (ratingid, website_name, rating_number, ratings_amount, reviews_amount) \
        values (%s, %s, %s, %s, %s);'
        cursor.execute(query, (ratingid, website_name, rating_number, ratings_amount, reviews_amount))
        db.get_db().commit()
        return '<h2>The review has been added. Thank you for your addition.</h2>'
