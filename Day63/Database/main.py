# my_solution
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
# from sqlalchemy import INTEGER, String
#
# #import sqlite3
# # db = sqlite3.connect('books-collection.db')
# # cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# # db.commit()
#


# class Base(DeclarativeBase):
#   pass
#
# db = (SQLAlchemy(model_class=Base))
#
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# # initialize the app with the extension
# db.init_app(app)
#
# class Books(db.Model):
#   id: Mapped[int] = mapped_column(primary_key=True)
#   title: Mapped[str] = mapped_column(unique=True,nullable=False)
#   author: Mapped[str] = mapped_column(nullable=False)
#   rating: Mapped[float] = mapped_column(nullable=False)
#
#
# with app.app_context():
#   db.create_all()



#sollution
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  author = db.Column(db.String(250), nullable=False)
  rating = db.Column(db.Float, nullable=False)

  # Optional: this will allow each book object to be identified by its title when printed.
  def __repr__(self):
    return f'<Book {self.title}>'

with app.app_context():
  db.create_all()

  # CREATE RECORD
  new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
  db.session.add(new_book)
  db.session.commit()

