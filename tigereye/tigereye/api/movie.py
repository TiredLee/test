from flask_classy import FlaskView
from tigereye.api import ApiView
from tigereye.models.movie import Movie
from flask import jsonify


class MovieView(ApiView):
    def all(self):
        movies = Movie.query.all()
        return movies
