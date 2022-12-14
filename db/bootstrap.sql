CREATE DATABASE fantasy_book_db;

USE fantasy_book_db;

GRANT ALL PRIVILEGES ON fantasy_book_db.* TO 'webapp'@'%';
FLUSH PRIVILEGES;

SET FOREIGN_KEY_CHECKS=0;
SET autocommit=1;

DROP TABLE IF EXISTS agent;

CREATE TABLE agent (
    agentid INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);

DROP TABLE IF EXISTS author;

CREATE TABLE author (
    authorid INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    agentid_fk INT,
    FOREIGN KEY (agentid_fk) REFERENCES agent (agentid),
    email VARCHAR(255)
);

DROP TABLE IF EXISTS publisher;

CREATE TABLE publisher (
    publisherid INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

DROP TABLE IF EXISTS genre;

CREATE TABLE genre (
    genreid INT PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS ratings;

CREATE TABLE ratings (
    ratingid INT PRIMARY KEY,
    website_name VARCHAR(255),
    rating_number DOUBLE(5, 2),
    ratings_amount INT,
    reviews_amount INT
);

DROP TABLE IF EXISTS date_of_birth;

CREATE TABLE date_of_birth (
    day INT,
    month VARCHAR(9),
    year INT
);

DROP TABLE IF EXISTS book;

CREATE TABLE book (
    bookid INT PRIMARY KEY,
    bookname VARCHAR(255),
    seriesname VARCHAR(255),
    authorid_fk INT,
    publisherid_fk INT,
    genreid_fk INT,
    ratingid_fk INT,
    FOREIGN KEY (authorid_fk) REFERENCES author (authorid),
    FOREIGN KEY (publisherid_fk) REFERENCES publisher (publisherid),
    FOREIGN KEY (genreid_fk) REFERENCES genre (genreid),
    FOREIGN KEY (ratingid_fk) REFERENCES ratings (ratingid),
    isbn10 VARCHAR(10),
    isbn13 VARCHAR(13),
    price DOUBLE(255, 2),
    language VARCHAR(255),
    pages INT,
    book_format VARCHAR(255)
);

INSERT INTO book
  (bookid, bookname, seriesname, authorid_fk, publisherid_fk, genreid_fk, ratingid_fk, isbn10, isbn13, price, language, pages, book_format)
VALUES
  (1, 'The Way of Kings', 'The Stormlight Archive', 1, 1, 1, 23, '0765326353', '9780765326355', '20.94', 'English', 1008, 'Hardcover'),
  (2, 'The Name of the Wind', 'The Kingkiller Chronicles', 2, 3, 1, 56, '075640407X', '9780756404079', '26.72', 'English', 662, 'Hardcover');

INSERT INTO author
  (authorid, first_name, last_name, agentid_fk, email)
VALUES
  (1, 'Brandon', ' Sanderson', 27, 'N/A'),
  (2, 'Patrick', 'Rothfuss', 45, 'N/A');

INSERT INTO publisher
  (publisherid, name, email)
VALUES
  (1, 'Tor Books', 'submissions@tor.com'),
  (3, 'DAW Books', 'info@astrapublishinghouse.com');

INSERT INTO agent
  (agentid, first_name, last_name, email)
VALUES
  (27, 'Joshua', 'Bilmes', 'JABagent@aol.com'),
  (45, 'Matt', 'Bialer', 'querymb@sjga.com');

INSERT INTO genre
  (genreid, name)
VALUES
  (1, 'High Fantasy');

INSERT INTO ratings
  (ratingid, website_name, rating_number, ratings_amount, reviews_amount)
VALUES
  (23, 'Goodreads', '4.65', '400423', '27694'),
  (56, 'Goodreads', '4.52', '859265', '49213');

INSERT INTO date_of_birth
  (day, month, year)
VALUES
  (19, 'December', 1975),
  (6, 'June', 1973);