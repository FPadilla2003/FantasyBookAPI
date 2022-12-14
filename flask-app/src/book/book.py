from flask import Blueprint, request, jsonify, make_response
import json
from src import db


book = Blueprint('book', __name__)

# Get all books from the DB
@book.route('/book', methods=['GET'])
def get_books():
    cursor = db.get_db().cursor()
    cursor.execute('select * from book')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get book detail for book with particular bookid
@book.route('/book/<bookid>', methods=['GET'])
def get_book(bookid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from book where bookid = {0}'.format(bookid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@book.route("/book/addbook")
def get_addbook():
    return """
    <h2>Add This Book</h2>
    <form action="/fantasy/book/addbookconfirmation" method="POST">
    <p>Before you add a book, make sure you add an author, publisher, genre, and rating</p>
    <label for="bookid">Book ID:</label><br>
    <input type="text" id="bookid" name="bookid"><br>
    <label for="bookname">Book Name:</label><br>
    <input type="text" id="bookname" name="bookname"><br><br>
    <label for="seriesname">Series Name:</label><br>
    <input type="text" id="seriesname" name="seriesname"><br><br>
    <label for="authorid">Author ID:</label><br>
    <input type="text" id="authorid" name="authorid"><br><br>
    <label for="publisherid">Publisher ID:</label><br>
    <input type="text" id="publisherid" name="publisherid"><br><br>
    <label for="genreid">Genre ID:</label><br>
    <input type="text" id="genreid" name="genreid"><br><br>
    <label for="ratingid">Rating ID:</label><br>
    <input type="text" id="ratingid" name="ratingid"><br><br>
    <label for="isbn10">ISBN 10:</label><br>
    <input type="text" id="isbn10" name="isbn10"><br><br>
    <label for="isbn13">ISBN 13:</label><br>
    <input type="text" id="isbn13" name="isbn13"><br><br>
    <label for="price">Price:</label><br>
    <input type="text" id="price" name="price"><br><br>
    <label for="language">Language:</label><br>
    <input type="text" id="language" name="language"><br><br>
    <label for="pages">Page Amount:</label><br>
    <input type="text" id="pages" name="pages"><br><br>
    <label for="book_format">Book Format (Paperback, etc.):</label><br>
    <input type="text" id="book_format" name="book_format"><br><br>
    <input type="submit" value="Submit">
    </form> 
    """

@book.route("/book/addbookconfirmation", methods = ['GET', 'POST'])
def post_book():
        cursor = db.get_db().cursor()
        bookid = request.form['bookid']
        bookname = request.form['bookname']
        seriesname = request.form['seriesname']
        authorid = request.form['authorid']
        publisherid = request.form['publisherid']
        genreid = request.form['genreid']
        ratingid = request.form['ratingid']
        isbn10 = request.form['isbn10']
        isbn13 = request.form['isbn13']
        price = request.form['price']
        language = request.form['language']
        pages = request.form['pages']
        book_format = request.form['book_format']
        query = 'insert into book (bookid, bookname, seriesname, authorid_fk, publisherid_fk, genreid_fk, ratingid_fk, isbn10, isbn13, price, language, pages, book_format) \
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        cursor.execute(query, (bookid, bookname, seriesname, authorid, publisherid, genreid, ratingid, isbn10, isbn13, price, language, pages, book_format))
        db.get_db().commit()
        return '<h2>The book has been added. Thank you for your addition.</h2>'


