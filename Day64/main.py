from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField,HiddenField
from wtforms.validators import DataRequired
import requests


API_AUTHORIZATION = """API KEY"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

class FindMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")
@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html",movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = request.form.get("title")
        list_of_movies = search_movie(movie_title)
        return render_template("select.html",movies=list_of_movies)

    return render_template("add.html", form=form)

@app.route("/select")
def select():
    movie_id = request.args.get("id")
    if movie_id:
        movie = get_movie(movie_id)
        title = movie["title"]
        description = movie["overview"]
        img_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        year = int(movie["release_date"].split("-")[0])

        new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('rate_movie', id=new_movie.id))

def search_movie(title):
    headers = {
        'authorization': f'Bearer {API_AUTHORIZATION}',
    }
    params = {
        'query': title,
    }
    response = requests.get('https://api.themoviedb.org/3/search/movie', headers=headers, params=params)
    return response.json()['results']


def get_movie(movie_id):
    headers = {
        'authorization': f'Bearer {API_AUTHORIZATION}',
    }
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}', headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
