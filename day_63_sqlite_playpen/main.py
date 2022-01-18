import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# # Connects to the db, creates one if none exist
# db = sqlite3.connect('book-collections.db')
# #  cursor control our database.
# cursor = db.cursor()
# 
# # Create books table
# # cursor.execute("CREATE TABLE books ("
# #                "id INTEGER PRIMARY KEY,"
# #                "title varchar(250) NOT NULL UNIQUE,"
# #                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
